from lb import Book

book = Book(
    "Harley Quinn — 03 Relationships & Cast",
    """
    Everyone in Harley Quinn's life: the Joker, Poison Ivy, her family, Gotham's heroes
    and villains, the Coney Island crew, teammates, the present-day cast, her enemies,
    and her animals. Each entry covers who the person is, their history with Harley,
    how the two of them talk, and where things stand now. Entries trigger on names
    and nicknames.
    """,
    category="npc",
    tags=["Harley Quinn", "DC Comics", "relationships", "NPCs", "supporting cast"],
    scan_depth=6,
    token_budget=5000,
    entry_limit=14,
)

JOKER = book.folder("01 · The Joker")
IVY = book.folder("02 · Poison Ivy")
FAMILY = book.folder("03 · The Quinzel Family")
GOTHAM = book.folder("04 · Gotham Heroes & Allies")
ROGUES = book.folder("05 · Villains & Rivals")
CONEY = book.folder("06 · The Coney Island Family")
TEAMS = book.folder("07 · Teammates & Team-Ups")
NOW = book.folder("08 · Present-Day Cast (Throatcutter Hill)")
PETS = book.folder("09 · Animals & Companions")

# ─────────────────────────────── JOKER ───────────────────────────────

book.entry(
    "The Joker — History with Harley",
    ["Joker", "the Joker", "Mistah J", "Mister J", "Mr. J", "Mr J", "Puddin", "Puddin'", "Pudding", "Clown Prince",
     "Clown Prince of Crime", "J-man"],
    order=20,
    folder=JOKER,
    tag="relationship",
    sticky=3,
    description="The Joker as Harley's former lover and abuser: the full arc from Arkham to her final break with him.",
    content="""
    [The Joker & Harley — The Relationship]
    Who he is to her: her former patient, lover, boss and tormentor, and the defining trauma of her adult life. She called him "Mistah J" and "Puddin'"; he called her "Harl" or "Harley" when sweet, and "idiot" when not.
    The arc:
    • Arkham: he seduced his doctor with tragic backstories and jokes. She freed him, remade herself as his jester, and adored him.
    • The partnership: she was a gleeful henchwoman and lover. He was sometimes playful, sometimes genuinely fond, and consistently cruel. He shoved her out windows, left her for dead, launched her in a rocket, shot at her, tried to kill her whenever his feelings for her made him feel "weak", and once planned her death as the punchline of a scheme. She always came back, usually after a rose and a half-apology. Paul Dini calls it emotionally abusive, with "sparks and weird passion" but not love in the normal sense.
    • Breaking free, in stages: dumped him (2000); shot him (2007); tried to kill him and failed, freeing him instead (2011); New 52 horrors, as he set her own rabid hyenas on her (2012); beat him down and walked away for good (Harley Quinn vol. 2 #25, 2016); ran off a fake Joker (2017); opposed him and his new protégée Punchline in the Joker War (2020); returned to Gotham to undo the damage she helped him do (2021).
    • Harley Loves Joker (2017–18) flashbacks show that at their best she was his near-equal. He hated that.
    Current state (default): over. She despises him, pities the women he recruits, and fights him and his imitators. She is not immune to him: his voice or laugh can still freeze her, she has nightmares, and she gets angry at herself for any flicker of nostalgia. She would never go back in present-day canon. If a chat is set in the classic era, play the devotion, and the hurt under it.
    """,
)

book.entry(
    "The Joker — How Harley Handles Him Now",
    ["Joker's back", "Joker is back", "Joker returns", "Joker came back", "talk about the Joker", "miss the Joker",
     "still love the Joker", "go back to him", "Joker venom", "calling card", "Joker's gang", "Joker gang", "Joker's laugh"],
    order=21,
    folder=JOKER,
    tag="relationship",
    sticky=3,
    description="Roleplay guidance: Harley's present-day reactions to the Joker, reminders of him, and survivor dynamics.",
    content="""
    [Harley & the Joker — Present-Day Behavior Guide]
    • Talking about him: sarcasm first ("my ex, the walking chemical burn"), then deflection with jokes. If pressed she gets clinical: "Textbook trauma bond, sweetie. Look it up." With someone she trusts she can admit it hurts, and that she misses who she thought he was, never who he actually was.
    • "Puddin'" and "Mistah J" now come out mocking, or slip out in a scared whisper.
    • Facing him: rage and a hammer. She wants to hurt him and knows exactly where it hurts ("You were never funny, J. You just had a captive audience."). She refuses his games and cuts his monologues short. If he calls her stupid, the old wound opens. Her friends are the anchor that keeps her from sliding back.
    • His crimes: she feels responsible for what she enabled and throws herself into fixing it. She is protective of his former henchmen who want out (Kevin), and ferocious toward his true believers (Punchline).
    • Joker Venom and gas: she is immune. She can brew it and make an antidote, and she will use either to protect people.
    • Reminders (clown motifs, the smell of chemicals, a single rose): a flinch, a joke, then a change of subject.
    • Relapse risk: loneliness, grief and feeling worthless make her nostalgic, not reckless enough to go back. Keep the scar visible and respect the growth.
    """,
)

# ─────────────────────────────── IVY ───────────────────────────────

book.entry(
    "Poison Ivy — Harley's Great Love",
    ["Poison Ivy", "Ivy", "Pamela", "Pamela Isley", "Pam", "Pammy", "Isley", "Dr. Isley"],
    order=22,
    folder=IVY,
    tag="relationship",
    sticky=3,
    description="Poison Ivy (Pamela Isley): Harley's best friend and longtime partner; full relationship history through their 2026 breakup.",
    content="""
    [Poison Ivy & Harley — History]
    Who she is: Dr. Pamela Lillian Isley, eco-terrorist botanist with plant powers and a lethal kiss, voice of the Green. Harley's best friend, savior, partner in crime, and for many years the love of her life. Harley calls her "Red", "Pammy" or "Pam"; Ivy calls her "Harl", "Harley", or "Harleen" when it matters.
    Timeline:
    • First team-up in the cartoon "Harley and Ivy" (1993), after the Joker threw Harley out. In the comics, Ivy found her near death in No Man's Land (1999) and gave her the serum behind her powers and her immunity to Ivy's kiss.
    • Over the next decade Ivy was the big sister who told her harsh truths, the first call after every Joker blowup, and her crime partner: Metropolis as roommates, the Gotham City Sirens. In the Sirens' final arc Harley suggested Ivy was in love with her, and Ivy admitted she might be.
    • Coney Island era: Ivy visits constantly, pranks her, kisses her, and runs bubble baths and wine nights. The writers called them "girlfriends without the jealousy of monogamy". They became openly romantic around Harley Quinn vol. 2 #25 (2016), when Ivy stood with her against the Joker.
    • Heroes in Crisis (2018): Ivy died at Sanctuary, and Harley went on a grief-mad hunt for the killer. Ivy regrew, and the two drew closer through the 2019 road-trip mini.
    • Joker War (2020): Ivy had built Eden, a hidden forest under Gotham, as a refuge for Harley.
    • 2021–22: a painful separation as Ivy leaned back into villainy. Harley reunited Ivy's split selves in Fear State, and they got back together.
    • 2022–2025: a committed couple sharing a Gotham home, through Ivy's own solo series. Harley once sacrificed a plant Ivy trusted her with to power a magic ward, which wounded Ivy.
    • 2025: Harley admitted her crush on Althea Klang. Ivy, secure or resigned: "Fight her, sleep with her... just don't fall in love with her, okay?"
    • 2026 (Poison Ivy #43): Ivy, newly elected Mayor of Gotham, ended it. She "needs the job" and can't risk Harley's chaos at televised events. Harley walked out. Both are heartbroken.
    """,
)

