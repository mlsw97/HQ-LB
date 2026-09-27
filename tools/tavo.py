"""Convert the Harley Quinn card and lorebooks to Tavo's import formats.

Tavo (docs.tavoai.dev, TavoJS API reference) imports:
- character cards as Character Card V3 JSON ({"spec": "chara_card_v3", ...}), V2, or SillyTavern
  wrappers; a card's `character_book` becomes a Tavo lorebook on import;
- lorebooks as standalone {"spec": "lorebook_v3", "data": {...}}, a bare CCv3 lorebook, SillyTavern
  World Info, or Tavo-native objects.

Every entry here is written with CCv3 fields (Tavo's preferred format), SillyTavern's character_book
extensions (sticky, depth, scan depth, whole-word matching), and the equivalent Tavo-native fields, so
the timing settings survive whichever reader Tavo applies.

Tavo has no Appearance, Backstory or Summary fields, so those Marinara fields are folded into
Description and Creator Notes. Called from tools/build.py; writes dist/tavo/.
"""

import copy
import json
import pathlib
import re

CREATOR_NOTES = """HARLEY QUINN: comprehensive character card, Tavo edition.
• Canon baseline: main-universe DC comics, current through 2026 (Throatcutter Hill, post-Ivy-breakup, the Klang flirtation). Adaptation details are used only where they don't contradict canon.
• Greetings: the default is the present day at her "destructive agency". Swipe the first message for the alternates: (1) Coney Island landlady, 2014; (2) Belle Reve and the Suicide Squad; (3) the classic 1990s Joker hideout; (4) Dr. Quinzel at Arkham before the fall; (5) the rooftop the night Ivy ends it; (6) a "Batquinn" alley rescue; (7) court-ordered therapy with Dr. Quinzel.
• Content: UNFILTERED by design. Graphic violence, abuse themes, explicit adult sexuality, heavy profanity. Adults only.
• Lore: import the five "Harley Quinn — 01…05" lorebook files (or use the "with all lorebooks" version of this card) and turn them on in the chat's World Book settings. The card also works alone.
• With the lorebooks on, you can disable "Harley Quinn — Core Profile" and "Harley Quinn — Voice & Speech Guide" in lorebook 01 to save about 950 tokens per turn, because the card covers them. Keep "Tone Directive — Unfiltered Harley" on.
• Avatar: none included. Add your own image in Tavo."""


def _entry(e, index, book_scan_depth):
    """One Marinara lorebook entry -> CCv3 entry + SillyTavern extensions + Tavo-native fields."""
    if e["position"] != 0 or e["useRegex"] or e["secondaryKeys"]:
        # Everything in this repo is keyword/constant, before-char, plain keys. Fail loudly if that changes.
        raise ValueError(f"unsupported entry shape for Tavo conversion: {e['name']}")
    scan_depth = e["scanDepth"] if e["scanDepth"] is not None else book_scan_depth
    sticky = e["sticky"] or 0
    return {
        # Character Card V3 lorebook entry
        "id": index,
        "name": e["name"],
        "comment": e["name"],
        "keys": list(e["keys"]),
        "secondary_keys": [],
        "content": e["content"],
        "enabled": e["enabled"],
        "constant": e["constant"],
        "selective": False,
        "insertion_order": e["order"],
        "priority": e["order"],
        "case_sensitive": e["caseSensitive"],
        "use_regex": False,
        "position": "before_char",
        # Top-level copies some SillyTavern-compatible readers look for instead of `extensions`
        "match_whole_words": e["matchWholeWords"],
        "scan_depth": scan_depth,
        "depth": e["depth"],
        # SillyTavern character_book extensions (what ST writes when it exports a card)
        "extensions": {
            "position": 0,
            "depth": e["depth"],
            "role": 0,
            "probability": 100,
            "useProbability": False,
            "selectiveLogic": 0,
            "scan_depth": scan_depth,
            "match_whole_words": e["matchWholeWords"],
            "case_sensitive": e["caseSensitive"],
            "sticky": sticky,
            "cooldown": 0,
            "delay": 0,
            "group": "",
            "group_override": False,
            "group_weight": 100,
            "prevent_recursion": True,
            "exclude_recursion": False,
            "delay_until_recursion": False,
            "display_index": index,
            "vectorized": False,
            "description": e["description"],
        },
        # Tavo-native fields (TavoJS LorebookEntry)
        "identifier": e["id"],
        "strategy": "constant" if e["constant"] else "keyword",
        "keywords": list(e["keys"]),
        "secondaryKeywords": [],
        "secondaryKeywordStrategy": "none",
        "scanDepth": scan_depth,
        "caseSensitive": e["caseSensitive"],
        "matchWholeWord": e["matchWholeWords"],
        "injectionPosition": "lorebookBefore",
        "injectionDepth": e["depth"],
        "injectionRole": "system",
        "probability": 100,
        "sticky": sticky,
        "cooldown": 0,
        "delay": 0,
    }


def _entries_in_order(book):
    """Folder order first (as shown in Marinara), then entry order, so Tavo's list reads the same way."""
    folder_rank = {f["id"]: i for i, f in enumerate(book.folders)}
    return sorted(book.entries, key=lambda e: (folder_rank.get(e["folderId"], -1), e["order"]))


