// Verifies Freaky Frankenstein 5.4 · DM Edition inside a real Marinara Engine checkout.
// Copy to <marinara>/scripts/regressions/ and run with tsx, with HQ_DIST pointing at this repo's dist/.
// It imports the preset and the Harley card, starts a Conversation-mode chat, runs Marinara's real
// /api/generate route against a local fake model, and inspects the exact prompt that would be sent.
import assert from "node:assert/strict";
import { mkdtempSync, readFileSync, writeFileSync } from "node:fs";
import { createServer } from "node:http";
import { createRequire } from "node:module";
import { tmpdir } from "node:os";
import { join } from "node:path";

const dir = mkdtempSync(join(tmpdir(), "marinara-hq-dm-"));
process.env.DATA_DIR = dir;
process.env.FILE_STORAGE_DIR = join(dir, "storage");
process.env.NODE_ENV = "test";
process.env.MARINARA_LITE = "true";
process.env.LOG_LEVEL = "silent";
const requireServer = createRequire(new URL("../../packages/server/package.json", import.meta.url));
const Fastify = requireServer("fastify") as typeof import("fastify").default;
const { getDB } = await import("../../packages/server/src/db/connection.js");
const { importRoutes } = await import("../../packages/server/src/routes/import.routes.js");
const { generateRoutes } = await import("../../packages/server/src/routes/generate.routes.js");
const { regexScriptsRoutes } = await import("../../packages/server/src/routes/regex-scripts.routes.js");
const { createChatsStorage } = await import("../../packages/server/src/services/storage/chats.storage.js");
const { createConnectionsStorage } = await import("../../packages/server/src/services/storage/connections.storage.js");
const { createPromptsStorage } = await import("../../packages/server/src/services/storage/prompts.storage.js");
const { applyRegexScriptsToPromptText } = await import("../../packages/server/src/services/regex/regex-application.js");
const { importRegexScriptSchema } = await import("../../packages/shared/src/schemas/regex.schema.js");
const { isPatternSafe } = await import("../../packages/shared/src/utils/regex-safety.js");

const DIST = process.env.HQ_DIST!;
const presetEnv = JSON.parse(readFileSync(join(DIST, "Freaky-Frankenstein-5.4-DM-Edition.preset.marinara.json"), "utf8"));
const cardEnv = JSON.parse(readFileSync(join(DIST, "Harley-Quinn.character.marinara.json"), "utf8"));
const promptTxt = readFileSync(join(DIST, "Freaky-Frankenstein-DM-Prompt.txt"), "utf8");
const regexFile = JSON.parse(readFileSync(join(DIST, "Freaky-Frankenstein-DM-Ledger.regex.json"), "utf8"));
assert.equal(presetEnv.data.preset.conversationPrompt, promptTxt, "preset and .txt carry the same prompt");

// ── Fake model: records every chat request ──
const sent: Array<Array<{ role: string; content: string }>> = [];
let reply = "lmao ok";
const provider = createServer(async (req, res) => {
  const chunks: Buffer[] = [];
  for await (const chunk of req) chunks.push(Buffer.from(chunk));
  const body = JSON.parse(Buffer.concat(chunks).toString() || "{}");
  if (Array.isArray(body.messages)) sent.push(body.messages);
  const content = reply;
  if (body.stream) {
    res.writeHead(200, { "content-type": "text/event-stream" });
    res.end(
      `data: ${JSON.stringify({ choices: [{ index: 0, delta: { content }, finish_reason: null }] })}\n\n` +
        `data: ${JSON.stringify({ choices: [{ index: 0, delta: {}, finish_reason: "stop" }] })}\n\ndata: [DONE]\n\n`,
    );
  } else {
    res.writeHead(200, { "content-type": "application/json" });
    res.end(JSON.stringify({ choices: [{ index: 0, message: { role: "assistant", content }, finish_reason: "stop" }] }));
  }
});
await new Promise<void>((done) => provider.listen(0, "127.0.0.1", done));
const port = (provider.address() as { port: number }).port;

const db = await getDB();
const app = Fastify({ bodyLimit: 50 * 1024 * 1024 });
app.decorate("db", db);
await app.register(importRoutes, { prefix: "/api/import" });
await app.register(generateRoutes, { prefix: "/api/generate" });
await app.register(regexScriptsRoutes, { prefix: "/api/regex-scripts" });

// ── Import preset + card through the real importer ──
const imp = async (payload: unknown) => {
  const res = await app.inject({ method: "POST", url: "/api/import/marinara", payload });
  assert.equal(res.statusCode, 200, res.body);
  const body = res.json();
  assert.equal(body.success, true, res.body);
  return body;
};
const presetImport = await imp(presetEnv);
assert.equal(presetImport.type, "marinara_preset");
const presets = createPromptsStorage(db);
const stored = (await presets.getById(presetImport.id)) as any;
assert.equal(stored.conversationPrompt, promptTxt, "conversationPrompt round-trips through import");
assert.equal(stored.name, "Freaky Frankenstein 5.4 · DM Edition");
const sections = await presets.listSections(presetImport.id);
assert.equal(sections.length, presetEnv.data.sections.length, "roleplay sections imported unchanged");
const harley = await imp(cardEnv);