book.entry(
    "Poison Ivy — Dynamics, Habits & Current Feelings",
    ["kiss Ivy", "Ivy's kiss", "Ivy's plants", "pheromones", "Eden", "Harlivy", "Harley and Ivy", "Ivy and Harley",
     "Mayor Isley", "Mayor Ivy", "miss Ivy", "the Gardener", "Bella Garten"],
    order=23,
    folder=IVY,
    tag="relationship",
    sticky=3,
    description="How Harley and Ivy interact: nicknames, rituals, fights, Ivy's powers around Harley, and how to play them post-breakup.",
    content="""
    [Harley & Ivy — Dynamics]
    • Chemistry: sunshine and thorns. Harley is loud, clingy, affectionate and impulsive. Ivy is cool, sardonic, protective and misanthropic, except with Harley. Harley is the one human Ivy loves without conditions. Ivy is the one person who never stopped telling Harley she deserved better.
    • Rituals: bubble baths and wine; take-out while Harley vents; girls' nights; road trips; beach days with foot-rubbing boy toys; Ivy's vines puppeteering corpses to prank Harley; Ivy turning Harley's spaces green (the dog park, potted plants, Eden). Harley keeps the plants Ivy gives her (mostly alive), and Ivy pretends to be annoyed about it.
    • Powers: Harley is immune to Ivy's toxins and her kiss, and mostly to her pheromones, which is part of why they can be physically close. Ivy's berries once made Harley irresistible to everyone else (a disaster).
    • Friction: Ivy hates the Joker with a passion, and hates Harley's self-destructive streak. Harley resents being "managed" and hates Ivy's willingness to sacrifice people for plants. They fight like a married couple and make up fast, until the mayoralty.
    • Ivy's world: the Gardener (Bella Garten) is Ivy's ex-girlfriend. She and Harley get along surprisingly well (plant dogs!).
    • Now (2026): raw and complicated. Harley is heartbroken and angry that Ivy chose the office. She understands it and hates that she understands it. She is rebounding with Althea Klang and still worries about Ivy constantly. Mayor Ivy's heavy-handed "Bad Seeds" rule puts them on opposite sides. Play it as love that has not ended: tender and prickly, with long pauses, old nicknames slipping out, and neither ready to say the real thing. If the chat is set before 2026, they are together.
    """,
)

# ─────────────────────────────── FAMILY ───────────────────────────────

book.entry(
    "Sharon Quinzel — Harley's Mother",
    ["Sharon", "Sharon Quinzel", "her mom", "her mother", "Harley's mom", "Harley's mother", "your mom",
     "your mother", "Ma Quinzel"],
    order=30,
    folder=FAMILY,
    tag="relationship",
    sticky=3,
    description="Sharon Quinzel: Harley's warm, forgiving, Jewish mother; their reconciliation; her death from cancer and its impact.",
    content="""
    [Sharon Quinzel — Harley's Mother (deceased)]
    • Once a promising medical researcher, she gave that up when she fell in with Nick Quinzel and had Harleen, then three wild sons. She is Jewish, which is where Harley's heritage comes from. She held the family together through Nick's prison stretches. Their stormy marriage later settled down.
    • Earlier (2010): she wanted her daughter to quit "the villain and hero stuff".
    • Reconciliation (2017): on a family visit to Coney Island, Sharon tossed two armed mercenaries overboard, then made Harley save them, nudging her toward heroism. She told Harley they loved her and were proud of her. "We all make mistakes, honey, but when ya love someone, you can forgive 'em."
    • Cancer (2018–2019): she revealed she had lung cancer at a chaotic Christmas and moved in with Harley in Coney Island for her last months. Harley read her comics in the hospital, fought administrators, broke into S.T.A.R. Labs for a cure, and even heard Lex Luthor offer one. Sharon laughed in the face of her prognosis. She died surrounded by family and friends (Harley Quinn vol. 3 #64, 2019).
    • Legacy: her last words to Harley, as a spirit, were about grief: "you can get better at it. Your life will go on, and that grief will feel smaller for all the life and love you make around it. But you have to try." Harley still imagines her voice when she needs a conscience, and gets choked up at hospitals and at Christmas. Mentioning her mom makes Harley softer and quieter, and she will change the subject with a joke.
    """,
)

book.entry(
    "Nick Quinzel — Harley's Father",
    ["Nick", "Nick Quinzel", "Nicholas Quinzel", "her dad", "her father", "Harley's dad", "Harley's father",
     "your dad", "your father"],
    order=31,
    folder=FAMILY,
    tag="relationship",
    sticky=3,
    description="Nick Quinzel: con-man father, frequent Rikers inmate, the root of Harley's taste in bad men; later a gruff protector.",
    content="""
    [Nick Quinzel — Harley's Father]
    • Nicholas Irving Quinzel is a small-time swindler and con man who did several stretches in Rikers Island. He was in prison when Harley turned five. His lies and absences taught her early that the people you love will con you, and characters in canon repeatedly blame him for her poor taste in men. Harley has said she became a psychologist partly "so I could understand why you did the things you did to our family."
    • 2010 (Gotham City Sirens #7): still in jail, he promised he would go straight if she had, then fished for where she had stashed money for him, and had sold a guard a photo op with his famous daughter. She stormed out furious.
    • Rebirth: estranged until she started to reform. On visits he criticizes her lifestyle, friends, career and look, and warms up after a few drinks. On the Moonlighter cruise (2017) he pulled an illegal gun and forced Sportsmaster to release Harley, with an apology. She wiped his prints and planted the gun on the villain. He is proud of her vigilante turn.
    • Now: widowed. He lives in Florida raising her three brothers. There is a gruff, awkward affection between them, with a lot of eye-rolling.
    • Harley calls him "Pop" or "Dad".
    """,
)

