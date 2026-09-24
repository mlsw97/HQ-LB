# Harley Quinn Lorebooks for Marinara Engine

Five lorebooks covering Dr. Harleen Frances Quinzel, a.k.a. Harley Quinn, in
[Marinara Engine](https://github.com/Pasta-Devs/Marinara-Engine)'s native lorebook format.
Main-universe DC comics canon is the baseline, current through 2026. Details from
adaptations and fan interpretation are included only where they don't contradict that
canon, and are labelled.

**110 entries in 34 folders, about 39k tokens of lore.** Only two entries (~950 tokens)
are always on. Everything else triggers on names, places and topics.

## Download

Import the five files in [`dist/`](dist/):

| File | Contents | Entries |
|---|---|---|
| `Harley-Quinn-01-Core-Identity.marinara.json` | Always-on profile and voice guide; names and aliases; roots and Jewish heritage; education and every job; age; love life; appearance; every costume; disguises; personality; psychology; morality; fears; humor; powers; fighting; intellect; the mallet and other weapons; likes, food, dislikes, habits; catchphrases | 26 |
| `Harley-Quinn-02-Canon-History.marinara.json` | All four origin versions (Mad Love, No Man's Land, New 52 Ace Chemicals, the modern version), then every era: the Quinntets, Metropolis, Vengeance Unlimited, the Secret Six and Countdown, Gotham City Sirens, the New 52 Suicide Squad, Coney Island, the Gang of Harleys, Joker's Last Laugh, Rebirth (zombies, Vote Harley, Mason's death, Apokolips, her mom's death, Joker War), Heroes in Crisis, Infinite Frontier (Kevin, Keepsake, Verdict), Tini Howard's run, and Throatcutter Hill through the 2026 Ivy breakup; plus a present-day snapshot | 27 |
| `Harley-Quinn-03-Relationships-Cast.marinara.json` | The Joker (history, plus how she handles him now), Poison Ivy (history, plus dynamics), her mother, father, brothers and extended family, Batman, Catwoman, the Bat-Family, Kevin, Punchline, Gotham's rogues, her own villains, Big Tony, Sy Borgman, Mason, the Coney Island tenants, Red Tool, the Gang of Harleys, Tina and friends, Deadshot, Waller and the Squad, hero team-ups, Althea Klang, Chicken Fingers, Bud & Lou, Bernie the Beaver, her other animals | 29 |
| `Harley-Quinn-04-Places-Groups-Things.marinara.json` | Her homes over the years, the Coney Island building, Eden, Gotham, Arkham, Ace Chemicals, Throatcutter Hill, New York spots, her Coney Island jobs, Metropolis, the Suicide Squad, the Joker's gang, a team index, Joker Venom, the Scatapult, her possessions | 16 |
| `Harley-Quinn-05-Adaptations-Alternate-Versions.marinara.json` | Rules for mixing canon with adaptations; the animated universe, the 2019 animated series, other cartoons; the Margot Robbie films and other live action; the Arkham games, Injustice and other games; White Knight, Harleen, Breaking Glass, Criminal Sanity, Old Lady Harley, Absolute and more | 12 |

## Install

1. In Marinara Engine, open **Import Lorebook (JSON)**. Select or drag in all five
   `.marinara.json` files at once; the dialog accepts several files.
2. Make them active for your Harley chats. Imported lorebooks are deliberately **not
   global**, so they won't leak into your other characters' chats. Either:
   - link all five to your Harley Quinn character (the character's Lorebook tab), or
   - drag them into a chat's settings to activate them for that chat only.
3. Recommended: keep the chat's lorebook token budget at **6,000 or more** (the default
   is 8,192). Typical turns use 1–4k tokens. Each book also has its own cap, so no
   single book can crowd out the others.

Every entry arrives **locked**, so Marinara's Lorebook Keeper agent won't rewrite canon
facts. Unlock any entry you want the agent to be able to change.

## How the books behave

- **Always on:** `Core Profile` (who she is, and the default setting) and `Voice & Speech
  Guide` (accent, slang, pet names, rhythm, sample lines).
- **Default era:** present-day canon (2026). Harley is in Gotham's Throatcutter Hill,
  newly broken up with Mayor Poison Ivy, and flirting with Althea Klang. If your chat
  sets another era (Coney Island landlady, Suicide Squad, classic Joker days, or an
  adaptation such as "movie Harley"), the matching history and adaptation entries
  supply that era's facts. The Core Profile tells the model to follow the chat's era.
- **Keywords** are whole-word and case-insensitive, and chosen so ordinary words don't
  trigger anything. "red", "crazy", "date", "fight", "cake", "hiya" and "right now"
  fire nothing. "Ivy", "Mistah J", "mallet", "Arkham", "Bernie", "Big Tony" and
  "Throatcutter Hill" fire their entries.
- **Sticky:** entries stay active for 2–3 messages after their keyword, so a topic
  doesn't drop out mid-scene.
- **Descriptions:** every entry has a one-line summary, used by Marinara's
  knowledge-router agent and by vector search if you turn it on.
- **Canon labels:** alternate-continuity entries start with `[ALTERNATE CONTINUITY: …]`
  and say which details can be borrowed into main canon. Places where canon contradicts
  itself (her New 52 origin, her Canarsie vs. Bensonhurst childhood, psychologist vs.
  psychiatrist) are explained, with the reading that fits best today.

## Verification

- `python3 tools/build.py` regenerates `dist/` from `src/` and validates every entry
  (folders exist, nothing empty, keys clean).
- `tools/verify_in_marinara.regression.ts` runs inside a Marinara Engine checkout (copy
  it to `scripts/regressions/` and run it with `tsx`, setting `HQ_DIST` to this `dist/`
  folder). It imports all five files through Marinara's real `/api/import/marinara`
  route, checks that every entry, key, folder and piece of content round-trips, then
  runs Marinara's own lorebook scanner on sample messages to confirm the right entries
  fire and everyday chatter doesn't. It passes against Marinara Engine at commit
  `12a0acd` (v2.4.6, September 2026).

## Editing

The lore lives in `src/book_*.py`, one file per lorebook, with each entry written as
`book.entry(name, keys, content, description=…, …)`. `src/lb.py` fills in every
Marinara field with sensible defaults. Edit, then run `python3 tools/build.py`.

## Sources

Built from Marinara Engine's schema and importer source; the DC Database (issue
synopses and character pages); Wikipedia's articles on Harley Quinn, her comic series,
the animated series and the films; Goodreads and Comic Book Roundup solicitations; and
2025–2026 coverage from ComicBook.com, Screen Rant, Bleeding Cool and AIPT for the
current run. Issue numbers are cited inside entries where they matter.