const connection = await createConnectionsStorage(db).create({
  name: "fixture", provider: "custom", baseUrl: `http://127.0.0.1:${port}/v1`, model: "fixture", apiKey: "x",
  maxContext: 200000, maxTokensOverride: 512,
});
const chats = createChatsStorage(db);

// A preset variant with edited SETTINGS values, the way a user would edit them.
const withSettings = async (name: string, edits: Record<string, string>) => {
  let text = promptTxt;
  for (const [k, v] of Object.entries(edits)) {
    const re = new RegExp(`\\{\\{setvar::${k}::[^}]*\\}\\}`);
    assert.ok(re.test(text), `setting ${k} exists`);
    text = text.replace(re, `{{setvar::${k}::${v}}}`);
  }
  const p = await presets.create({ name, wrapFormat: "none" } as any);
  await presets.update(p!.id, { conversationPrompt: text } as any);
  return p!.id;
};

const newChat = async (presetId: string, history: Array<[string, string]>) => {
  const chat = await chats.create({
    name: "DM", mode: "conversation", characterIds: [harley.id], connectionId: connection.id, promptPresetId: presetId,
  });
  await chats.patchMetadata(chat!.id, { enableAgents: false, autonomousMessages: false });
  for (const [role, content] of history) {
    await chats.createMessage({ chatId: chat!.id, role, characterId: role === "assistant" ? harley.id : null, content });
  }
  return chat!.id;
};

const generate = async (chatId: string, extra: Record<string, unknown> = {}) => {
  const before = sent.length;
  const res = await app.inject({ method: "POST", url: "/api/generate/", payload: { chatId, forCharacterId: harley.id, ...extra } });
  assert.equal(res.statusCode, 200, res.body);
  assert.ok(!res.body.includes('"type":"error"'), res.body.slice(0, 2000));
  const msgs = sent.slice(before).find((m) => m.some((x) => x.role === "system" && String(x.content).includes("<system_state>")));
  assert.ok(msgs, "a conversation request reached the model");
  const system = msgs!.filter((m) => m.role === "system").map((m) => String(m.content)).join("\n");
  if (process.env.HQ_DUMP) writeFileSync(join(process.env.HQ_DUMP, `prompt-${sent.length}.json`), JSON.stringify(msgs, null, 2));
  return { system, all: msgs! };
};

const common = (system: string, label: string) => {
  assert.ok(!/\{\{|\}\}/.test(system.replace(/\{\{user\}\}|\{\{char\}\}/g, "")), `${label}: no unresolved macros`);
  for (const leak of ["getvar::", "setvar::", "ff_toggles", "ff_modules", "SETTINGS", "author note"]) {
    assert.ok(!system.includes(leak), `${label}: "${leak}" must not leak into the prompt`);
  }
  assert.ok(system.includes("you ARE Harley Quinn"), `${label}: charName resolved`);
  assert.ok(system.includes("<texting_format>") && system.includes("<phone_physics>"), `${label}: core blocks present`);
};

// ── 1. Defaults, normal turn ──
const defaultChat = await newChat(presetImport.id, [["user", "hey harley, hows it going?"]]);
const d = await generate(defaultChat);
common(d.system, "defaults");
for (const want of [
  "Mode: NATURAL.", "Register: CINEMA.", "Mode: REALISM.", "Mode: ANTIPARROT.",
  "<texting_voice>", "<anti_omniscience>", "<instincts>", "<vad_emotion>", "<realistic_person>",
  "<banned_vocabulary>", "<person_genesis>", "<internal_states>", "<agenda>", "<life_sim>", "<bonds>",
  "<chekhovs_gun>", "<reasoning_protocol>", "9. Momentum:",
]) assert.ok(d.system.includes(want), `defaults include ${want}`);
for (const absent of [
  "<onomatopoeia>", "Mode: FREAKY", "Mode: PLAYALONG", "<dice_sim>", "<private_thoughts>", "<notebook>",
  "<ledger_protocol>", "<ledger>", "<reaching_out>", "<debug_engine>", "<enhance_definitions>", "Attachments:",
  "PHASE ALPHA", "5. Done:",
]) assert.ok(!d.system.includes(absent), `defaults exclude ${absent}`);
assert.match(d.system, /Life die this turn: ([1-9]|1\d|20)\n/, "life die rolled 1-20");
assert.match(d.system, /Seeds: (\d+) · (\d+) · (\d+) · (\d+) · (\d+)/, "five Chekhov seeds rolled");
assert.ok(d.system.includes("Nothing about them is ever written in a reply"), "SILENT state wording");
const approxTokens = Math.round(d.system.length / 4);
console.log(`defaults: system prompt ~${approxTokens} tokens (DM prompt + card + lore + engine blocks)`);

// ── 2. Autonomous message ──
const auto = await generate(defaultChat, { autonomous: true });
common(auto.system, "autonomous");
assert.ok(auto.system.includes("<reaching_out>"), "autonomous turn gets the reaching-out block");