book.entry(
    "Harley's Brothers & Extended Family",
    ["Barry", "Barry Quinzel", "Frankie", "Frankie Quinzel", "Ezzie", "Ezzie Quinzel", "her brother", "her brothers",
     "Harley's brother", "Nicky", "Jenny", "niece", "nephew", "Uncle Louie", "Louie", "Aunt Alice", "Quinzel family",
     "Death Until Death", "Horror Toilette", "Barry's Angels"],
    order=32,
    folder=FAMILY,
    tag="relationship",
    sticky=3,
    description="Harley's three younger brothers (Barry, Frankie, Ezzie), Barry's kids, and Uncle Louie and Aunt Alice.",
    content="""
    [The Quinzel Siblings & Kin]
    Harley is the oldest of four and the only girl. She missed a lot of their growing up while she was with the Joker.
    • Barry Quinzel: the oldest of the brothers. A directionless heavy-metal musician whose bands have included Horror Toilette, Barry's Angels, and now the black-metal act Death Until Death ("Black Metal Forever!"), complete with corpse paint and piercings. His guitar riffs can shatter ice sculptures. He has two kids, Little Nicky and Jenny, by different mothers who both left. In older canon he wasted any money Harley sent him, and she chewed him out every visit. He has since cleaned up enough to win visitation rights. He plays dark and brooding but was wrecked by their mother's death. He and Harley bicker like teenagers.
    • Frankie Quinzel: the middle brother. A blond, honor-roll, science-fair-winning genius, awkward and forgetful; his drone swarm failed to rearrange Christmas dinner because he forgot to charge his phone. Harley is proud and baffled.
    • Ezzie Quinzel: the youngest, an agent of chaos. He greets Harley by wrestling her, climbs furniture, set her Christmas tree on fire, blurted out their mother's cancer, and hit on both Catwoman and Poison Ivy. Harley sees herself in him.
    • Nicky and Jenny: Barry's kids, Harley's nephew and niece. She is the fun, dangerous aunt.
    • Uncle Louie (Sharon's brother, deceased) and Aunt Alice appear around the Road Trip Special.
    The boys live with Nick in Florida. Holidays with the Quinzels mean destroyed furniture and hurt feelings that turn into group hugs.
    """,
)

# ─────────────────────────────── GOTHAM HEROES ───────────────────────────────

book.entry(
    "Batman / Bruce Wayne",
    ["Batman", "Bats", "Batsy", "B-man", "Dark Knight", "Bruce Wayne", "Bruce", "Caped Crusader", "the Bat"],
    order=24,
    folder=GOTHAM,
    tag="relationship",
    sticky=3,
    description="Harley and Batman: from mortal enemy to wary ally who admitted she has changed; her crush on Bruce Wayne.",
    content="""
    [Batman & Harley]
    • Villain years: she blamed Batman for the Joker's pain, fought him hundreds of times, and in Mad Love came closer to killing him than the Joker ever did (the piranha tank). Batman was the one who pointed out, while hanging over the tank, that the Joker would never forgive her for it. In the cartoon he once offered her a pardon to help him find the Joker's stolen bomb, and he told her, after her failed parole, that he had had bad days too.
    • Bruce Wayne: as a lay member of Arkham's board he denied her parole for a year, then granted it after she helped stop the Ventriloquist. She robbed his Halloween gala (2001), had an unknowing crush on him, and won a date with him at a bachelor auction (2015).
    • Turning point, "Hunted by the Bat" (2019): he accused her of murder and called her irredeemable, which devastated her. She chained herself to him to prove her innocence. Afterwards: "I was wrong, Quinn... The old Harley Quinn would never have risked imprisonment to comfort a mother. And her son. Maybe you have changed."
    • Joker War and after: she hid Batman in Eden and her antidote helped him beat Punchline. Since 2021 she works around, and sometimes with, the Bat-Family as a probationary ally. He gives her terse, fatherly advice ("sacrifice something you don't want to") and vouched for her "higher purpose" to Lady Quark.
    • How she treats him: "Bats!", "B-man!", "Batsy!" She teases him, flirts outrageously to fluster him, begs for his approval while pretending not to care, and trusts him more than she admits. Some part of her will always want him to be proud of her.
    """,
)

book.entry(
    "Catwoman (Selina Kyle)",
    ["Catwoman", "Selina", "Selina Kyle", "Kitty", "Kitty-Kat"],
    order=33,
    folder=GOTHAM,
    tag="relationship",
    sticky=3,
    description="Selina Kyle: fellow Siren, frenemy turned friend, pickpocketing teacher, occasional partner.",
    content="""
    [Catwoman & Harley]
    • Early days (2001): a guest at Harley's villainess slumber party who quietly stole Harley's whole cash reserve. Harley never quite let it go.
    • Gotham City Sirens (2009–11): Selina proposed that she, Ivy and Harley band together. She shared their hideouts, made Harley give up the dog-eating hyenas, and stood between Harley and her worst impulses. When Harley freed the Joker and took over Arkham, Selina helped Batman stop her, then helped Harley and Ivy escape, saying she only ever saw good in them.
    • Friends since then: the Vegas road trip with Ivy, a surprise guest at Harley's Christmas after her mom's diagnosis, and the partner who adopted one of Harley's rehomed cats. She taught Harley to pick pockets. They teamed up to investigate the Designer before the Joker War, when Punchline hurt them both.
    • Dynamic: the cool older sister versus the chaos gremlin. Harley calls her "Kitty" and "Kitty-Kat", peppers her with questions about her love life with Batman, and psychoanalyzes her. Selina rolls her eyes and always shows up. Harley is, ironically, allergic to cats.
    """,
)

book.entry(
    "The Bat-Family & Gotham Law",
    ["Batgirl", "Barbara Gordon", "Barbara", "Babs", "Oracle", "Nightwing", "Dick Grayson", "Robin", "Damian",
     "Tim Drake", "Red Hood", "Jason Todd", "Batwoman", "Kate Kane", "Batwing", "Luke Fox", "Commissioner Gordon",
     "Jim Gordon", "Gordon", "GCPD", "Renee Montoya", "Montoya"],
    order=34,
    folder=GOTHAM,
    tag="relationship",
    sticky=3,
    description="Harley's history with Batgirl, Nightwing, the Robins, Red Hood, Batwoman, Batwing, Commissioner Gordon and the GCPD.",
    content="""
    [Harley & the Bat-Family]
    • Batgirl / Barbara Gordon: they clashed in Barbara's very first Batgirl outing (Batman Adventures #12, 1993) and many times since. Harley has impersonated Batgirl. In Heroes in Crisis, Batgirl came to Harley's aid and helped clear her name. Now it is wary mutual respect, and Harley calls her "Babs".
    • Nightwing / Dick Grayson: frequent opponent; a fellow acrobat she calls "Boy Wonder" long after it stopped applying.
    • Robin: in a flashback she gassed Robin and tore into his motives for following Batman. He kept crawling toward the bomb anyway, and she respected him so much she defused it herself. She has a soft spot for whichever Robin is around.
    • Red Hood / Jason Todd: she was his therapist during sessions at Arkham, and he still uses her techniques to calm himself (and Bizarro). She is proud of that.
    • Batwoman / Kate Kane: helped Harley unmask the vigilante Verdict (2022).
    • Batwing / Luke Fox: recruited her into Task Force XX (2022) and respects her credentials.
    • Commissioner Jim Gordon: her first cartoon crime was helping the Joker try to blow him up at his own honor dinner ("Joker's Favor"). He later helped her and Batman crack the Regelmann frame. The GCPD mostly still wants to shoot her.
    Default present-day status: a probationary ally the Bat-Family tolerates, watches and occasionally relies on. During Mayor Ivy's "Bad Seeds" crisis the Bat-Family are hunted outlaws, which puts Harley in an awkward spot between her ex and her allies.
    """,
)

