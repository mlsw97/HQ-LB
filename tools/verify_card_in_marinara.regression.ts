import assert from "node:assert/strict";
import { mkdtempSync, readFileSync } from "node:fs";
import { createRequire } from "node:module";
import { tmpdir } from "node:os";
import { join } from "node:path";

const dir = mkdtempSync(join(tmpdir(), "marinara-hq-card-"));
process.env.DATA_DIR = dir;
process.env.FILE_STORAGE_DIR = join(dir, "storage");
process.env.NODE_ENV = "test";
process.env.LOG_LEVEL = "silent";
const requireServer = createRequire(new URL("../../packages/server/package.json", import.meta.url));
const Fastify = requireServer("fastify") as typeof import("fastify").default;
const { getDB } = await import("../../packages/server/src/db/connection.js");
const { importRoutes } = await import("../../packages/server/src/routes/import.routes.js");
const { createCharactersStorage } = await import("../../packages/server/src/services/storage/characters.storage.js");
const { loadCharacterPromptInfo } = await import("../../packages/server/src/services/generation/character-prompt-context.js");
const { characterDataSchema } = await import("../../packages/shared/src/schemas/character.schema.js");

const raw = JSON.parse(readFileSync(process.env.HQ_CARD!, "utf8"));
const src = raw.data.data;
assert.ok(characterDataSchema.safeParse(src).success, "card data passes Marinara's characterDataSchema");

const db = await getDB();
const app = Fastify({ bodyLimit: 50 * 1024 * 1024 });
app.decorate("db", db);
await app.register(importRoutes, { prefix: "/api/import" });
const res = await app.inject({ method: "POST", url: "/api/import/marinara", payload: raw });
assert.equal(res.statusCode, 200, res.body);
const body = res.json();
assert.equal(body.success, true, res.body);
assert.equal(body.type, "marinara_character");
assert.equal(body.name, "Harley Quinn");

const chars = createCharactersStorage(db);
const row = (await chars.getById(body.id)) as any;
const stored = typeof row.data === "string" ? JSON.parse(row.data) : row.data;
for (const k of ["name", "summary", "description", "personality", "scenario", "first_mes", "mes_example",
  "creator_notes", "system_prompt", "post_history_instructions", "character_version"]) {
  assert.equal(stored[k], src[k], `field ${k} round-trips`);
}
assert.deepEqual(stored.alternate_greetings, src.alternate_greetings, "alternate greetings round-trip");
assert.deepEqual(stored.tags, src.tags, "tags round-trip");
for (const k of ["backstory", "appearance", "nameColor", "dialogueColor", "talkativeness", "phoneticName"]) {
  assert.deepEqual(stored.extensions[k], src.extensions[k], `extension ${k} round-trips`);
}
assert.deepEqual(stored.extensions.nameAliases, src.extensions.nameAliases);
assert.deepEqual(stored.extensions.trackerCustomFieldDefaults, src.extensions.trackerCustomFieldDefaults);
assert.equal(stored.extensions.rpgStats.enabled, false);

const [info] = await loadCharacterPromptInfo({ chars, characterIds: [body.id], chatMode: "roleplay" });
assert.equal(info.name, "Harley Quinn");
for (const [k, v] of Object.entries({
  description: src.description, personality: src.personality, scenario: src.scenario,
  backstory: src.extensions.backstory, appearance: src.extensions.appearance, mesExample: src.mes_example,
  systemPrompt: src.system_prompt, postHistoryInstructions: src.post_history_instructions, firstMes: src.first_mes,
})) {
  assert.ok((info as any)[k].length > 0, `${k} reaches the prompt`);
  assert.equal((info as any)[k], v, `${k} reaches the prompt unchanged`);
}
console.log(`imported "${body.name}" (${body.id}); ${1 + stored.alternate_greetings.length} greetings; all prompt fields intact`);
console.log("ALL HQ CARD CHECKS PASSED");
process.exit(0);
