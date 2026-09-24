"""Tiny authoring layer for Marinara Engine lorebooks.

Each lorebook module in src/ builds a `Book`, adds folders and entries, and
tools/build.py serialises every Book into Marinara's native export envelope
({"type": "marinara_lorebook", "version": 1, "data": {lorebook, entries, folders}}).

Field names and defaults mirror packages/shared/src/schemas/lorebook.schema.ts
and packages/server/src/services/import/marinara.importer.ts in Marinara Engine.
"""

import textwrap
import uuid

NAMESPACE = uuid.UUID("6c1d7e0a-9f5b-4d0e-9a57-4a1f2b8c3e11")
TIMESTAMP = "2026-09-24T00:00:00.000Z"


def _id(*parts):
    return str(uuid.uuid5(NAMESPACE, "::".join(parts)))


def _text(s):
    return textwrap.dedent(s).strip()


class Book:
    def __init__(self, name, description, category="character", tags=(), *,
                 scan_depth=6, token_budget=4096, entry_limit=40,
                 recursive_scanning=False, enabled=True):
        self.id = _id("book", name)
        self.name = name
        self.lorebook = {
            "id": self.id,
            "name": name,
            "description": _text(description),
            "category": category,
            "imagePath": None,
            "scanDepth": scan_depth,
            "tokenBudget": token_budget,
            "entryLimit": entry_limit,
            "recursiveScanning": recursive_scanning,
            "maxRecursionDepth": 3,
            "excludeFromVectorization": False,
            "vectorQueryDepth": 10,
            "vectorScoreThreshold": 0.3,
            "vectorMaxResults": 10,
            "characterId": None,
            "characterIds": [],
            "personaId": None,
            "personaIds": [],
            "chatId": None,
            "isGlobal": False,
            "enabled": enabled,
            "hiddenFromLibrary": False,
            "scope": {"mode": "all", "chatIds": []},
            "tags": list(tags),
            "generatedBy": "user",
            "sourceAgentId": None,
            "createdAt": TIMESTAMP,
            "updatedAt": TIMESTAMP,
        }
        self.folders = []
        self.entries = []
        self._names = set()

    def folder(self, name, parent=None):
        fid = _id(self.name, "folder", name)
        self.folders.append({
            "id": fid,
            "lorebookId": self.id,
            "name": name,
            "enabled": True,
            "parentFolderId": parent,
            "order": len(self.folders),
            "createdAt": TIMESTAMP,
            "updatedAt": TIMESTAMP,
        })
        return fid

    def entry(self, name, keys, content, *, description, folder=None, tag="lore",
              secondary_keys=(), selective_logic="and", constant=False, order=100,
              position=0, depth=4, role="system", sticky=None, cooldown=None,
              probability=None, scan_depth=None, whole_words=True, use_regex=False,
              case_sensitive=False, group="", enabled=True):
        if name in self._names:
            raise ValueError(f"duplicate entry name in {self.name}: {name}")
        if not constant and not keys:
            raise ValueError(f"non-constant entry without keys: {name}")
        self._names.add(name)
        secondary_keys = list(secondary_keys)
        self.entries.append({
            "id": _id(self.name, "entry", name),
            "lorebookId": self.id,
            "name": name,
            "content": _text(content),
            "description": _text(description),
            "keys": list(keys),
            "secondaryKeys": secondary_keys,
            "enabled": enabled,
            "constant": constant,
            "selective": bool(secondary_keys),
            "selectiveLogic": selective_logic,
            "probability": probability,
            "scanDepth": scan_depth,
            "matchWholeWords": whole_words,
            "caseSensitive": case_sensitive,
            "useRegex": use_regex,
            "characterFilterMode": "any",
            "characterFilterIds": [],
            "characterTagFilterMode": "any",
            "characterTagFilters": [],
            "generationTriggerFilterMode": "any",
            "generationTriggerFilters": [],
            "additionalMatchingSources": [],
            "position": position,
            "outletName": "",
            "depth": depth,
            "order": order,
            "role": role,
            "sticky": sticky,
            "cooldown": cooldown,
            "delay": None,
            "ephemeral": None,
            "group": group,
            "groupWeight": None,
            "folderId": folder,
            "locked": True,
            "preventRecursion": True,
            "excludeRecursion": False,
            "delayUntilRecursion": False,
            "tag": tag,
            "relationships": {},
            "dynamicState": {},
            "activationConditions": [],
            "schedule": None,
            "excludeFromVectorization": False,
            "embedding": None,
            "createdAt": TIMESTAMP,
            "updatedAt": TIMESTAMP,
        })

    def envelope(self):
        return {
            "type": "marinara_lorebook",
            "version": 1,
            "exportedAt": TIMESTAMP,
            "data": {
                "lorebook": self.lorebook,
                "entries": self.entries,
                "folders": self.folders,
            },
        }