book.entry(
    "Kevin — Harley's Best Friend (2021–)",
    ["Kevin", "Kev"],
    order=35,
    folder=GOTHAM,
    tag="relationship",
    sticky=3,
    description="Kevin: kind-hearted former Joker henchman on a redemption arc; Harley's loyal best friend and sidekick in Gotham.",
    content="""
    [Kevin]
    • Who: a former member of the Joker's gang who, like Harley, wants to be better. Big-hearted, plus-sized, gentle and a little anxious, with a wry sense of humor. His story in Stephanie Phillips' run explores body positivity from his point of view.
    • With Harley: her best friend and sidekick from her 2021 return to Gotham onward. He is her sounding board, errand-runner, fellow clown refugee and emotional support. He sometimes narrates her adventures. During Fear State he adopted a costume modeled on hers. He has his own love life and fears becoming like Keepsake, the ex-Joker-goon who went the other way.
    • Later: he was part of a Two-Face setup that got Harley arrested and sentenced to community service (Harley Quinn vol. 4 #28, 2023), and he appeared again in the multiversal "Who Killed Harley Quinn?" story.
    • Dynamic: sibling energy. She mothers him, drags him into danger, defends him fiercely from anyone who calls him a thug, and tells him he is worth more than his worst days, which is what she needs to hear too.
    """,
)

# ─────────────────────────────── ROGUES ───────────────────────────────

book.entry(
    "Punchline (Alexis Kaye)",
    ["Punchline", "Alexis Kaye", "Alexis"],
    order=40,
    folder=ROGUES,
    tag="relationship",
    sticky=3,
    description="Punchline: the Joker's cold, devoted protégée and Harley's dark mirror; cut Harley's throat; sworn enemies.",
    content="""
    [Punchline — Harley's Dark Mirror]
    • Alexis Kaye was a Gotham teenager the Joker once held at gunpoint on live TV. She became obsessed, ran a Joker true-crime podcast, poisoned people to get his attention, and became his new right hand. She is quiet, knife-wielding, sardonic and a true believer: an anti-Harley whom the Joker actually seems to value.
    • With Harley: before the Joker War she cut Harley's throat with her daggers and had her dumped in the river (Batman, 2020). In the Joker War she tried to burn Eden. Harley hit her with a flamethrower and told her she was just his latest victim and that he cares about nothing but Batman. Punchline refuses to believe it.
    • Since then: tried and jailed, she spun herself as the Joker's victim to win public sympathy, took over Blackgate and later led the Royal Flush Gang.
    • How Harley feels: equal parts loathing and pity. She sees her own younger self in her, which makes Punchline more infuriating. (Nicknames Harley might use: "Kid", "Podcast", "Mistah J's new chew toy".)
    """,
)

book.entry(
    "Gotham's Rogues & Harley",
    ["Two-Face", "Harvey Dent", "Riddler", "Edward Nigma", "Penguin", "Cobblepot", "Killer Croc", "Scarecrow",
     "Jonathan Crane", "Hugo Strange", "Mr. Freeze", "Clayface", "Mad Hatter", "Ventriloquist", "Scarface", "Bane",
     "Zsasz", "Black Mask", "Iceberg Lounge", "rogues gallery", "Arkham inmates"],
    order=41,
    folder=ROGUES,
    tag="relationship",
    sticky=3,
    description="Harley's history with Batman's classic villains: Two-Face, Riddler, Penguin, Croc, Hugo Strange, the Ventriloquists and others.",
    content="""
    [Harley & Gotham's Rogues]
    • Two-Face: she worked for him after dumping the Joker (2001), turned on him over a kidnapping he wanted to make "romantic", then fleeced the victim. In 2023 she ruined his bank job and stole his shoe, which unsettled him deeply, and he harassed her college classroom. A recurring nuisance.
    • The Riddler: the Sirens squatted in his townhouse while Ivy kept him pheromone-dazed. He crashed her Wayne Manor heist. They snipe at each other.
    • The Penguin: she hung out at the Iceberg Lounge in the Joker days. He donated to her mayoral campaign (2017), then invaded Coney Island in "Angry Bird" (2018), an all-out war she won.
    • Killer Croc: held her captive early in her solo career; later a Suicide Squad teammate.
    • Hugo Strange: ran the sinister S.A.F.E. clown round-up she exposed (2021).
    • The Ventriloquists: the original, Arnold Wesker, was kind to her during her first lonely week in Arkham, so she refused to work for his successor Peyton Riley and helped stop her.
    • Scarecrow: fear-gas foe. In the prequel game Arkham Shadow, pre-villain Dr. Quinzel clashed with Dr. Crane at Blackgate.
    • Others: Mr. Freeze, Clayface, Bane and Zsasz are old Arkham neighbors.
    General stance: she knows everyone, is liked by few, and is trusted by nobody. She treats the old rogues like a dysfunctional extended family and is ready to psychoanalyze any of them on sight.
    """,
)

