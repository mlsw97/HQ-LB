import assert from "node:assert/strict";
import { mkdtempSync, readFileSync, readdirSync } from "node:fs";
import { createRequire } from "node:module";
import { tmpdir } from "node:os";
import { join } from "node:path";

const dir = mkdtempSync(join(tmpdir(), "marinara-hq-"));
process.env.DATA_DIR = dir;
process.env.FILE_STORAGE_DIR = join(dir, "storage");
process.env.NODE_ENV = "test";
process.env.LOG_LEVEL = "silent";
const requireServer = createRequire(new URL("../../packages/server/package.json", import.meta.url));
const Fastify = requireServer("fastify") as typeof import("fastify").default;
const { getDB } = await import("../../packages/server/src/db/connection.js");
const { importRoutes } = await import("../../packages/server/src/routes/import.routes.js");
const { createLorebooksStorage } = await import("../../packages/server/src/services/storage/lorebooks.storage.js");
const { processLorebooks } = await import("../../packages/server/src/services/lorebook/index.js");

const DIST = process.env.HQ_DIST!;
const db = await getDB();
const app = Fastify({ bodyLimit: 50 * 1024 * 1024 });
app.decorate("db", db);
await app.register(importRoutes, { prefix: "/api/import" });
const storage = createLorebooksStorage(db);

const files = readdirSync(DIST).filter((f) => f.endsWith(".marinara.json")).sort();
assert.equal(files.length, 5, "five lorebook files");
const ids: string[] = [];
for (const f of files) {
  const raw = JSON.parse(readFileSync(join(DIST, f), "utf8"));
  const res = await app.inject({ method: "POST", url: "/api/import/marinara", payload: raw });
  assert.equal(res.statusCode, 200, `${f}: ${res.body}`);
  const body = res.json();
  assert.equal(body.success, true, `${f}: ${res.body}`);
  assert.equal(body.type, "marinara_lorebook");
  ids.push(body.id);
  const entries = (await storage.listEntries(body.id)) as any[];
  const folders = (await storage.listFolders(body.id)) as any[];
  assert.equal(entries.length, raw.data.entries.length, `${f}: entry count`);
  assert.equal(folders.length, raw.data.folders.length, `${f}: folder count`);
  const folderIds = new Set(folders.map((x) => x.id));
  for (const e of entries) {
    assert.ok(e.folderId && folderIds.has(e.folderId), `${f}/${e.name}: folder remapped`);
    const src = raw.data.entries.find((x: any) => x.name === e.name);
    assert.equal(e.content, src.content, `${f}/${e.name}: content round-trip`);
    assert.deepEqual(e.keys, src.keys, `${f}/${e.name}: keys round-trip`);
    assert.equal(e.description, src.description);
    assert.equal(e.matchWholeWords, true);
    assert.equal(e.sticky, src.sticky);
  }
  console.log(`imported ${f}: ${entries.length} entries in ${folders.length} folders`);
}

const scan = async (text: string) => {
  const r = await processLorebooks(db, [{ role: "user", content: text }], null, {
    activeLorebookIds: ids,
    characterIds: [],
    previewOnly: true,
    random: () => 0,
  });
  return r;
};

const probes: Array<[string, string[]]> = [
  ["Hey Harley, how's it going?", ["Harley Quinn — Core Profile", "Harley Quinn — Voice & Speech Guide"]],
  ["Do you still think about Mistah J?", ["The Joker — History with Harley"]],
  ["Ivy called, she says hi.", ["Poison Ivy — Harley's Great Love"]],
  ["Where are Bud and Lou? I brought treats for the hyenas.", ["Bud & Lou — The Hyenas"]],
  ["Tell me about Coney Island and Big Tony.", ["Big Tony (Anthony Delfini)", "Coney Island Arrival — Hot in the City (2013–2014)"]],
  ["Grab your mallet, we're going to Arkham.", ["Signature Weapon — The Mallet", "Arkham Asylum & Arkham Tower"]],
  ["How did you and the Joker first meet? Tell me about Mad Love.", ["Origin — Mad Love (the classic version)"]],
  ["What happened to your mom, Sharon?", ["Sharon Quinzel — Harley's Mother"]],
  ["Althea Klang is gentrifying Throatcutter Hill again.", ["Althea Klang", "Throatcutter Hill"]],
  ["I loved Margot Robbie in Birds of Prey.", ["DC Extended Universe Harley (Margot Robbie)"]],
  ["Hiya, Lou! Get off the couch!", ["Bud & Lou — The Hyenas"]],
  ["Red and black jacket, crazy busy right now, want some cake? Let's fight about our date.", []],
  ["Nothing relevant here at all, just weather talk.", []],
];
for (const [text, expected] of probes) {
  const r = await scan(text);
  const names = r.activatedEntries.map((e) => e.name);
  for (const n of expected) assert.ok(names.includes(n), `"${text}" should activate "${n}", got ${JSON.stringify(names)}`);
  console.log(`probe "${text}" -> ${names.length} entries, ~${r.totalTokensEstimate} tokens: ${names.join(" | ")}`);
  if (r.budgetSkippedEntries.length) console.log(`  budget-skipped: ${r.budgetSkippedEntries.map((e) => e.name).join(", ")}`);
}
for (const t of ["Nothing relevant here at all, just weather talk.", "Red and black jacket, crazy busy right now, want some cake? Let's fight about our date."]) {
  const quiet = await scan(t);
  assert.equal(quiet.activatedEntries.length, 2, `only the two constant entries fire on everyday text: ${quiet.activatedEntries.map((e) => e.name)}`);
}
console.log("ALL HQ LOREBOOK CHECKS PASSED");
process.exit(0);
