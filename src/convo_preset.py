"""Freaky Frankenstein 5.4 · DM Edition: the Conversation-mode prompt, packaged three ways.

- preset():  the original FF 5.4 (Agent Gating) preset, unchanged for Roleplay mode, with
             `conversationPrompt` filled in, so one preset drives both modes.
- PROMPT:    the bare template, for pasting into a preset's Conversation Prompt field or a
             chat's custom system prompt.
- regex_scripts(): the companion regex scripts for the optional LEDGER state mode.
"""

import copy
import datetime
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent / "convo"
SOURCE = HERE / "Freaky_Frankenstein_5.4_Agent_Gating.source.marinara.json"
PROMPT = (HERE / "freaky_frankenstein_dm.txt").read_text(encoding="utf-8").strip() + "\n"

NAME = "Freaky Frankenstein 5.4 · DM Edition"
DESCRIPTION = (
    "FF 5.4 (Agent Gating) by Dbtgreg, with a full Conversation/DM prompt ported from it: "
    "texting fingerprint voice, phone-physics anti-omniscience, instincts + VAD, realistic people, "
    "banned words, person genesis, REALISM/FREAKY sexting modes, anti-parrot, life sim d20, agenda, "
    "bonds, Chekhov's gun, dice, thoughts, notebook, optional hidden ledger, debug, and MICRO/BOLT/MAX "
    "reasoning. Roleplay mode is the original preset, unchanged. DM toggles live in the SETTINGS "
    "block at the top of the Conversation Prompt."
)

# The ledger is optional (ff_state = LEDGER). Pattern also matches an unterminated block while a
# reply is still streaming.
LEDGER_PATTERN = r"\n*<ledger>[\s\S]*?(?:<\/ledger>|$)"


def regex_scripts():
    return [
        {
            "name": "FF DM · Hide ledger",
            "enabled": True,
            "findRegex": LEDGER_PATTERN,
            "replaceString": "",
            "trimStrings": [],
            "placement": ["ai_output"],
            "flags": "gi",
            "promptOnly": False,
            "applyMode": "display",
            "targetCharacterIds": [],
            "targetPromptPresetIds": [],
            "order": 0,
            "minDepth": None,
            "maxDepth": None,
        },
        {
            # Keep only the newest ledger or two in the prompt; older ones are dead weight.
            "name": "FF DM · Strip old ledgers from prompt",
            "enabled": True,
            "findRegex": LEDGER_PATTERN,
            "replaceString": "",
            "trimStrings": [],
            "placement": ["ai_output"],
            "flags": "gi",
            "promptOnly": True,
            "applyMode": "prompt",
            "targetCharacterIds": [],
            "targetPromptPresetIds": [],
            "order": 1,
            "minDepth": 4,
            "maxDepth": None,
        },
    ]


def preset():
    env = json.loads(SOURCE.read_text(encoding="utf-8"))
    env = copy.deepcopy(env)
    p = env["data"]["preset"]
    p["name"] = NAME
    p["description"] = DESCRIPTION
    p["conversationPrompt"] = PROMPT
    p["isDefault"] = False
    p["author"] = "Dbtgreg (FF 5.4); DM Edition conversation prompt added"
    now = datetime.datetime(2026, 9, 25, tzinfo=datetime.timezone.utc).isoformat().replace("+00:00", ".000Z")
    p["updatedAt"] = now
    env["exportedAt"] = now
    return env