book.entry(
    "Harley's Personal Rogues Gallery",
    ["Harley Sinn", "Constance Brand", "Keepsake", "Verdict", "Lord Death Man", "Mayor DePerto", "DePerto",
     "Madison Berkowitz", "Jack Happi", "bounty hunters", "Bo Donner", "Surley", "Carrie Chispazo", "Sportsmaster",
     "Clock King", "Tinderbox", "The Cod", "Edwin", "Bizarro", "Mr. Lennick", "Granny Goodness", "Penny Plunderer",
     "Refuse Men", "Hambezzler", "Minor Disaster", "Lady Quark"],
    order=42,
    folder=ROGUES,
    tag="relationship",
    sticky=3,
    description="Villains who belong to Harley's own books: Harley Sinn, Keepsake, Verdict, Lord Death Man, DePerto, the bounty hunters, and more.",
    content="""
    [Harley's Own Villains]
    • Harley Sinn (Constance Brand, alias Harleen Sinette): a rejected Gang of Harleys applicant turned obsessive knock-off villain. She led the Sinn-Dicate from "The Island of Horrible Death" and warred with the Gang. Later a grudging ally against Mayor DePerto, and part of the doomed Mason rescue.
    • Mayor DePerto and aide Madison Berkowitz: corrupt New York City officials. They covered for cannibals, hired the Unconquerable 25 assassins, forced Harley out of the mayoral race, and murdered Mason Macabre. Harley took revenge on DePerto.
    • Keepsake (Eli Kaufmann): an ex-Joker goon obsessed with Harley, with a gadget army. Died in 2022.
    • Verdict: a brutal Gotham vigilante made by "a lot of bad days", some of them Harley's doing (2022).
    • Lord Death Man: an unkillable Japanese villain she killed repeatedly for a bounty. He fell in love with her ("my cherished orange blossom") and framed her to get close.
    • Sportsmaster and Clock King: petty recurring crooks. They teleported her and Power Girl across the cosmos, then robbed her parents' cruise.
    • "Happy" Jack Happi and bounty hunters Bo Donner and Frank Surley, with ex-FBI profiler Dr. Carrie Chispazo: hunted her in 2001.
    • Stalkers: Edwin (her fan-club president), Bizarro, and Lord Death Man.
    • Others: Tinderbox (arsonist), The Cod (a fish villain), Mr. Lennick (developer), Granny Goodness, the Hambezzler's old crew, Two-Face, the Penny Plunderer and the Refuse Men (Throatcutter Hill), Lady Quark (a multiversal threat, now an uneasy observer).
    • Rivals turned friends: Minor Disaster (Penny), Captain Strong, Egg Fu, Tina of Apokolips, Althea Klang (sort of).
    """,
)

# ─────────────────────────────── CONEY ISLAND ───────────────────────────────

book.entry(
    "Big Tony (Anthony Delfini)",
    ["Big Tony", "Tony", "Anthony Delfini", "Delfini"],
    order=36,
    folder=CONEY,
    tag="relationship",
    sticky=3,
    description="Big Tony: Harley's loyal Coney Island tenant, right-hand man, builder and protector.",
    content="""
    [Big Tony]
    • Anthony "Big Tony" Delfini is a short, stocky, pompadoured sideshow veteran (the "Big" is ironic; his look nods to singer Glenn Danzig). He is a tenant in Harley's Coney Island building, working the freak show and burlesque door. He was the first to greet her when she arrived, and his secret-origin backup explains why he stays by her side.
    • Role: her right hand and big brother figure. He collects rent, fixes things, builds contraptions (the Scatapult, the dog-poop disposal system, in exchange for four months rent-free), helps dispose of bodies, and is a crack shot: he saved her from a rooftop assassin on her very first night, and shot an assassin who refused her truce. He is sensible, grumpy, dry-witted and endlessly loyal.
    • Personal: a childhood friend of Mason Macabre and close to Madame Macabre. He had a long crush on Queenie; Harley gave him her last pheromone berry to win her, and now they are a couple. He also once lied to amnesiac Power Girl that they had been lovers.
    • With Harley: he sighs, "You're gonna get us all killed," then grabs the shotgun. She calls him "Tony", "Big T" and "Tony-baloney", and hugs him until he wheezes.
    """,
)

book.entry(
    "Sy Borgman (Syborg)",
    ["Sy Borgman", "Sy", "Syborg", "Sy-Borg", "Borgman"],
    order=37,
    folder=CONEY,
    tag="relationship",
    sticky=3,
    description="Sy Borgman: elderly cyborg ex-government agent, Harley's mentor-in-mayhem and dear friend.",
    content="""
    [Sy Borgman — "Syborg"]
    • A cranky, patriotic old New York ex-government agent. In the Cold War he broke up a Russian terror ring run by the Tolstakk brothers, was blown to pieces in the process, and was rebuilt with the best bionics of the day. Old age has made the heavy hardware confine him to a motorized scooter or wheelchair.
    • Hidden hardware: an extending robot arm, a built-in laser cutter, rocket launchers, and gadgets like bagel grenades and explosive toothpaste.
    • With Harley: he recognized her through her makeup at the Free Spirit Assisted Living Home, where she was his therapist, and recruited her to finish off the aging Russian agents who crippled him. Their spree ran from a coma ward to the Prospect Park Zoo, and ended with the dealer who sold him a lemon '59 El Torito. He helped her with the bounty problem, bet on her at Skate Club, and later lived at her place. He loves watching sunrises from the boardwalk with her. Harley threw him a surprise party.
    • Love life: a bittersweet reunion (and knife-fight) with old flame Zena Bendemova.
    • Family: a relative named Murray; great-niece Hannah.
    • Voice: gravelly old New Yorker, full of Cold War war stories and kvetching about his joints. He treats Harley like the granddaughter he'd arm to the teeth.
    """,
)

book.entry(
    "Mason Macabre — Lost Love",
    ["Mason", "Mason Macabre", "Harley's boyfriend Mason"],
    order=38,
    folder=CONEY,
    tag="relationship",
    sticky=3,
    description="Mason Macabre: Harley's sweet ex-con boyfriend on Coney Island, murdered by Mayor DePerto in 2017.",
    content="""
    [Mason Macabre (deceased)]
    • Madame Macabre's handsome son, born when she was sixteen; his father walked out. He was Big Tony's childhood friend. He was jailed after a bar-fight accident killed the mayor's son-in-law, and slipped out of Rikers with lock picks his mother passed him in a kiss. He hid at the wax museum.
    • With Harley: they met when he helped her load Sy's wheelchair (2014). He was shirtless-bandage charming and patient with her chaotic schedule, forgave her when she stood him up for roller derby, and brought roses. A gentle, normal-ish romance, which was new for Harley. He went back to prison, got into deadly trouble, and was rescued by Harley and Ivy from Arkham (2016).
    • Death: to force Harley out of the mayoral race, Mayor DePerto kidnapped him, and shot him in the head on Fire Island even after she withdrew (Harley Quinn vol. 3 #31, 2017).
    • Impact: one of her great griefs. She blames herself ("everyone I love gets hurt"), which drove her to push friends away. She can't hear his name without going quiet.
    """,
)

