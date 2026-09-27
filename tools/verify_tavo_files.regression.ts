// Checks the Tavo files (dist/tavo/) with an independent SillyTavern/Character Card V3 reader.
// Tavo itself is a closed mobile app, so this uses Marinara Engine's SillyTavern importers, which read
// chara_card_v3 cards, embedded character_book lorebooks and CCv3/World Info lorebooks.
// Copy to <marinara>/scripts/regressions/ and run with tsx, with HQ_DIST pointing at this repo's dist/.
import assert from "node:assert/strict";
import { mkdtempSync, readFileSync, readdirSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";

const dir = mkdtempSync(join(tmpdir(), "marinara-hq-tavo-"));
process.env.DATA_DIR = dir;
process.env.FILE_STORAGE_DIR = join(dir, "storage");
process.env.NODE_ENV = "test";
process.env.LOG_LEVEL = "silent";
const { getDB } = await import("../../packages/server/src/db/connection.js");
const { importSTLorebook } = await import("../../packages/server/src/services/import/st-lorebook.importer.js");
const { importSTCharacter } = await import("../../packages/server/src/services/import/st-character.importer.js");
const { createLorebooksStorage } = await import("../../packages/server/src/services/storage/lorebooks.storage.js");
const { createCharactersStorage } = await import("../../packages/server/src/services/storage/characters.storage.js");

const DIST = process.env.HQ_DIST!;
const TAVO = join(DIST, "tavo");
const db = await getDB();
const lorebooks = createLorebooksStorage(db);
const characters = createCharactersStorage(db);
const read = (f: string) => JSON.parse(readFileSync(join(TAVO, f), "utf8"));

// Source of truth: the Marinara-native books.
const marinara = readdirSync(DIST).filter((f) => /^Harley-Quinn-0\d.*\.marinara\.json$/.test(f)).sort()
  .map((f) => JSON.parse(readFileSync(join(DIST, f), "utf8")).data);
const byName = new Map(marinara.flatMap((b: any) => b.entries.map((e: any) => [e.name, e])));
assert.equal(byName.size, 114);

const checkEntries = async (lorebookId: string, expected: number, label: string) => {
  const got = (await lorebooks.listEntries(lorebookId)) as any[];
  assert.equal(got.length, expected, `${label}: entry count`);
  for (const e of got) {
    const src: any = byName.get(e.name);
    assert.ok(src, `${label}: unknown entry ${e.name}`);
    assert.equal(e.content, src.content, `${label} / ${e.name}: content`);
    assert.deepEqual(e.keys, src.keys, `${label} / ${e.name}: keys`);
    assert.equal(Boolean(e.constant), src.constant, `${label} / ${e.name}: constant`);
    assert.equal(Boolean(e.enabled), true, `${label} / ${e.name}: enabled`);
    assert.equal(Boolean(e.matchWholeWords), true, `${label} / ${e.name}: whole words`);
    assert.equal(Boolean(e.caseSensitive), false, `${label} / ${e.name}: case-insensitive`);
    assert.equal(e.position, 0, `${label} / ${e.name}: before character`);
  }
  return got;
};

// 1. The five standalone lorebook_v3 files.
const bookFiles = readdirSync(TAVO).filter((f) => f.endsWith(".tavo.lorebook.json")).sort();
assert.equal(bookFiles.length, 5);
for (const [i, f] of bookFiles.entries()) {
  const env = read(f);
  assert.equal(env.spec, "lorebook_v3", `${f}: spec`);
  const res: any = await importSTLorebook(env.data, db);
  assert.equal(res.success, true, `${f}: imported`);
  assert.equal(res.name, marinara[i].lorebook.name, `${f}: name`);
  const got = await checkEntries(res.lorebookId, marinara[i].entries.length, f);
  const stickyOk = got.every((e) => (e.sticky ?? 0) === ((byName.get(e.name) as any).sticky ?? 0));
  assert.ok(stickyOk, `${f}: sticky durations survive`);
  console.log(`${f}: ${got.length} entries OK`);
}

// 2. The card alone, and the card with all lorebooks embedded.
const source = JSON.parse(readFileSync(join(DIST, "Harley-Quinn.character.marinara.json"), "utf8")).data.data;
for (const [f, embedded] of [["Harley-Quinn.tavo.card.json", 0], ["Harley-Quinn-with-all-lorebooks.tavo.card.json", 114]] as const) {
  const env = read(f);
  assert.equal(env.spec, "chara_card_v3");
  assert.equal(env.spec_version, "3.0");
  const res: any = await importSTCharacter(structuredClone(env), db);
  assert.ok(res && !res.error, `${f}: imported (${JSON.stringify(res).slice(0, 200)})`);
  const id = res.characterId ?? res.id;
  const row: any = await characters.getById(id);
  const data = typeof row.data === "string" ? JSON.parse(row.data) : row.data;
  assert.equal(data.name, "Harley Quinn");
  for (const k of ["personality", "scenario", "first_mes", "mes_example", "system_prompt", "post_history_instructions"])
    assert.equal(data[k], source[k], `${f}: ${k}`);
  assert.deepEqual(data.alternate_greetings, source.alternate_greetings, `${f}: 7 alternate greetings`);
  for (const part of [source.description, source.extensions.appearance, source.extensions.backstory])
    assert.ok(data.description.includes(part.trim()), `${f}: description carries profile, appearance and backstory`);
  if (embedded) {
    // This reader names the embedded book after the character; Tavo keeps its own naming.
    assert.ok(res.lorebook?.lorebookId, `${f}: embedded character_book became a lorebook`);
    await checkEntries(res.lorebook.lorebookId, embedded, f);
  }
  console.log(`${f}: card OK${embedded ? `, ${embedded} embedded entries OK` : ""}`);
}
console.log("ALL TAVO FILE CHECKS PASSED");
process.exit(0);