def lorebook(book):
    lb = book.lorebook
    entries = [_entry(e, i, lb["scanDepth"]) for i, e in enumerate(_entries_in_order(book))]
    return {
        "name": lb["name"],
        "description": lb["description"],
        "scan_depth": lb["scanDepth"],
        "token_budget": lb["tokenBudget"],
        "recursive_scanning": lb["recursiveScanning"],
        "extensions": {},
        "entries": entries,
    }


def lorebook_file(book):
    return {"spec": "lorebook_v3", "data": lorebook(book)}


def merged_lorebook(books):
    entries = []
    for book in books:
        for e in lorebook(book)["entries"]:
            e = copy.deepcopy(e)
            e["id"] = e["extensions"]["display_index"] = len(entries)
            entries.append(e)
    return {
        "name": "Harley Quinn — Complete Lore",
        "description": "All five Harley Quinn lorebooks (core identity, canon history, relationships, "
                       "places/things, adaptations) in one book.",
        "scan_depth": max(b.lorebook["scanDepth"] for b in books),
        "token_budget": 8000,
        "recursive_scanning": False,
        "extensions": {},
        "entries": entries,
    }


def _description(x):
    ext = x["extensions"]
    return "\n\n".join([
        x["description"].strip(),
        ext["appearance"].strip(),
        ext["backstory"].strip(),
    ])


def card(marinara_card_env, book=None):
    x = marinara_card_env["data"]["data"]
    data = {
        "name": x["name"],
        "nickname": "",
        "description": _description(x),
        "personality": x["personality"],
        "scenario": x["scenario"],
        "first_mes": x["first_mes"],
        "alternate_greetings": list(x["alternate_greetings"]),
        "group_only_greetings": [],
        "mes_example": x["mes_example"],
        "system_prompt": x["system_prompt"],
        "post_history_instructions": x["post_history_instructions"],
        "creator_notes": x["summary"].strip() + "\n\n" + CREATOR_NOTES,
        "tags": list(x["tags"]),
        "creator": x["creator"],
        "character_version": x["character_version"],
        "source": ["https://github.com/mlsw97/hq-lb"],
        "creation_date": 1790208000,       # 2026-09-24T00:00:00Z
        "modification_date": 1790208000,
        "assets": [{"type": "icon", "uri": "ccdefault:", "name": "main", "ext": "png"}],
        "extensions": {
            "talkativeness": str(x["extensions"].get("talkativeness", 0.5)),
            "fav": False,
            "world": book["name"] if book else "",
            "depth_prompt": {"prompt": "", "depth": 4, "role": "system"},
        },
    }
    if book:
        data["character_book"] = book
    return {"spec": "chara_card_v3", "spec_version": "3.0", "data": data}


def validate_card(env):
    """Structural check against the Character Card V3 spec."""
    problems = []
    if env.get("spec") != "chara_card_v3" or env.get("spec_version") != "3.0":
        problems.append("spec/spec_version")
    d = env["data"]
    for k in ("name", "description", "tags", "creator", "character_version", "mes_example", "extensions",
              "system_prompt", "post_history_instructions", "first_mes", "alternate_greetings",
              "personality", "scenario", "creator_notes", "group_only_greetings"):
        if k not in d:
            problems.append(f"card missing {k}")
    for k in ("tags", "alternate_greetings", "group_only_greetings"):
        if not isinstance(d.get(k), list):
            problems.append(f"card {k} must be a list")
    if not d["first_mes"].strip() or not d["name"].strip():
        problems.append("Tavo requires name and first_mes")
    if "character_book" in d:
        problems += validate_book(d["character_book"])
    return problems


def validate_book(b):
    problems = []
    if not isinstance(b.get("entries"), list) or not isinstance(b.get("extensions"), dict):
        return ["lorebook needs entries[] and extensions{}"]
    for e in b["entries"]:
        for k, t in (("keys", list), ("content", str), ("extensions", dict), ("enabled", bool),
                     ("insertion_order", int), ("use_regex", bool)):
            if not isinstance(e.get(k), t):
                problems.append(f"{b['name']} / {e.get('name')}: {k} must be {t.__name__}")
        if not e["content"].strip():
            problems.append(f"{b['name']} / {e['name']}: empty content")
        if not e["constant"] and not e["keys"]:
            problems.append(f"{b['name']} / {e['name']}: keyword entry without keys")
        if e.get("position") not in ("before_char", "after_char"):
            problems.append(f"{b['name']} / {e['name']}: bad position")
    ids = [e["id"] for e in b["entries"]]
    if len(ids) != len(set(ids)):
        problems.append(f"{b['name']}: duplicate entry ids")
    return problems


def build(out_dir, books, marinara_card_env):
    out_dir.mkdir(parents=True, exist_ok=True)
    for old in out_dir.glob("*.json"):
        old.unlink()
    problems = []
    for book in books:
        env = lorebook_file(book)
        problems += validate_book(env["data"])
        slug = re.sub(r"[^A-Za-z0-9]+", "-", book.name).strip("-")
        (out_dir / f"{slug}.tavo.lorebook.json").write_text(
            json.dumps(env, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    plain = card(marinara_card_env)
    full = card(marinara_card_env, merged_lorebook(books))
    for env, name in ((plain, "Harley-Quinn.tavo.card.json"),
                      (full, "Harley-Quinn-with-all-lorebooks.tavo.card.json")):
        problems += validate_card(env)
        (out_dir / name).write_text(json.dumps(env, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    n = len(full["data"]["character_book"]["entries"])
    print(f"tavo/: 5 lorebooks, card, card with {n} embedded entries")
    return problems