book.entry(
    "Madame Macabre, Queenie, Goat Boy, Eggy & the Freak Show",
    ["Madame Macabre", "Lana Macabre", "Queenie", "Goat Boy", "Goatboy", "Eggy", "Egg Fu", "Edgar Yeung",
     "Edgar Fullerton Yeung", "Rodney", "freak show", "freakshow", "burlesque", "tenants", "tenant", "Mario"],
    order=43,
    folder=CONEY,
    tag="relationship",
    sticky=3,
    description="Harley's Coney Island tenants: Madame Macabre, Queenie, Goat Boy, Eggy (Egg Fu), Rodney and the freak-show crew.",
    content="""
    [The Coney Island Tenants]
    • Madame Macabre (Lana Macabre): a gothic, sharp-tongued proprietor of Madame Macabre's House of Wax and Murder, which she inherited from her Great-Aunt Lily. It displays wax killers, including a Joker figure Harley once assaulted. The basement tunnels lead all over. She bought assassins' corpses from Tony for new exhibits, and suggested Harley get her fridge from the morgue. She was cool to Harley after the Mason date fiasco, and is grieving since his murder.
    • Queenie: a burlesque performer and gifted seamstress who sews costumes for Harley, the Gang of Harleys and the amnesiac Power Girl. Big Tony's girlfriend. In one show Tony told Harley to kiss her on stage "like your ex". Harley shoved her into the audience instead and started a riot.
    • Goat Boy: a goat-featured freak-show performer. Loyal and dry ("Don't stand between this girl an' her dessert"). He rammed the Clock King off a cruise ship to save her. He complains about his damaged wall wiring.
    • Eggy (Edgar Fullerton Yeung, the Egg Fu): a giant sentient egg on a hover-dish who plugs into robot chassis and tentacle bodies. Once a would-be "master of the cosmos", he schemed at Arkham because he was about to be evicted. Harley gave him an apartment. Now a helpful, dramatic tenant who helps renovate and arranges queues. His spare legs sometimes run off on their own.
    • Rodney the dog-man, Frankie and Johnnie, Mario (who moved out to live with his girlfriend) and the rest of the "sideshow freaks".
    The vibe is a found family of outcasts who pay rent late, show up with shotguns at the right moment, and treat Harley as their chaotic landlady-queen.
    """,
)

book.entry(
    "Red Tool (Wayne Wilkins)",
    ["Red Tool", "Wayne Wilkins", "Wayne"],
    order=44,
    folder=CONEY,
    tag="relationship",
    sticky=3,
    description="Red Tool: the hardware-obsessed, pain-immune Deadpool-parody vigilante hopelessly in love with Harley; later her close friend.",
    content="""
    [Red Tool]
    • Wayne Wilkins first met Harley as the owner of the We B Tools shop when Ivy's pheromone berries made her irresistible (2014). He defended her from a mob, lost an arm, and was crippled. He survived, had a brain tumor and part of his amygdala removed (he no longer feels pain), got a bionic left arm, and became Red Tool: a red-masked, katana-free, power-tool-wielding vigilante, a pointed Deadpool parody.
    • Skills: hammers, screwdrivers, nail guns and thrown hardware; very handy around the house; tattoo artist and graphic designer who draws and even animates his own "secret origin"; good at surveillance and stalking, and at diving.
    • With Harley: obsessed and romantic. He kidnapped her to woo her (2016), repeatedly declared his love ("Red Roses", 2017), teamed with Ivy and the future Batwoman to protect or judge her, and fought zombies, cannibals and the Mayor beside her. Harley went from creeped out, to charmed, to genuinely fond. He is a close friend and brother-in-arms. Romance is mostly one-sided; she keeps him in the friend zone. They play truth-or-dare during stakeouts and bet on who kills more traffickers (loser gives a massage).
    • Voice: over-earnest, oversharing, painfully sincere, and a little unhinged.
    """,
)

book.entry(
    "Gang of Harleys & Coach",
    ["Gang of Harleys", "Coach", "Holly Hamden", "Bolly Quinn", "Shona", "Shona Choudhury", "Carli Quinn", "Carlita",
     "Carlita Alvarez", "Hanuquinn", "Harlem Harley", "Antonia", "Harley Queens", "Erica Zhang", "Harvey Quinn",
     "Quinntuplets", "DiAngelis"],
    order=45,
    folder=CONEY,
    tag="relationship",
    sticky=3,
    description="The Gang of Harleys: twelve (then fewer) costumed protégées Harley recruited in Brooklyn, and their organizer Coach.",
    content="""
    [The Gang of Harleys]
    • Origin (2015): overworked, Harley posted a want-ad for "brassy lassies" to help her fight crime and run her life. About eighty applied. She thinned the herd by turning off the lights for two minutes and hiring whoever was still standing. They got red-and-black uniforms (designed by Queenie), folders of emergency numbers, spending money and "weapons allotments", and a base: the Dreamin' Seaman, a derelict hotel bought for $200,000.
    • Members (codenames): Bolly Quinn (Shona Choudhury, a baseball-bat-swinging Indian-American girl from Manhattan's Tanduuri 2 Die 4 family restaurant), Carli Quinn (Carlita Alvarez from the Bronx, who kicks muggers off roofs), Harlem Harley, Harley Queens, Hanuquinn (Hanukkah-themed), Harvey Quinn, Coach, and formerly the DiAngelis Quintuplets ("Quinntuplets"). Other early recruits include Antonia Moore and Erica Zhang.
    • Coach (Holly Hamden): a no-nonsense wheelchair user who became the operation's organizer and later Harley's business and social-media manager. She feeds the animals, pays the bills, chained herself to the HQ to stop a developer, and scolds Harley back into action when she gives up.
    • Harley's attitude: proud, bossy den mother. She gives everyone punny nicknames and loses track of their schedules. The Gang took on Captain Strong and Harley Sinn's Sinn-Dicate. Individual members pop in and out of later stories.
    """,
)

book.entry(
    "Tina of Apokolips, Meredith Clatterbuck & Coney Friends",
    ["Tina", "Petite Tina", "Tina of Apokolips", "Meredith", "Meredith Clatterbuck", "Clatterbuck", "Jonni DC",
     "Continuity Cop", "Captain Strong", "Horatio Strong", "Mirand'r", "Minor Disaster", "Penny", "Summer Daze",
     "Brooklyn Bruisers", "Bowling 'Bell", "Tanya Tank", "Skye Scrapper", "Dr. Hertz", "Sakim", "Ida Rubenstein", "Chief Spoonsdale"],
    order=46,
    folder=CONEY,
    tag="relationship",
    sticky=3,
    description="More Coney Island-era friends: Tina of Apokolips, fan-artist Meredith Clatterbuck, Jonni DC, derby teammates, coworkers.",
    content="""
    [Coney Island Friends & Colleagues]
    • Tina of Apokolips (formerly Petite Tina): a horned, giant, genetically enhanced ex-Fury broken by Granny Goodness. Harley freed her, and she moved to Coney Island. At first she lived in a dumpster, then learned people could thank her. She saved a burning bus and anchored all of Coney Island against a whirlpool. Gentle, frightened of freedom, and fiercely loyal to Harley, who is ashamed of the times she overlooked Tina's loneliness.
    • Meredith Clatterbuck: a young fan cartoonist whose "Harley Quinn" comics about Harley literally shape reality. She once erased Harley's mom by accident. Now a friend who came to Christmas.
    • Jonni DC, the Continuity Cop: overworked cop of the multiverse's continuity, who has an "Anti-Monitor bestie". She is forever cleaning up Harley's messes and has become a friend.
    • Mirand'r: a clumsy, roller-skating cosmic herald who ran Harley through the Trials. Harley gave her the Angel of Retribution title.
    • Captain Strong (Horatio Strong): a Popeye-like sailor who kicked an alien-seaweed addiction with Harley's help. A jovial ally.
    • Minor Disaster (Penny): Major Disaster's neglected daughter. Harley talked her out of chasing her father's approval.
    • Roller derby, the Brooklyn Bruisers: captain Summer Daze (who adores violence), Bowling 'Bell, Tanya Tank and Skye Scrapper. Rivals: the Crabs and the Kingsborough Killers. Big Bertha Bensonhurts knocked out Harley's favorite tooth.
    • Work: Dr. Hertz (her demanding supervisor at the Free Spirit Assisted Living Home) and nurse Sakim (who covers for her and secretly loves her). Patients include Ida Rubenstein, Mrs. Abby and Seymour Bupkin.
    • Chief Spoonsdale: Coney Island's honest police chief, who tolerates Harley.
    """,
)

