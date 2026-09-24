"""Build every lorebook in src/ into dist/<name>.marinara.json and validate it.

Usage: python3 tools/build.py
"""

import importlib
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))

BOOK_MODULES = sorted(p.stem for p in (ROOT / "src").glob("book_*.py"))


def approx_tokens(text):
    return round(len(text) / 4)


def validate(book):
    problems = []
    folder_ids = {f["id"] for f in book.folders}
    for e in book.entries:
        where = f"{book.name} / {e['name']}"
        if e["folderId"] and e["folderId"] not in folder_ids:
            problems.append(f"{where}: unknown folder")
        if not e["content"]:
            problems.append(f"{where}: empty content")
        if not e["description"]:
            problems.append(f"{where}: empty description")
        if len(e["name"]) > 200:
            problems.append(f"{where}: name longer than 200 chars")
        for k in e["keys"] + e["secondaryKeys"]:
            if k != k.strip() or not k:
                problems.append(f"{where}: bad key {k!r}")
            if e["useRegex"]:
                try:
                    re.compile(k)
                except re.error as err:
                    problems.append(f"{where}: invalid regex {k!r}: {err}")
    return problems


def main():
    out_dir = ROOT / "dist"
    out_dir.mkdir(exist_ok=True)
    for old in out_dir.glob("*.marinara.json"):  # lorebooks and the card
        old.unlink()
    all_problems = []
    total_entries = 0
    for mod_name in BOOK_MODULES:
        book = importlib.import_module(mod_name).book
        all_problems += validate(book)
        slug = re.sub(r"[^A-Za-z0-9]+", "-", book.name).strip("-")
        path = out_dir / f"{slug}.marinara.json"
        path.write_text(json.dumps(book.envelope(), indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        tokens = sum(approx_tokens(e["content"]) for e in book.entries)
        constant = sum(approx_tokens(e["content"]) for e in book.entries if e["constant"])
        biggest = max((approx_tokens(e["content"]) for e in book.entries), default=0)
        total_entries += len(book.entries)
        print(f"{path.name}: {len(book.entries)} entries, {len(book.folders)} folders, "
              f"~{tokens} tokens total, ~{constant} constant, largest entry ~{biggest}")
    print(f"TOTAL: {total_entries} entries")

    card = importlib.import_module("card_harley")
    env = card.envelope()
    data = env["data"]["data"]
    if len(data["summary"]) > 500:
        all_problems.append(f"card summary is {len(data['summary'])} chars (max 500)")
    for field in ("name", "description", "personality", "scenario", "first_mes", "mes_example"):
        if not data[field].strip():
            all_problems.append(f"card field {field} is empty")
    card_path = out_dir / "Harley-Quinn.character.marinara.json"
    card_path.write_text(json.dumps(env, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    prompt_fields = [data["description"], data["personality"], data["scenario"], data["mes_example"],
                     data["system_prompt"], data["post_history_instructions"],
                     data["extensions"]["backstory"], data["extensions"]["appearance"]]
    print(f"{card_path.name}: ~{sum(approx_tokens(f) for f in prompt_fields)} tokens always in context, "
          f"{1 + len(data['alternate_greetings'])} greetings")
    if all_problems:
        print("\nPROBLEMS:")
        for p in all_problems:
            print("  " + p)
        sys.exit(1)


if __name__ == "__main__":
    main()