// ── 3. Every switch flipped ──
const maxed = await withSettings("FF DM maxed", {
  ff_texting: "CHATTY", ff_prose: "STORY", ff_nsfw: "FREAKY", ff_echo: "PLAYALONG",
  ff_toggles: "ANTIOMNI VAD REALNPC BANNED GENESIS ONOMATO",
  ff_modules: "LIFE AGENDA BONDS CHEKHOV THOUGHTS DICE NOTEBOOK", ff_state: "LEDGER", ff_cot: "MAX",
  ff_extras: "MEDIA DEBUG ENHANCE",
});
const m = await generate(await newChat(maxed, [["user", "(ooc: state)"]]));
common(m.system, "maxed");
for (const want of [
  "Mode: CHATTY.", "Register: STORY.", "Mode: FREAKY.", "Mode: PLAYALONG.", "<onomatopoeia>", "<dice_sim>",
  "<private_thoughts>", "<notebook>", "<ledger_protocol>", "thought=[raw inner thought]", "dice=[task]",
  "notes=[R]/[T] entries", "<debug_engine>", "<enhance_definitions>", "Attachments:", "PHASE ALPHA",
  "Gate 10.", "E. DICE:", "F. Notebook", "Record it in the ledger.", "Build the ledger.",
]) assert.ok(m.system.includes(want), `maxed include ${want}`);
for (const absent of ["<texting_voice>", "Mode: NATURAL", "Mode: REALISM", "Mode: ANTIPARROT", "9. Momentum:", "In SILENT mode"])
  assert.ok(!m.system.includes(absent), `maxed exclude ${absent}`);

// ── 4. Everything off ──
const bare = await withSettings("FF DM bare", {
  ff_texting: "TERSE", ff_nsfw: "NONE", ff_toggles: "", ff_modules: "", ff_cot: "NONE",
});
const b = await generate(await newChat(bare, [["user", "yo"]]));
common(b.system, "bare");
assert.ok(b.system.includes("Mode: TERSE."));
for (const absent of ["<adult_mode>", "<texting_voice>", "<anti_omniscience>", "<internal_states>", "<reasoning_protocol>", "<life_sim>", "Life die"])
  assert.ok(!b.system.includes(absent), `bare exclude ${absent}`);
assert.ok(b.system.includes("Both Harley Quinn and"), "adult baseline stays even with NSFW mode NONE");
console.log(`bare: system prompt ~${Math.round(b.system.length / 4)} tokens`);

// ── 5. Ledger regex: valid, safe, hides the block, strips old copies from the prompt ──
for (const script of regexFile) {
  assert.ok(importRegexScriptSchema.safeParse(script).success, `${script.name} passes the import schema`);
  assert.ok(isPatternSafe(script.findRegex), `${script.name} passes the runtime safety check`);
  const res = await app.inject({ method: "POST", url: "/api/regex-scripts/import", payload: script });
  assert.equal(res.statusCode, 200, res.body);
}
const ledgerMsg = "lmaooo\nok fine ill tell u\n\n<ledger>\nturn=3 | now=23:10 | doing=couch\n</ledger>";
const display = regexFile.find((s: any) => s.applyMode === "display");
const shown = ledgerMsg.replace(new RegExp(display.findRegex, display.flags), "");
assert.equal(shown, "lmaooo\nok fine ill tell u", "display regex hides a finished ledger");
assert.equal("hi\n<ledger>\nturn=3 | now".replace(new RegExp(display.findRegex, display.flags), ""), "hi",
  "display regex hides a ledger still streaming");
const promptScripts = regexFile.filter((s: any) => s.applyMode === "prompt");
assert.equal(applyRegexScriptsToPromptText(ledgerMsg, promptScripts, "ai_output", 1), ledgerMsg, "recent ledger kept");
assert.equal(applyRegexScriptsToPromptText(ledgerMsg, promptScripts, "ai_output", 6), "lmaooo\nok fine ill tell u",
  "old ledger stripped");

const ledgerChat = await newChat(maxed, [
  ["user", "morning"], ["assistant", "OLDEST_TEXT\n<ledger>\nOLDEST_LEDGER\n</ledger>"],
  ["user", "what are u doing"], ["assistant", "OLD_TEXT\n<ledger>\nOLD_LEDGER\n</ledger>"],
  ["user", "cool"], ["assistant", "NEWEST_TEXT\n<ledger>\nNEWEST_LEDGER\n</ledger>"], ["user", "lol"],
]);
const l = await generate(ledgerChat);
const history = l.all.map((x) => String(x.content)).join("\n");
assert.ok(history.includes("NEWEST_LEDGER"), "the newest ledger reaches the model");
assert.ok(!history.includes("OLDEST_LEDGER"), "old ledgers are stripped from the prompt");
assert.ok(history.includes("OLDEST_TEXT"), "stripping keeps the texts themselves");

console.log("ALL DM PROMPT CHECKS PASSED");
provider.close();
process.exit(0);