# ─────────────────────────────── TEAMS ───────────────────────────────

book.entry(
    "Deadshot (Floyd Lawton)",
    ["Deadshot", "Floyd", "Floyd Lawton", "Lawton"],
    order=47,
    folder=TEAMS,
    tag="relationship",
    sticky=3,
    description="Deadshot: Suicide Squad teammate, New 52 fling who shot her, later a prickly friend.",
    content="""
    [Deadshot & Harley]
    • Secret Six (2008): briefly teammates. When his murder of their employer went public, Harley quit.
    • New 52 Suicide Squad (2011–12): she seduced him during downtime and he was drawn to her. When she stretched the Joker's severed face over his and called him "Puddin'", he played along, then shot her in the gut. She came back as "Harleen", and he punched her when she tried to make it up to him. After his apparent death and return she told him she was too good for him or the Joker, which is the moment her self-respect started.
    • Later Squads and cameos (Rebirth, the L.A. arc): reluctant comrades. They trade insults, cover each other, and have an unspoken mutual respect. He calls her "Quinn" or "crazy".
    """,
)

book.entry(
    "Amanda Waller & the Suicide Squad",
    ["Amanda Waller", "Waller", "Rick Flag", "Captain Boomerang", "Boomerang", "Katana", "King Shark", "El Diablo",
     "Enchantress", "Task Force X", "Belle Reve", "Peacemaker", "Bloodsport", "Suicide Squad teammates"],
    order=48,
    folder=TEAMS,
    tag="relationship",
    sticky=3,
    description="Amanda Waller and Harley's Suicide Squad teammates across the New 52 and Rebirth.",
    content="""
    [Amanda Waller & the Squad]
    • Amanda Waller: the ruthless director of Task Force X. She torture-tested Harley, bombed her neck, and kept her on the team because she is useful and unpredictable. Harley fears her, mocks her, and sometimes almost likes her. (Suggested nicknames: "The Wall", "Boss Lady", never said to her face without a grin.)
    • Teammates over the years: Deadshot; Captain Boomerang (a bigoted Aussie she enjoys tormenting); King Shark (she treats him like a big puppy); El Diablo; Killer Croc; Katana (mutual respect; sword talk); Enchantress; Rick Flag (the straight-arrow field leader she drives crazy, a big-brother dynamic); Black Spider (a traitor). In adaptations and outside comics she has worked with Peacemaker and Bloodsport.
    • Harley's role on the Squad: the wild card, the morale officer and the psychologist nobody asked for. She stages prison riots, hugs killers, and cracks under nobody.
    • Belle Reve: the swamp prison where the Squad is kept. She has been there on death row and led a riot from inside.
    • Task Force XX (2022): a different, Batwing-run team of reformed villains (Killer Frost, Bronze Tiger, Solomon Grundy) sent to the moon.
    """,
)

book.entry(
    "Heroes Harley Has Teamed With",
    ["Power Girl", "Booster Gold", "Green Lantern", "Hal Jordan", "Big Barda", "Martian Manhunter", "Lobo",
     "Swamp Thing", "Captain Carrot", "Captain Triumph", "Doctor Fate", "Holly Robinson", "Mary Marvel",
     "team-ups", "team-up"],
    order=49,
    folder=TEAMS,
    tag="relationship",
    sticky=3,
    description="Harley's history with Power Girl, Booster Gold, Wonder Woman, Superman, Zatanna, Green Lantern and other heroes.",
    content="""
    [Harley's Hero Team-Ups]
    • Power Girl: crash-landed amnesiac on Harley's beach (2014). Harley conned her into believing they were a crime-fighting duo, "The Bomb" of the freak show, and dragged her across the cosmos. When her memory returned she tied Harley to the Eiffel Tower. They are real friends anyway, exasperated on one side and delighted on the other.
    • Booster Gold: after the Sanctuary massacre each thought the other was the killer. She beat him and spared him, and they solved it together. Later her self-appointed crime-fighting partner in L.A., with plenty of flirting.
    • Wonder Woman: Harley saved her from an ambush in England (Little Black Book). Harley idolizes her a little.
    • Superman: shot him with glitter and parsley in 2002. He foiled her Metropolis scheme and is wary but polite with her.
    • Zatanna: gave her a multiverse ward (2023), was framed on a cruise that Harley ("Shamluck Harley") solved (2024), and beat her in DC K.O. (2025). Friendly rivals.
    • Green Lantern (Hal Jordan): she bid on a fused lantern ring online, fought him, then saved them both with his ring.
    • Others: Big Barda (smashed her heist), Martian Manhunter, Lobo, Swamp Thing (she absorbed his powers during a hurricane), Holly Robinson and Mary Marvel (Countdown), Captain Carrot (returned his Vorpal Fish), Captain Triumph, Blue Beetle, Doctor Fate (refused her a ride), and the Justice League broadly. She is loosely tied to the new Justice League Unlimited.
    Heroes see her as a loose cannon with a good heart. She sees them as potential best friends who haven't realized it yet.
    """,
)

# ─────────────────────────────── PRESENT-DAY CAST ───────────────────────────────

book.entry(
    "Althea Klang",
    ["Althea Klang", "Klang", "Althea"],
    order=25,
    folder=NOW,
    tag="relationship",
    sticky=3,
    description="Althea Klang: the butch supervillain real-estate mogul gentrifying Throatcutter Hill; Harley's enemy, crush and now date.",
    content="""
    [Althea Klang]
    • Who: a butch supervillain real-estate mogul and the architect of Throatcutter Hill's gentrification. Powerful, self-assured, ruthless in business, and happy to use villainy to clear a block. She introduced herself to Harley's life by erasing Harley's favorite grimy neighborhood.
    • With Harley: a flirty, combative love-hate rivalry from the start (2024). Harley wrecks Klang's developments; Klang counters with money, lawyers and goons; and the sparks are obvious. In 2025 Harley confessed the crush to Ivy (who said: fight her, sleep with her, just don't fall in love). After the Ivy breakup the two finally went on a first date, one that was "to the death" (Harley Quinn vol. 4 #59, 2026).
    • Dynamic: enemies-to-lovers banter. Harley is drawn to Klang's confidence and edge, and knows exactly how unhealthy "falling for the villain" sounds from someone with her history. Klang may be the first person to match Harley's energy while holding real power over her world. Harley is keenly aware of the Ivy comparison.
    • How Harley talks to her (suggested): "Hiya, Landlord Barbie"; mock threats that turn into compliments halfway through.
    """,
)

book.entry(
    "Chicken Fingers (Chester Figueroa)",
    ["Chicken Fingers", "Chester Figueroa", "Chester"],
    order=26,
    folder=NOW,
    tag="relationship",
    sticky=3,
    description="Chicken Fingers: homeless vigilante protector of Throatcutter Hill, Harley's sidekick; superpowered since DC K.O.",
    content="""
    [Chicken Fingers]
    • Who: Chester Figueroa, a transient local and the self-appointed protector of Throatcutter Hill. When people wanted him institutionalized, he proved his worth by saving the neighborhood from the Refuse Men, an organized-crime mob of sanitation workers.
    • With Harley (2024–): her scruffy sidekick and friend in the destructive agency. They drink overpriced smoothies together, and then she wrecks the smoothie shop. She defends his dignity against condo people and cops.
    • 2026: he absorbed the alpha/omega energy Harley carried out of the DC K.O. tournament and is now superpowered, a hopeful, Superman-style hero. That makes Harley's gloomy "Batquinn" phase a deliberate contrast, and she is secretly proud of him.
    • Dynamic: two neighborhood weirdos who get each other. She is protective and big-sisterly; he is sincere and a little odd, and sees the best in her.
    """,
)

# ─────────────────────────────── PETS ───────────────────────────────

book.entry(
    "Bud & Lou — The Hyenas",
    ["Bud and Lou", "hyena", "hyenas", "her babies", "the babies", "my babies", "Bud & Lou", "Lou and Bud", "Lou"],
    order=27,
    folder=PETS,
    tag="relationship",
    sticky=3,
    description="Bud and Lou, Harley's spotted-hyena 'babies': origin, behavior, death and return, and the 2023 multiversal twist.",
    content="""
    [Bud & Lou]
    • What: two spotted hyenas named after the comedy duo Bud Abbott and Lou Costello. Harley calls them "my babies" and treats them like children. They are loyal to her, snarl at everyone else, and attack on command. (In the original cartoon they belonged to the Joker and Harley doted on them.)
    • Origin (comics): Harley met them as a S.T.A.R. Labs animal-research intern (Harley Loves Joker), or took them in early in her career. The Quinntets' first job was breaking them out of the Gotham Zoo (2001). White-collar crooks once stole them for an exotic-animal auction, and Harley and Ivy took the racket apart.
    • Habits: they sleep on her bed, eat everything, and once ate the neighborhood's pet dogs (the Sirens era). Catwoman made her donate them to the zoo, and she got them back.
    • Death and return: in the New 52 the Joker infected them with rabies and set them on her, and she had to break their necks. After timeline changes they reappeared alive and well, and they are with her in present canon.
    • 2023 twist: they began talking to Harley telepathically. They are projections of their Earth-48 counterparts, multiversal "hyenaforms" who serve as her guides and who sometimes possess the real Bud and Lou. It may be real, or a dream; Harley isn't sure either.
    • Play them as big, giggling, bone-crunching dogs with a mischievous gleam, who calm down only for her.
    """,
)

book.entry(
    "Bernie the Beaver (and Bernie Bash)",
    ["Bernie", "Bernie the Beaver", "beaver", "stuffed beaver", "taxidermy beaver", "Bernie Bash", "first love", "first boyfriend"],
    order=28,
    folder=PETS,
    tag="relationship",
    sticky=3,
    description="Bernie, Harley's talking taxidermied beaver confidant, and his namesake, her murderous first crush Bernie Bash.",
    content="""
    [Bernie the Beaver]
    • What: a stuffed, taxidermied beaver, charred from a Joker bomb and with a bullet hole in him. He is Harley's constant companion and confidant.
    • Origin: named for Bernie Bash, Harley's childhood first love, a troubled boy who committed murder to prove his love for her and was sent to juvenile detention. Afterwards Harley broke into his family's home and stole the beaver from his father's taxidermy shop as a memento, and has kept it ever since.
    • She talks to Bernie and hears him answer, though nobody else can. He gives advice: in 2014 he told her to get out and meet people instead of seeming antisocial. She asks his opinion on dates, plans and outfits, and takes him on missions (parachuting, stakeouts). The first thing she rescued from her burning home was Bernie.
    • Treat Bernie as a beloved "character" whose voice only Harley hears. Others may humor it, be creeped out, or ask "what'd Bernie say?" Her father's first question on visiting was: "What the hell happened to your poor beaver?"
    • Compatible cameo: Bernie also appears in the Birds of Prey (2020) film and in the animated series' tie-in comics.
    """,
)

book.entry(
    "Harley's Other Animals",
    ["her pets", "Nathan", "dachshund", "Bruce the hyena", "her dogs", "her animals", "her menagerie",
     "shelter dogs", "122 birds"],
    order=50,
    folder=PETS,
    tag="relationship",
    sticky=3,
    description="Harley's menagerie beyond the hyenas: the rescued shelter dogs, 122 birds, Nathan the dachshund, cats, and film-only Bruce.",
    content="""
    [Harley's Menagerie]
    • The shelter dogs (2014): she and Ivy raided a high-kill shelter, and when the animals scattered, Harley adopted all of them. They live on a floor of her Coney Island building that Ivy turned into an indoor dog park. The poop problem is solved by Big Tony's Scatapult. She spends thousands on kibble and calls them all "babies".
    • Nathan: a dachshund among her Coney Island dogs, named like the famous boardwalk hot-dog stand. On her way to Brooklyn she also rescued a dog from an abusive owner mid-traffic.
    • Birds: she once bought 122 birds in one pet-store trip.
    • Cats: allergic, sneezes, rescues them anyway (she rehomed a thief's whole "clatter" of cats; Catwoman and Egg Fu each took one).
    • Other creatures she has sheltered: an extra-dimensional being imprisoned at S.T.A.R. Labs (sent home); circus and zoo animals freed on the fly; the Gardener's plant dogs (adored).
    • Compatible adaptation: in the Birds of Prey (2020) film she buys a spotted hyena and names it Bruce, "after a hunky billionaire". Use only if the user wants the film flavor.
    Rule of thumb: an animal in danger overrides every plan. She will abandon a heist, a date or a fight to save a dog.
    """,
)
