from lb import Book

book = Book(
    "Harley Quinn — 02 Canon History",
    """
    Harley Quinn's comic-book history, in order: every origin version, the New Earth
    years (1999–2011), the New 52 (2011–2016), Rebirth (2016–2021), Infinite Frontier
    and Dawn of DC (2021–2024), and DC All In (2024–present). Each entry covers one
    era or arc and is triggered by its names, places and villains. Where canon
    contradicts itself, the entry says so and gives the reading that fits best today.
    """,
    category="character",
    tags=["Harley Quinn", "DC Comics", "history", "timeline", "canon"],
    scan_depth=6,
    token_budget=4500,
    entry_limit=12,
)

ORIGIN = book.folder("01 · Origins (all versions)")
NEWEARTH = book.folder("02 · New Earth Era (1999–2011)")
N52 = book.folder("03 · New 52 Era (2011–2016)")
REBIRTH = book.folder("04 · Rebirth Era (2016–2021)")
IF = book.folder("05 · Infinite Frontier & Dawn of DC (2021–2024)")
ALLIN = book.folder("06 · DC All In — Present Day (2024–)")

# ─────────────────────────────── ORIGINS ───────────────────────────────

book.entry(
    "Origin — Mad Love (the classic version)",
    ["Mad Love", "how she met the Joker", "how Harley met", "fell in love with the Joker", "first met the Joker",
     "origin story", "her origin", "backstory", "became Harley", "Arkham intern", "internship at Arkham",
     "piranha", "piranhas", "rose in a vase", "Feel better soon"],
    order=40,
    folder=ORIGIN,
    tag="event",
    sticky=2,
    description="The definitive 1994 origin (Dini & Timm): Arkham intern Harleen falls for the Joker; the piranha trap; the rose.",
    content="""
    [Origin I — "Mad Love" (The Batman Adventures: Mad Love, 1994; adapted in The New Batman Adventures, 1999)]
    The template for every later version, and the story most fans mean by "Harley's origin".
    • Harleen Quinzel, a gymnast on a Gotham State scholarship and an ambitious psychology student with a reputation for charming her way to good grades, took an internship at Arkham Asylum. She wanted the most famous patient of all for her career, and possibly a best-selling book.
    • The staff warned her off. She insisted and got sessions with the Joker. He played her perfectly: sad stories about an abusive, alcoholic father (one of many versions he tells), jokes just for her, and the claim that Batman was the cause of his misery. She fell head over heels, blamed Batman, and began slipping him favors.
    • After one of his escapes, Batman brought him back battered. Harleen snapped. She bought a harlequin costume from a novelty shop, broke him out, and introduced herself as Harley Quinn.
    • Years later, fed up with being ignored, she dug up one of the Joker's own abandoned death traps: Batman hung upside down over a tank of piranhas. She came closer to killing Batman than the Joker ever had. Batman, hanging there, laughed at her and pointed out that the Joker would never forgive her for doing it first and not "getting the joke". She called the Joker to prove her love. Enraged, he knocked her out a window.
    • Broken in an Arkham bed, she swore she was finished with him. Then she saw a single rose in a vase with a card, "Feel better soon — J", and sighed, "My angel."
    Themes: love as self-destruction; the Joker's cruelty and insecurity; Harley's brilliance wasted on him. It won the Eisner and Harvey awards for Best Single Issue.
    """,
)

book.entry(
    "Origin — Batman: Harley Quinn (1999, No Man's Land)",
    ["No Man's Land", "rocket", "Robinson Park", "earthquake", "Cataclysm", "license revoked", "Batman: Harley Quinn",
     "first comic origin", "how she got her powers", "Ivy saved her", "Ivy found her"],
    order=41,
    folder=ORIGIN,
    tag="event",
    sticky=2,
    description="Harley's 1999 entry into the main DC Universe: the Joker's rocket, Ivy's serum, and the Joker's apology during No Man's Land.",
    content="""
    [Origin II — Batman: Harley Quinn #1 (1999, Paul Dini & Yvel Guichet), set during No Man's Land]
    This is how Harley entered mainstream DC continuity. It is darker than Mad Love.
    • As a psychology intern, Harleen landed Joker sessions and fell for him. After she helped him escape more than once, the authorities caught on. They revoked her license and locked her in her own asylum as an inmate.
    • An earthquake leveled Gotham (the "Cataclysm" that led to No Man's Land) and freed her. She became Harley Quinn at the Joker's side.
    • In a quake-shattered, quarantined Gotham, the Joker admitted to himself that he really felt something for her. Because those feelings got in the way of his "purpose", he decided to kill her by strapping her to a rocket and launching it.
    • She crashed in Robinson Park, where Poison Ivy found her. Ivy nearly killed her, then got curious about why the prospect of dying didn't move her, and heard her story. Ivy saw a fellow castoff, nursed her in her toxic-waste-dump lair, and injected her with an experimental serum: toxin immunity, and enhanced strength, speed and agility (see Core "Powers").
    • Harley and Ivy went on a successful crime spree. Harley even helped Batman take down the Joker's gang. She chased the Joker up a ruined building to throw him off, but he apologized, and she melted and went back to him. She served as his lieutenant through the rest of No Man's Land and the Emperor Joker saga. Disgusted, Ivy ended the partnership, but remained Harley's first call whenever the Joker hurt her again.
    """,
)

book.entry(
    "Origin — New 52 Revision (Ace Chemicals)",
    ["Ace Chemicals", "Ace Chemical", "chemical vat", "vat of chemicals", "vat", "pushed her in", "jumped in",
     "bleached skin", "why is her skin white", "Dr. Sterano", "Sterano", "drunk driver", "tenth session",
     "undercover as a patient", "New 52 origin", "mosaic"],
    order=42,
    folder=ORIGIN,
    tag="event",
    sticky=2,
    description="The 2011–2014 revision: undercover at Arkham, the drunk-driver finger, Dr. Sterano, and the plunge into Ace Chemicals that bleached her skin.",
    content="""
    [Origin III — The New 52 (Suicide Squad #6–7, 2012; Detective Comics #23.2; Secret Origins #4, 2014)]
    • Harleen, an honor student and gymnast, studied at Gotham University. She switched from veterinary and biological science to psychology, excelled, and transferred to Arkham because the other doctors couldn't reach the patients. She even went undercover as an inmate to study them. The Joker saw through her disguise at once, and was impressed.
    • She never swallowed his sob stories. At their very first session she threatened him when she spotted the knife he had smuggled in. On their tenth session he "gifted" her the severed finger of a rich drunk driver who, he claimed, had killed her father and walked free. He promised to teach her to stop caring about the rules. (Later canon has her father Nick alive, so treat this as a Joker lie or a discarded retcon.)
    • Her supervisor, Dr. Sterano, stole her session notes to publish as his own and discovered her feelings. In a rage she tried to kill him, killed a guard instead, and broke the Joker out.
    • That night at Ace Chemicals, where his own "birth" happened, the Joker called it her birthday and shoved her into a vat. She came out alive, with bleached-white skin and, as he saw it, freed from reality. He named her Harley Quinn. Years later she tracked down Sterano and killed him.
    • She then assembled her costume as "a mosaic of all the people she was or wanted to be", and repressed her guilt along with Harleen.
    Continuity note: fans disliked that this version took away Harley's choice. Later Rebirth-era storytelling (and the 2016 film's iconic image) frames the plunge as Harley diving in herself, and some accounts call "he pushed me" a story she told herself. When roleplaying present-day Harley, say she went into the vat, that it bleached her skin, and that whether she jumped or was pushed is a sore spot she answers differently depending on her mood.
    """,
)

book.entry(
    "Origin — Modern Consensus & Harley Loves Joker",
    ["Harley Loves Joker", "Jake's Joke Shop", "Jenna Duffy", "The Grison", "March Harriet", "costume change",
     "why she changed costume", "old days with the Joker", "back when she was with the Joker", "Joker years",
     "henchwoman days", "the Carpenter"],
    order=43,
    folder=ORIGIN,
    tag="event",
    sticky=2,
    description="Rebirth-era flashbacks (Harley Loves Joker, 2017–18) and the working modern version of her past with the Joker.",
    content="""
    [Origin IV — The Modern Working Version]
    Present-day canon keeps the essentials of all versions:
    1. Brooklyn girl, gymnast, PhD psychologist.
    2. Arkham assignment to the Joker. He manipulated her, she fell in love, and she freed him.
    3. Years as his partner, lover and punching bag.
    4. Poison Ivy's rescue and serum.
    5. Chemically bleached skin.
    6. A long, hard break with him, and a life of her own.
    Harley Loves Joker (backup stories in Harley Quinn vol. 3 #17–25 plus a 2-issue mini, 2017–18, by co-creator Paul Dini with Jimmy Palmiotti) shows the old days with more balance: Harley as the Joker's near-equal, not a doormat. In these flashbacks:
    • She interned in animal research at S.T.A.R. Labs before Arkham, which is where she met the hyenas Bud and Lou.
    • She secretly moonlighted as the cat-burglar "The Grison", out-heisting the Joker's own jobs, and took tea with fellow crooks March Harriet and Jenna Duffy, "the Carpenter".
    • She had the Carpenter build a luxury secret hideout (pool, hyena run, big-top bedroom) that became "Jake's Joke Shop". The bill came to $3 million. When Harley balked, Jenna planted bombs in the walls and gave her seven days to pay.
    • The Joker grew suspicious of her absences. The story ends by explaining why she swapped the classic jester suit for her modern look: it marked her leaving him.
    Birthday-party and Robin flashbacks (25th Anniversary Special) belong to this era too.
    """,
)

# ─────────────────────────────── NEW EARTH ───────────────────────────────

book.entry(
    "Solo Career & the Quinntets (2000–2001)",
    ["Quinntets", "Quinntettes", "Lewis LeBeau", "Lester Wilde", "Buster", "Two-Bear", "Kenny Two-Bear", "Nix Two-Bear",
     "Margo", "Jack Happi", "Happy Jack", "Carrie Chispazo", "Bo Donner", "Frank Surley", "Two-Face job",
     "slumber party", "sleepover", "Wayne Manor heist", "Big Barda", "Rose and Thorn", "Finger Warehouse", "H.Q.H.Q."],
    order=50,
    folder=NEWEARTH,
    tag="event",
    sticky=2,
    description="Harley Quinn vol. 1 #1–13 (Kesel/Dodson): breaking up with the Joker, working for Two-Face, the Quinntets gang, the Wayne Manor heist.",
    content="""
    [Harley Quinn vol. 1 #1–13 (2000–2001), by Karl Kesel & Terry Dodson: "love gone horribly, terribly wrong"]
    • #1: Harley breaks the Joker out of Arkham and helps him build a death-trap roller coaster. Sick of her "mothering", he shoots her, but it is Poison Ivy in her place, a precaution Ivy took. He tries to kill her anyway, and Harley breaks up with him.
    • #2: Heartbroken, she takes a job with Two-Face kidnapping Oscar Cartwright for two ransoms, from his wife and his mistress. The two women turn out to be one woman with a split personality. Moved by Oscar's acceptance of her, Harley turns on Two-Face, then quietly blackmails the wife herself. Crime boss "Happy" Jack Happi starts hunting her.
    • #3: Harley throws a villainess slumber party at her new hideout, with Catwoman, Ivy, Hope, Mercy, the Body Doubles and the masked "Pagan". Truth-or-dare unmasks Pagan as Rose and Thorn. The girls want Harley to lead a team; she declines. Catwoman secretly steals Harley's cash reserves.
    • #4–5: She forms her own gang, the Quinntets: ex-Joker henchmen Lewis LeBeau and Buster, Lester Wilde (who insists he looks like the Joker), the Two-Bear brothers Kennedy "Kenny" and Nixon "Nix", and later Brad. Their first job frees her hyenas Bud and Lou from the Gotham Zoo (Wilde is shot and killed). She robs the Finger Warehouse of oversized heist props, taking only one piece, which reminds her of her first boyfriend. Her HQ is "H.Q.H.Q." in the Glover Building.
    • #5–8: Bounty hunters Bo Donner and Frank Surley, joined by ex-FBI profiler Dr. Carrie Chispazo, dig into her past, including a field trip to Gotham State University.
    • #6–7: She robs Bruce Wayne's Halloween charity gala. She clashes with his bodyguard Sasha Bordeaux, her hacker recruit Margo betrays her for the bounty and "dies" by dynamite, the Riddler's gang crashes in, and Big Barda wrecks everyone.
    • #9–13: Killer Croc takes her captive, a mystery "original Batgirl" appears, Matches Malone joins the Quinntets, and the Our Worlds at War special has her drive Jimmy Olsen to Metropolis in the Jokermobile, confusing Female Furies along the way.
    """,
)

book.entry(
    "Metropolis, Holly Chance & the Afterlife Trip (2002)",
    ["Daily Planet", "Holly Chance", "love columnist", "advice column", "Bizarro", "Highwater",
     "glitter and dried parsley", "World Without Harley", "Martian Manhunter", "Harley in Metropolis"],
    order=51,
    folder=NEWEARTH,
    tag="event",
    sticky=2,
    description="Harley Quinn vol. 1 #14–25: moving to Metropolis with Ivy, the Daily Planet love column, Bizarro's crush, death and escape from the afterlife.",
    content="""
    [Harley Quinn vol. 1 #14–25 (2002)]
    • "Bright Lights, Big City": fleeing the Gotham bounty, Harley and Ivy move to Metropolis. After a brawl with Thorn and a run from the Special Crimes Unit, they settle into the apartment of a suicidal Ms. Chance. Harley becomes "Holly Chance", the dead woman's "niece".
    • She flirts with neighbor Jimmy Olsen until he introduces her to Perry White, and with help from Ivy's pheromones she lands a job as the Daily Planet's love-advice columnist. Her advice is chaos. She crosses paths with Clark Kent and shoots Superman with glitter and dried parsley ("You shot me with glitter and dried parsley?").
    • Bizarro falls in love with her and chases her with dead flowers; the real Superman shuts down her biggest scheme.
    • #20–22: Harley "pays the ultimate price" and dies, ending up in a supernatural prison "way, way below". She escapes by getting past Highwater, the doorman of the great beyond, through his heart rather than her fists.
    • #23: "World Without Harley": Martian Manhunter, in his private-eye guise, picks up a case that leads back to her.
    • #25 (Kesel's finale): the Joker returns "with something less than romance in his heart", with Batman guest-starring, to test whether she really renounced him.
    """,
)

book.entry(
    "Vengeance Unlimited — Dr. Jessica Seaborn (2003)",
    ["Vengeance Unlimited", "Jessica Seaborn", "Detective Bishop", "cop killer", "killing a police officer",
     "orphan girl", "$500,000", "serum wearing off", "Cupid of Crime"],
    order=52,
    folder=NEWEARTH,
    tag="event",
    sticky=2,
    description="Harley Quinn vol. 1 #26–38 (Lieberman): framed for a cop's murder, the fake shrink Dr. Seaborn, Ivy's serum failing, the Joker's last con.",
    content="""
    [Harley Quinn vol. 1 #26–38 (2003), by A.J. Lieberman: grittier crime noir]
    • Back in Gotham, Harley is wanted for murdering a police officer (a frame she disputes). Dogged Detective Bishop swears to take her down for killing his partner.
    • She hides in plain sight as psychiatrist "Dr. Jessica Seaborn", in a new, sort-of costume, treating patients so disturbed they make her look sane. Her confidant is a man called "Doc", with whom she talks about love.
    • She gets shot, twice. She discovers the Joker may have had a hand in framing her, leading to a fateful confrontation with "the one-time love of her life".
    • A stalker whose obsession "can bring down buildings" hunts her, and someone kills him before she can.
    • Bishop meets "Dr. Seaborn" without knowing who she is, and asks her out. The Joker crashes the date: "We're perfect together, Harley."
    • #30 reveals Ivy's serum lets her breathe underwater. In #31 the serum turns on her. Without a plant compound Ivy made, her body starts to fail, and she tears through Gotham's bottom-feeders to get it back.
    • #34–35: for a $500,000 score she protects an orphaned 11-year-old girl hunted by every mob family in Gotham, and ends up caring about the kid.
    • #38 (finale): the apparent arrest of the Joker sends her into paranoia, and he turns the tables on her once more.
    """,
)

book.entry(
    "Arkham, Parole, Secret Six & Countdown (2005–2008)",
    ["Ventriloquist", "Peyton Riley", "Arnold Wesker", "Scarface", "Secret Six", "Clown at Midnight",
     "Amazon shelter", "women's shelter", "Holly Robinson", "Granny Goodness", "Themyscira", "Mary Marvel",
     "Thalia", "shot the Joker", "Countdown to Final Crisis", "her parole"],
    order=53,
    folder=NEWEARTH,
    tag="event",
    sticky=2,
    description="Mid-2000s: voluntary Arkham stay and parole, the Joker's plan to kill her, the Secret Six, and the Amazon shelter in Countdown.",
    content="""
    [New Earth, 2005–2008]
    • One Year Later: Harley voluntarily commits herself to Arkham. For a year her parole requests are rejected by the layman on the medical board, Bruce Wayne.
    • Peyton Riley, the new female Ventriloquist, kidnaps her and offers her a job. Harley refuses out of respect for Arnold Wesker, the original Ventriloquist, who tried to cheer her up during her first lonely week in Arkham. She helps Batman and Gordon foil Riley. Impressed, Bruce grants her parole (Detective Comics #831).
    • "The Clown at Midnight" (Batman #663): she helps the Joker with a plan to kill all his former henchmen, not realizing the "punchline" is her own death. When she figures it out, she shoots him in the shoulder.
    • She briefly joins the Secret Six as its sixth member. When Oracle leaks footage of teammate Deadshot murdering their double-crossing employer, she asks: "Is it a bad time to say 'I quit'?"
    • Countdown to Final Crisis (2007–08): a reformed Harley, out of costume and dressed in an Amazonian chiton, works at an Amazon-run women's shelter. She befriends ex-Catwoman fill-in Holly Robinson. "Athena" (secretly Granny Goodness) takes them to Themyscira for Amazon training. With the real Athena and Mary Marvel they expose Granny, follow her to Apokolips, and free the captive Olympian gods. Thalia grants Harley powers as a reward; they vanish once she returns to Earth, and Harley and Holly go home to Gotham.
    """,
)

book.entry(
    "Gotham City Sirens (2009–2011)",
    ["Gotham City Sirens", "Sirens", "Boneblaster", "animal shelter", "cat and dog shelter", "Riddler's townhouse",
     "Gaggy", "Christmas in Brooklyn", "visited her family", "Bentley", "Gotham County Arboretum", "Arboretum",
     "Arkham takeover", "Arkham riot", "Cash Gordon", "Alisa Adams", "Dr. Paula Irving", "the Broker"],
    order=54,
    folder=NEWEARTH,
    tag="event",
    sticky=2,
    description="The Harley/Ivy/Catwoman team book: shared hideouts, the Bensonhurst Christmas, the hyenas' dog problem, betrayal and the Arkham takeover.",
    content="""
    [Gotham City Sirens #1–26 (2009–2011), by Paul Dini, Guillem March and others]
    • Harley and Ivy are squatting in the Riddler's townhouse, keeping him pheromone-controlled, when Catwoman, weakened after Hush stole her heart, gets ambushed by the upstart Boneblaster. The three beat him and Selina proposes they band together. Ivy's condition: Catwoman must reveal Batman's identity. Selina can't; Talia had magically buried the secret in her mind.
    • The Broker finds them a hideout: the abandoned Gotham City Shelter for Cats and Dogs, which Harley warmly calls home. Later they move to the closed Gotham County Arboretum.
    • Harley meets "Bruce Wayne" (really Hush in disguise) and then survives a jealous "Joker" attack, which turns out to be a Joker impersonator from his old gang. Gaggy (Gagsworth A. Gagsworthy) also turns up.
    • #7, Christmas: she visits her family in Bensonhurst. Her lazy brother Barry is chasing rock stardom, and her mother Sharon wants her to quit "the villain and hero stuff". She visits her swindler father in prison, realizes he is only fishing for where she stashed money, and finds he has sold a guard a photo op with her. She storms back to Gotham to spend Christmas with Selina and Ivy.
    • #11: neighborhood dogs, including Bentley, go missing. Bud and Lou have been eating them while sleeping on Harley's bed. Selina makes her donate the hyenas to the Gotham Zoo. Ivy takes a S.T.A.R. Labs job as "Dr. Paula Irving" and is trapped by a vengeful assistant, Alisa Adams.
    • #19–26: Selina's confessions about Batman stir up Harley's memories of the Joker. She knocks out her friends with Joker bombs and goes to Arkham swearing to kill him, but can't; she frees him instead. Together they seize the asylum, killing or holding staff hostage. When Ivy makes her choose, Harley blindsides her. Batman and Catwoman, with Cash's lighting trick, take the couple down, and Harley is wheeled off in a straitjacket and muzzle. Ivy, betrayed and abandoned by Selina, breaks Harley out to kill Catwoman together. In the final fight Selina says she only ever saw good in them, and helps them escape Batman.
    """,
)

# ─────────────────────────────── NEW 52 ───────────────────────────────

book.entry(
    "Suicide Squad Conscript (2011–2014)",
    ["Suicide Squad", "Task Force X", "Belle Reve", "Amanda Waller", "micro-bomb", "nanobomb", "neck bomb",
     "Floyd Lawton", "Basilisk", "Regulus", "Black Spider", "El Diablo", "Joker's face", "Death of the Family",
     "Red Hood costume", "rabies", "killed Bud and Lou", "Black Canary", "New 52 Suicide Squad"],
    order=55,
    folder=N52,
    tag="event",
    sticky=2,
    description="New 52 Suicide Squad (Adam Glass): Belle Reve, the Deadshot fling, the Joker's face, his return, and the death of the hyenas.",
    content="""
    [Suicide Squad vol. 4 (2011–2014) and related]
    • Black Canary arrests her mid-revenge spree against the lawyers who put the Joker away. On death row at Belle Reve she is gassed, tortured to test her loyalty, implanted with a micro-bomb, and drafted into Amanda Waller's Task Force X, alongside Deadshot, King Shark, El Diablo, Captain Boomerang and others, against the terror group Basilisk.
    • She seduces Deadshot during downtime. When a guard accidentally disables her bomb she stages a Belle Reve riot, then flees to Gotham after hearing the Joker died. There she enlists escaped Arkham inmates, kills Dr. Sterano, gets herself arrested on purpose, and steals the Joker's severed face from GCPD evidence. She knocks Deadshot out, stretches the face over his and talks to him as the Joker. Playing along, he orders her to kill the Bat-family, then shoots her in the stomach.
    • Nearly dying, she dissociates and insists she is only "Dr. Harleen Quinzel". Waller keeps her on anyway. The Squad is betrayed by Black Spider, and Deadshot seemingly dies killing Regulus.
    • At Deadshot's funeral, a Joker-gas attack drops everyone but Harley (she is immune). The Joker is back, wearing his own cut-off face, and he is jealous and vicious. She lures Batman into a chemical trap in the Joker's old Red Hood costume, but warns him that the Joker has changed. The Joker chokes her with a chain and sets her own hyenas, infected with rabies, on her. She has to kill Bud and Lou. She tries to kill him and fails, and slits her own wrists to get out of his cuffs.
    • Recovering, she tells Deadshot she is too good for him or the Joker. The run ends with Forever Evil (2014). She continues in New Suicide Squad (2014–16).
    Note: Bud and Lou later reappear alive (timeline alterations), so their deaths are not permanent in present canon.
    """,
)

book.entry(
    "Coney Island Arrival — Hot in the City (2013–2014)",
    ["Coney Island", "Hot in the City", "inherited a building", "inherited the building", "Robert Coachman",
     "bounty on her head", "two million dollars", "hit on Harley", "Free Spirit", "nursing home", "Ida Rubenstein",
     "Rubenstein", "Russian agents", "Syborg", "Zena Bendemova", "The Bear", "El Torito", "Brooklyn Assassins Guild",
     "sleepwalking", "put a hit on herself", "dog park", "kill shelter", "King Hill Pet Adoption"],
    order=56,
    folder=N52,
    tag="event",
    sticky=2,
    description="Harley Quinn vol. 2 #0–8 (Conner/Palmiotti): inheriting the Coney Island building, jobs, the bounty mystery, and Sy Borgman's Russian hit list.",
    content="""
    [Harley Quinn vol. 2 #0–8 (2013–2014), by Amanda Conner & Jimmy Palmiotti]
    • #0: a Joker bomb destroys her storage-unit home. Clutching Bernie the beaver, she learns from lawyer Robert Coachman that an anonymous former Arkham patient left her a four-story building on Coney Island in his will. She rides to Brooklyn on a motorbike, whips a man who is dragging his dog and adopts the dog, then punts a bounty hunter's head off with her hammer.
    • The building has shops on the ground floor, including a freak show, a burlesque theater and Madame Macabre's House of Wax and Murder. Eight apartments on the second floor, storage on the third, and the whole fourth floor is hers, with an express elevator and roof access. The catch: back taxes, insurance and upkeep. Big Tony welcomes her and becomes her right hand.
    • To pay the bills she covers her white skin with makeup and takes two jobs: therapist at the Free Spirit Assisted Living Home, and skater with the Brooklyn Bruisers roller-derby team (she wins the tryout by being the last woman standing). Someone has posted a $2 million bounty on her.
    • #2: she and Ivy break into a kill shelter. The freed animals run wild, so Harley adopts them all, and Ivy turns the empty third floor into a dog park. #3: Ivy's pheromone berries make every man (and one policewoman) fall for her on Valentine's Day.
    • #4: a patient's supposedly neglectful family gets bulldozed, and then she learns Mrs. Rubenstein has Alzheimer's and they visit her three times a week. Oops. Sy Borgman, a cyborg ex-agent, recruits her to finish off the elderly Russian agents who crippled him in the 1960s. They take out Igor Lenivetskin, Ivana Brekemoff, "The Bear" (eaten by his own bears) and the rest at the Prospect Park Zoo. Sy's old flame Zena Bendemova ends up on a rhino horn. The "eighth man" is Chuck, who sold Sy a lemon '59 El Torito.
    • #7: Ivy discovers Harley has been sleepwalking and posting her own bounty from her laptop. They confront the Brooklyn Assassins Guild and call off the hit.
    • #8: she pawns Brekemoff's rings, gets kicked off the Bruisers for playing croquet with an opponent's head, is invited to the underground Skate Club, and unveils the Scatapult (see World lorebook).
    """,
)

book.entry(
    "Power Girl, Mason & the Assistant Crisis (2014–2015)",
    ["Power Outage", "Power Girl", "Kara", "amnesia", "The Bomb", "Beatriz La Bomba", "Clock King", "Sportsmaster",
     "Vartox", "Manos", "Eiffel Tower", "Edwin", "fan club", "Skate Club", "Maria Monsterella", "Mason Macabre",
     "burlesque", "Kiss Kiss Bang Stab", "Egg Fu", "Eggy", "Dr. Bash", "Dr. Bliss", "Hurl Girl", "Sakim", "Mrs. Abby",
     "Little Black Book", "bachelor auction", "The Cod"],
    order=57,
    folder=N52,
    tag="event",
    sticky=2,
    description="Harley Quinn vol. 2 #9–14, the Annual, the Power Girl mini and the specials: stalker Edwin, Mason, Power Girl's amnesia, Egg Fu, overwork.",
    content="""
    [Harley Quinn vol. 2 #9–14, Annual #1, Harley Quinn & Power Girl #1–6, specials (2014–2015)]
    • #9: filling in at the burlesque show, Harley causes a riot, gets "arrested" by Edwin (the president of her fan club, in a stolen cop uniform) and locked in a cage on Staten Island. She could leave any time, but psychoanalyzes him instead, makes him agree to a year of therapy, then punishes the comic-shop guys who mocked her.
    • #10: at Skate Club (no rules; anyone on wheels) she blows her giant opponent Maria Monsterella in half with Sy's explosive toothpaste and is disqualified. She meets handsome Mason Macabre, Madame Macabre's son, fresh out of Rikers on a bum rap, who helped her load Sy's chair. At sunrise, Power Girl crashes into the beach at her feet.
    • #11–13 and the mini: Power Girl has amnesia. Harley convinces her they are a crime-fighting duo who share an apartment, with a secret identity as "The Bomb", the strongwoman in the freak show. Big Tony adds that he and Power Girl were lovers. Clock King and Sportsmaster teleport them across space (a dog-king, the tyrant Manos, a near-forced marriage to Vartox). Back home, a bird poops on Power Girl's head and her memory returns. She ties Harley to the top of the Eiffel Tower and leaves her there.
    • Annual #1 (scratch-and-sniff): Harley launches herself to Gotham via the Scatapult to rescue Ivy from Arkham doctors Bash and Bliss. They are working for Egg Fu (Edgar Fullerton Yeung), who wanted a likability potion because he was being evicted. Everyone hallucinates on gas. Harley gives Egg Fu an apartment, and he becomes the tenant "Eggy".
    • Valentine's Special: Harley has a crush on Bruce Wayne (not knowing he is Batman), wins a date with him at a bachelor auction, and rescues him from the fish-villain "The Cod". Harley's Little Black Book (2016–17) has her team up with Wonder Woman, Green Lantern (she wins a fused ring and puts on Hal's), Zatanna, Superman, Lobo and more.
    • #14, "A Day in the Life": overwork collapses everything. The water heater bursts, pets go hungry, and a patient, Mrs. Abby, collapses (Harley revives her). Nurse Sakim covers for her, but she misses the derby bout and has to cancel her dinner date with Mason. When Mason finds her out with the derby girls instead, he feels lied to.
    """,
)

book.entry(
    "Gang of Harleys, Captain Strong & the Road Trip (2015)",
    ["Gang of Harleys", "Gang of Harley", "brassy lassies", "help wanted", "Dreamin' Seaman", "Holly Hamden", "Coach",
     "Captain Strong", "alien seaweed", "Road Trip Special", "Uncle Louie", "Aunt Alice", "Las Vegas", "Sam Goldstones",
     "Los Angeles", "Hollywood", "kidnapped girl", "Harley Sinn", "Harleen Sinette", "Sinn-Dicate"],
    order=58,
    folder=N52,
    tag="event",
    sticky=2,
    description="Harley Quinn vol. 2 #15–21, the Road Trip Special and Gang of Harleys mini: recruiting twelve Harleys, Captain Strong, Vegas and L.A.",
    content="""
    [Harley Quinn vol. 2 #15–21, Road Trip Special, Harley Quinn and Her Gang of Harleys #1–6 (2015–2016)]
    • #15: Harley saves people from the arsonist Tinderbox and vents to Ivy over wine. Mason forgives her and asks her out properly. Ivy suggests an assistant, and Harley posts a want-ad for "a few brassy lassies willing to make the world a better place" (twelve spots).
    • #16: about eighty women apply. After interviews, she turns off the lights for two minutes and hires whoever is still standing. The Gang of Harleys moves into the Dreamin' Seaman, a derelict hotel (once a Russian mob torture den) she bought for $200,000 with a blackmailed credit card. Holly Hamden, known as "Coach", runs operations from the wheelchair-accessible first floor. Queenie designs uniforms. One rejected applicant, Harleen Sinette, will return as the villain Harley Sinn.
    • #17–19, "A Call to Arms": the Gang's first missions. Popeye-parody sailor Captain Strong, addicted to alien seaweed, kidnaps people onto his boat. Harley and Ivy rescue the Gang, and Strong gets clean and becomes a friend.
    • #19–21: Harley goes to Los Angeles to rescue a kidnapped girl. She fights Deadshot, meets a movie producer, and kills a gang-banger, then heads home.
    • Road Trip Special: Harley, Ivy and Catwoman take a cross-country trip tied to the death of her Uncle Louie (introducing her Aunt Alice). In Las Vegas they return a casino owner's money, Sam Goldstones comps them the presidential suite, and Harley throws a party that ends with him and her motorcycle crashing out a window onto the Strip. She pinky-swore never to tell what happened next.
    • Gang of Harleys mini (Tieri/Palmiotti): the Gang, which includes Bolly Quinn, Carli Quinn, Coach, Hanuquinn, Harlem Harley, Harley Queens, Harvey Quinn and the DiAngelis "Quinntuplets", faces Harley Sinn and her Sinn-Dicate while Harley is away.
    """,
)

book.entry(
    "The Joker's Last Laugh & Red Tool (2015–2016)",
    ["Joker's Last Laugh", "back to Arkham", "rescued Mason", "beat up the Joker", "beat the Joker",
     "first kiss with Ivy", "Red Tool", "Wayne Wilkins", "Chief Spoonsdale", "Spoonsdale",
     "Black, White and Red All Over", "mech suit"],
    order=59,
    folder=N52,
    tag="event",
    sticky=2,
    description="Harley Quinn vol. 2 #22–30: Mason in peril, Harley's return to Arkham and her decisive beating of the Joker; Red Tool's arrival.",
    content="""
    [Harley Quinn vol. 2 #22–30 (2015–2016)]
    • #22–24: Russian gangsters, multiple abductions, and "prison boyfriend woes". Mason Macabre is jailed again and ends up in deep trouble. The most violent issues of the run.
    • #25, "The Joker's Last Laugh": Harley goes back to Gotham and Arkham for the first time in over two years to save Mason, and comes face to face with the Joker. With Ivy at her side she beats him down and walks away, finally free of him on her own terms ("Gotham's so pretty from this distance... I've changed, too. I love the home I have now."). Batman lets them go. Harley and Ivy's relationship turns openly romantic, and a sexual relationship is alluded to. The writers confirmed they are "girlfriends without the jealousy of monogamy". It also sets up her Rebirth look: new hair with dyed tips.
    • #26–28: Coney Island has a new honest police chief, Spoonsdale. Red Tool (Wayne Wilkins) arrives, a Deadpool-parody vigilante obsessed with Harley. He kidnaps her in a clumsy attempt to woo her, and it turns into a surprisingly sweet, lopsided friendship.
    • #29: a one-shot in which Harley pilots a giant Harley-shaped mech suit (cluster missiles fire from its rear) against gangsters, with Big Tony, Bernie and Ivy.
    • #30: a gentle, done-in-one finale featuring Ivy and a Mr. Woodson, leading into the Rebirth relaunch.
    """,
)

# ─────────────────────────────── REBIRTH ───────────────────────────────

book.entry(
    "Rebirth Coney Island I — Zombies, the Fake Joker, Red Meat (2016–2017)",
    ["Die Laughing", "zombie", "zombies", "Vertigax", "alien hot dog", "Joker Loves Harley", "fake Joker",
     "Red Meat", "cannibal", "cannibals", "Madison Berkowitz", "Bat-Fan", "Devani", "Batwoman from the future",
     "Future Kill", "Red Roses", "Unconquerable 25", "Gossamer"],
    order=60,
    folder=REBIRTH,
    tag="event",
    sticky=2,
    description="Harley Quinn vol. 3 #1–21: alien-zombie outbreak, Ivy vacation, the fake Joker, the homeless-cannibal plot, the future Batwoman.",
    content="""
    [Harley Quinn vol. 3 #1–21 (2016–2017), by Conner & Palmiotti]
    • "Die Laughing" (#1–7): the alien Vertigax crash-lands disguised as a cow, gets butchered, and is ground into Coney Island hot dogs. Everyone who eats one becomes a zombie. Harley, Ivy, Big Tony and Red Tool save Coney Island. The arc also establishes the corrupt New York Mayor DePerto and his aide Madison Berkowitz.
    • #8–13, "Joker Loves Harley": Harley takes Ivy to the Bahamas and tries to win her into something more permanent. Back home, a "kinder, gentler" Joker starts courting her again, despite everyone believing him dead, and red-faced Red Tool tries to stop him. He turns out to be a fake Joker. A holiday issue has Harley save Santa by going inside his brain.
    • "Red Meat" (#14–19): New York's homeless are disappearing. Harley, Red Tool and Ivy uncover cannibals feeding on them. The cannibals are entangled with the Mayor's office: his aide Madison Berkowitz wants them out of the city quietly. Chief Spoonsdale investigates the "Cannibal Killer" until the Mayor shuts him down.
    • #20–21, "Future Kill"/"Red Roses": Bat-Fan, the future Batwoman Devani Kage, arrives with a year before being pulled back to her own time, convinced Harley must die to save existence. She later teams with Red Tool to judge Harley up close. Red Tool finally declares his love.
    • "Gossamer" and a Big Tony secret-origin backup follow (#34).
    """,
)

book.entry(
    "Family Circles, Vote Harley & Mason's Death (2017–2018)",
    ["Family Circles", "Moonlighter", "parents visit", "Vote Harley", "running for mayor", "Mayor DePerto",
     "DePerto", "Fire Island", "Mason died", "Mason's death", "Exit Tragedy", "Penguin donation",
     "Harley for Mayor", "Sy Borgman's surprise party"],
    order=61,
    folder=REBIRTH,
    tag="event",
    sticky=2,
    description="Harley Quinn vol. 3 #22–34: her parents' visit, Harley Sinn's return, the mayoral race, and DePerto's murder of Mason Macabre.",
    content="""
    [Harley Quinn vol. 3 #22–34 (2017–2018)]
    • #22–24, "The Family Circles": her parents Nick and Sharon visit. Dad is critical until the drinks come out. Harley Sinn ambushes her and proposes they join forces against the Mayor; Harley knocks her out and leaves her with the Macabres. At dinner on the cruise ship Moonlighter (with Goat Boy), Sportsmaster and Clock King rob the passengers. Harley attacks with a dessert cart. Nick pulls an illegal gun to force Sportsmaster to free his daughter, and Sharon tosses mercenaries overboard, then makes Harley rescue them. Harley plants the gun on Sportsmaster, is hailed on Channel 3 news, and gets her dessert tray. Her parents say they love her and are proud of her; Harley cries. Madison Berkowitz hires the assassin squad "Unconquerable 25".
    • #25–27, "Surprise, Surprise": Sy Borgman's surprise party, and more.
    • #28–31, "Vote Harley": sick of Mayor DePerto's corruption, Harley runs for Mayor of New York City. She accepts campaign cash from Gotham villains like the Penguin, which horrifies her friends. To stop her, DePerto kidnaps Mason Macabre and extorts her into dropping out. Harley, Harley Sinn, Red Tool and Ivy try to rescue him on Fire Island, but DePerto shoots Mason in the head in front of them (#31).
    • #32: Harley takes revenge on DePerto. #33–34 close Conner & Palmiotti's five-year, 64-issue run.
    Emotional impact: Mason's murder is a lasting grief. She blames herself and becomes more protective and isolated in the arcs that follow.
    """,
)

book.entry(
    "Angry Bird & the Paranoid Spiral (2018)",
    ["Angry Bird", "Penguin", "Oswald Cobblepot", "Man-Bat", "Man-Bat serum", "Man-Batter Up",
     "pushed her friends away", "Old Lady Harley tie-in"],
    order=62,
    folder=REBIRTH,
    tag="event",
    sticky=2,
    description="Harley Quinn vol. 3 #35–44 (Tieri, Sebela): Man-Bat serum, the Penguin's invasion of Coney Island, betrayal, paranoia.",
    content="""
    [Harley Quinn vol. 3 #35–44 (2018), by Frank Tieri, then Christopher Sebela]
    • "Man-Batter Up" (#35–36): someone is targeting Harley's friends and she guesses wrong about who. Juiced on Man-Bat serum, she gets scary angry.
    • "Angry Bird" (#37–41): the Penguin, tired of a bat-infested Gotham, moves to make Coney Island his new nest and wages a cold-then-hot war on Harley. After Mason's death she refuses to put friends in harm's way and pushes them away, while they keep trying to help anyway. Betrayed by one of her last underworld allies from Gotham, she is cornered, which is where she is most dangerous. "Someone's gonna get killed here, and it ain't Harley."
    • #42 ties into Old Lady Harley (a possible future; see Adaptations lorebook).
    • #43–44 (Sebela): in a paranoid spiral, with her friends pushed away, someone blows up her favorite bodega, and the bomb was meant for her.
    """,
)

book.entry(
    "Humphries I — Apokolips, Clown for Hire, Destroying Continuity (2018–2019)",
    ["Apokolips", "Female Furies", "Female Fury", "Granny Goodness", "Lashina", "Bernadeth", "Petite Tina",
     "Tina of Apokolips", "Hammer Harleen", "Badhnisia", "Subjukator", "Lowlies", "Clown for Hire",
     "Lord Death Man", "Cap'n Crook", "Hidden Treasures", "Mr. Lennick", "Jonni DC", "Continuity Cop",
     "Meredith Clatterbuck", "Clatterbuck", "destroyed DC continuity", "Captain Triumph", "Minor Disaster",
     "Major Disaster", "Disaster Dial", "Coney Island volcano", "Pettergate", "Monsieur Katz"],
    order=63,
    folder=REBIRTH,
    tag="event",
    sticky=2,
    description="Harley Quinn vol. 3 #45–56 (Humphries): Female Fury on Apokolips, Petite Tina, Lord Death Man, the Continuity Cop, Captain Triumph, Minor Disaster.",
    content="""
    [Harley Quinn vol. 3 #45–56 (2018–2019), by Sam Humphries]
    • "Harley vs. Apokolips" (#45–47): on vacation in Badhnisia, Harley is abducted by Lashina and Bernadeth. Granny Goodness bakes her cookies and makes her a Female Fury: "Hammer Harleen", with an Apokoliptian hammer (flight, boom tubes, a built-in Granny Box). Sent to hunt the runaway Fury Petite Tina (a horned giantess), Harley instead sends the enslaved Lowlies to Badhnisia. Granny calls her "exercising free will" the ultimate crime. Put in the Psycho Crusher, Harley won't break: "There ain't nothin' I love more than seein' a grade-A jerkface like you so furious!" With Tina she beats Granny, scatters the Subjukator's power source across the universe, and boom-tubes everyone to the beach for mai tais. Tina moves to Coney Island as "Tina of Apokolips".
    • "Clown for Hire" (#48–49): developer Mr. Lennick tries to seize Harley's secret HQ for unpaid mortgage while Coach chains herself to the door. Harley fails at a dozen jobs (fast food, party clown, Daily Planet intern, cabbie, skywriter) before taking Cap'n Crook's $1 million bounty on the unkillable Lord Death Man. She kills him over and over; the patron was Lord Death Man himself, who has fallen in love with her.
    • #50, "Harley Quinn Destroys DC Continuity": Harley and her mom read fan cartoonist Meredith Clatterbuck's "Harley Quinn #50" about themselves reading it, and the infinite regression breaks reality and erases Sharon. With Continuity Cop Jonni DC (and her "bestie" the Anti-Monitor) Harley redraws the world and gets her mother back.
    • #51–52: displaced Golden Age hero Captain Triumph. #53–54: Minor Disaster (Penny, Major Disaster's daughter) humiliates social-media-star Harley with her Disaster Dial. Harley talks her out of chasing a worthless father's approval, and Penny plugs a whirlpool by creating a Coney Island volcano.
    • #56, "Pettergate": Harley rehomes a thief's cats despite her allergy. Catwoman takes one.
    """,
)

book.entry(
    "Humphries II — Mom's Cancer, the Trials & Sharon's Death (2019–2020)",
    ["mom has cancer", "mother's cancer", "Sharon's death", "her mom died", "mother died", "Christmas reveal",
     "Mirand'r", "Angel of Retribution", "Lords of Order and Chaos", "Challenge Belt", "Three Fates",
     "cockroach", "Hunted by the Bat", "Dr. Regelmann", "Smylex", "Year of the Villain", "Apex Lex",
     "Lex Luthor's offer", "The Offer", "Castaway Quinn", "Harley-er Quinn", "Hambezzler",
     "Villain of the Year", "Death himself"],
    order=64,
    folder=REBIRTH,
    tag="event",
    sticky=2,
    description="Harley Quinn vol. 3 #55–69: Sharon's cancer, the cosmic Trials of Harley Quinn, Batman's accusation, her mother's death, grief.",
    content="""
    [Harley Quinn vol. 3 #55–69 (2019–2020)]
    • #55, Christmas: her whole family descends on Coney Island and destroys dinner, the furniture and the tree (Ezzie sets it on fire). Ezzie blurts out why they came: Sharon has lung cancer. Harley storms out, comes back to a restored apartment and friends (Catwoman, Meredith Clatterbuck, Jonni DC), and Sharon moves in with her. Mirand'r, a stumbling cosmic herald, lands in the Coney Island volcano.
    • "The Trials of Harley Quinn" (#57–66): the Lords of Order and Chaos choose Harley as candidate for the Galactic Angel of Retribution, if she passes six tests while her mother is in and out of the hospital.
      – "Hunted by the Bat": framed with Smylex for supposedly murdering chemicals dealer Dr. Regelmann. Batman calls her irredeemable and it shatters her. She cuffs herself to him to solve it. It was Lord Death Man. Batman admits, "Maybe you have changed."
      – The Three Fates turn her into a giant cockroach; she breaks the curse by not caring what the crowd thinks.
      – She breaks into S.T.A.R. Labs for "fancy cancer-fighting stuff", finds an imprisoned extra-dimensional creature, listens to it, and sends it home.
      – She laughs in Death's face (#63).
    • #64, "The Offer": in Year of the Villain, "Apex" Lex Luthor pesters Harley to join his side, finally offering to cure Sharon's cancer. Before she can answer, Sharon dies, surrounded by family and friends.
    • #65–66: Harley drowns her sorrows and becomes a castaway on the volcano. The final trial was courage in grief. Made the Angel of Retribution, she uses the flaming sword to try to kill the Lords for her mother's death. Over tea they explain they didn't cause the cancer. She bargains, then accepts. Sharon's spirit says goodbye: "Your grief... you can get better at it." Harley quits and hands the title to Mirand'r.
    • #67–69 and Villain of the Year: a "Harley-er Quinn" wages war on Year of the Villain itself. Her ex-con accountant "the Hambezzler" brings his old crew to Coney Island.
    """,
)

book.entry(
    "Hollywood or Die, Joker War & Harley's Break with Coney (2020)",
    ["Hollywood or Die", "underground wrestling", "Booster Gold", "Joker War", "Punchline", "Alexis Kaye",
     "Their Dark Designs", "Underbroker", "Eden", "Clownhunter", "throat cut", "cut her throat",
     "the Designer", "roast of Harley Quinn"],
    order=65,
    folder=REBIRTH,
    tag="event",
    sticky=2,
    description="Harley Quinn vol. 3 #70–75 and Batman #86–100: L.A. wrestling, Booster Gold, the Joker War, Punchline, Eden.",
    content="""
    [Harley Quinn vol. 3 #70–75 and Batman vol. 3 #86–100 (2020)]
    • "Hollywood or Die" (#70–75): still grieving, Harley goes to Los Angeles and joins an underground wrestling troupe. When a new friend dies she suspects foul play and investigates, with Booster Gold insisting on being her crime-fighting partner. Clatterbuck's comics had already imagined the two of them on a Ferris-wheel date. It culminates in a star-studded "Roast of Harley Quinn". The series ends as she meets Punchline face to face.
    • "Their Dark Designs" (Batman #86–94): Harley partners with Catwoman to dig into the Designer's plot. Working for the Joker, his new protégée Punchline (Alexis Kaye), an intense true-believer who is Harley's opposite, cuts Harley's throat and orders her body dumped in the river. Harley survives.
    • "The Joker War" (Batman #95–100): the Joker seizes the Wayne fortune and floods Gotham with clowns. Poison Ivy had built Eden, a secret forest under Gotham, as a refuge for Harley, and Harley shelters Batman there. When Punchline tries to torch it, Harley hits her with a flamethrower. She tells her the Joker is nothing but a manipulator, that Punchline is just his latest victim, and that all he cares about is Batman. The concoction Harley gave Batman lets him shake off Punchline's drug and beat her.
    • Aftermath: Harley decides to stay in Gotham and atone. Her Coney Island era ends (Big Tony, Coach, Tina and the crew remain her friends).
    """,
)

book.entry(
    "Suicide Squad Rebirth, Heroes in Crisis & the Ivy Mini (2016–2020)",
    ["Suicide Squad Rebirth", "Rick Flag", "Katana", "Justice League vs. Suicide Squad", "Max Lord", "Task Force X",
     "Heroes in Crisis", "Sanctuary", "Booster Gold", "Wally West", "Ivy died", "Ivy regrew", "Harley Quinn and Poison Ivy",
     "Jody Houser", "Tom Taylor", "Bad Blood"],
    order=66,
    folder=REBIRTH,
    tag="event",
    sticky=2,
    description="Harley on the Rebirth Suicide Squad, the Sanctuary massacre in Heroes in Crisis, and the 2019 Harley & Ivy road-trip mini.",
    content="""
    [Team books and events, Rebirth era]
    • Suicide Squad (Rob Williams, 2016–2019): Harley is a core Task Force X member under Rick Flag, alongside Deadshot, Captain Boomerang, Katana, Killer Croc and Enchantress. She is the Squad's volatile heart: the one who hugs, jokes and shoots first. Crossovers include Justice League vs. Suicide Squad (Max Lord). Tom Taylor's Suicide Squad (2019–2020, "Bad Blood") keeps her in the mix.
    • Heroes in Crisis (2018–2019): Harley sneaks into Sanctuary, the secret superhero trauma center, to stay with Ivy, who is a patient there and urges Harley to get help with her Joker trauma too. An explosion kills most residents, including Ivy. Only Harley and Booster Gold survive, and each suspects the other. Harley ambushes Booster at dinner, then fights and beats him (Batgirl helps her clear her name), but spares him. They team up with Blue Beetle and discover the truth: Wally West lost control of the Speed Force, then faked his death with a time-displaced corpse. Ivy's plant physiology lets her regrow.
    • Harley Quinn & Poison Ivy (Jody Houser, 2019–2020): Ivy comes back from death changed, with unstable powers. Harley stands by her through a road-trip story that deepens their bond as partners.
    """,
)

# ─────────────────────────────── INFINITE FRONTIER / DAWN ───────────────────────────────

book.entry(
    "No Good Deed & Keepsake — Back in Gotham (2021–2022)",
    ["No Good Deed", "Hugo Strange", "S.A.F.E.", "kidnapped clowns", "Keepsake", "Eli Kaufmann", "Fear State",
     "the Gardener", "Bella Garten", "two Ivies", "split Ivy", "Queen Ivy", "Urban Legends",
     "make up for the sins"],
    order=67,
    folder=IF,
    tag="event",
    sticky=2,
    description="Harley Quinn vol. 4 #1–12 (Phillips/Rossmo): back in Gotham to atone, Kevin, Hugo Strange's clown hunt, Keepsake, and Fear State.",
    content="""
    [Harley Quinn vol. 4 #1–12 (2021–2022), by Stephanie Phillips & Riley Rossmo]
    • Premise: after the Joker War, Harley returns to Gotham "to make up for the sins of my past" and help the city recover, especially from the damage done by the Joker, whom she enabled for years. There is no welcoming committee. Batman is wary, the GCPD hostile, and the public skeptical. New Rossmo costume, baseball bat in hand.
    • Kevin: a sweet, big-hearted former Joker henchman on his own redemption arc, and Harley's new best friend and sidekick. He later adopts a costume modeled on hers and has his own romance subplot.
    • Hugo Strange, working out of S.A.F.E. headquarters, runs a sinister program rounding up the Joker's former clowns, complete with out-of-control orderlies. Harley investigates the kidnappings and exposes him. The site becomes the planned Arkham Tower, an open-to-the-public mental-health facility.
    • Keepsake (Eli Kaufmann): an ex-Joker Gang member who is obsessed with Harley and went the other way. He builds an army (freeze rays, weaponized umbrellas, flamethrowers) and embodies the fear that not every villain can grow better. Kevin fears becoming him. Keepsake dies in #12.
    • "Fear State" tie-in: Ivy has split into two versions. Harley, with Kevin and Ivy's ex-girlfriend the Gardener (Bella Garten, who has little plant dogs), fights to reunite Ivy's selves. Around this time Harley and Ivy go through a painful separation while Ivy leans back toward eco-villainy; they later reconcile.
    """,
)

book.entry(
    "Verdict, Task Force XX & Who Killed Harley Quinn? (2022–2023)",
    ["Verdict", "put on trial", "Arkham Tower", "back to being a psychologist", "Task Force XX", "Luke Fox",
     "Batwing", "moon base", "JLA moon base", "Killer Frost", "Bronze Tiger", "Solomon Grundy",
     "Who Killed Harley Quinn", "multiverse Harleys", "fifty Harleys", "mermaid Harley", "Harley died",
     "dead Harley"],
    order=68,
    folder=IF,
    tag="event",
    sticky=2,
    description="Harley Quinn vol. 4 #13–27: psychologist again, framed and tried, the vigilante Verdict, Task Force XX on the moon, and the multiversal Harley murders.",
    content="""
    [Harley Quinn vol. 4 #13–27 (2022–2023)]
    • "Verdict" (#13–17): Harley resumes her career as a psychologist, tied to the new Arkham Tower. Issue #15 settles that she holds a PhD in psychology and quotes the Joker's contempt for it. She is dragged into court and nearly jailed for something she didn't do. With Batwoman's help she unmasks the violent vigilante Verdict, whose "origin" is a string of bad days, some caused by Harley herself.
    • "Task Force XX" (#18–21, the 2022 Annual, Shadow War Zone #1): Luke Fox (Batwing) sends a team of reformed villains to clean up a dangerous leftover experiment in the old JLA moon base. The team includes Harley, Killer Frost, Bronze Tiger and Solomon Grundy. Batwing's file notes her doctorate and her "hundreds of clinical hours" with Gotham's criminally insane.
    • "Who Killed Harley Quinn?" (#22–27): Harley is killed ("bein' dead is just like ridin' a bike"). Fifty Harleys from across the Multiverse gather while an interdimensional murderer hunts every Harley. Our Harley gets an existential crisis from meeting herself 49 times and is jealous of Mermaid Harley. Kevin and two hungry hyenas help. The Harley Quinn 30th Anniversary Special celebrates her history.
    """,
)

book.entry(
    "Tini Howard Era — Professor Quinn, Girl in a Crisis, Brother Eye (2023–2024)",
    ["Girl in a Crisis", "Lady Quark", "Earth-48", "Earth 48", "cartoon fish", "Vorpal Fish", "Captain Carrot",
     "Zoo Crew", "Earth-26", "Cosmic Treadmill", "multiversal hyenas", "Gotham City Community College",
     "community service", "Abnormal Psych", "Knight Terrors", "Eye Don't Like Me", "Brother Eye", "OMAC",
     "OMACs", "Clown About Town", "In-Continuity Dreams", "Lovely Angels", "Zatanna warding spell"],
    order=69,
    folder=IF,
    tag="event",
    sticky=2,
    description="Harley Quinn vol. 4 #28–43 (Tini Howard): community-service professor, multiverse crisis with Lady Quark, talking hyenas, Brother Eye.",
    content="""
    [Harley Quinn vol. 4 #28–43 (2023–2024), by Tini Howard & Sweeney Boo, with "In-Continuity Dreams" backups]
    • Status: Harley lives with Poison Ivy in their Gotham home. Ivy is often away, for example on a road trip. Harley and Kevin still hang out.
    • #28: Harley ruins Two-Face's bank robbery at the Amusement Mile carnival and steals his shoe, which rattles him. A breakfast with Kevin turns out to be a setup, and she is arrested and sentenced to community service as a professor of Abnormal Psychology at Gotham City Community College. Two-Face drives into her classroom on day one.
    • "Girl in a Crisis": during the fight she somehow grabs a cartoon fish from another reality, the Vorpal Fish. Lady Quark of Earth-48 warns that using objects from other universes risks a crisis that will destroy her Earth. Zatanna gives her a multiverse ward that needs a meaningful sacrifice. Batman advises her to sacrifice something she doesn't want to, so she destroys a plant Ivy asked her to tend, which devastates Ivy when she finds out. Bud and Lou start talking telepathically: they are projections of their Earth-48 counterparts and her "multiverse guides". She rides a cosmic treadmill to Earth-26 to return the fish to Captain Carrot's Zoo Crew (most of whom Backseid killed without it), eats a Cosmic Carrot to save a student, and is spared by Lady Quark because of a call from Batman: "she has a higher purpose."
    • Knight Terrors: Harley Quinn #1–2, her nightmare-realm tie-in.
    • "Eye Don't Like Me" (#32–37): fighting for her life against Brother Eye and his O.M.A.C.s; "Harley the Barbarian" dream backups.
    • "Clown About Town" (#38–43): Harley flirts with villainy again ("There ain't nothin' like villainy!"), dealing with Gotham's rogues. Backup dreams parody anime (Lovely Angel Harley with Catwoman and Ivy; Evangelion), fantasy quests (kissing Ivy awake), and more.
    """,
)

# ─────────────────────────────── ALL IN / PRESENT ───────────────────────────────

book.entry(
    "Throatcutter Hill & Destructive Comics (2024–2025)",
    ["Throatcutter Hill", "gentrification", "gentrified", "destructive agency", "destructive agent", "Destructive Comics",
     "Althea Klang", "Klang", "Chicken Fingers", "Chester Figueroa", "Refuse Men", "smoothie", "Raymond Chandler"],
    order=70,
    folder=ALLIN,
    tag="event",
    sticky=2,
    description="Harley Quinn vol. 4 #44–49 (Elliott Kalan & Mindy Lee): saving Throatcutter Hill from gentrification; Althea Klang; Chicken Fingers.",
    content="""
    [Harley Quinn vol. 4 #44–49 (late 2024–2025), by Elliott Kalan & Mindy Lee, DC All In]
    • Harley's favorite dangerous neighborhood in Gotham, Throatcutter Hill, has been gentrified beyond recognition: boutique smoothie bars, luxury condos, dead character. She "breaks bad" on a one-clown mission to make Gotham safe for crime again. In practice she protects the neighborhood's people and its grime from being bulldozed.
    • She opens a "destructive agency", a detective-agency parody narrated like a Raymond Chandler novel.
    • Althea Klang: a butch supervillain real-estate mogul and the architect of the gentrification. She and Harley develop a flirty love-hate rivalry. In #48 Harley admits her crush to Ivy, who answers: "Do what you need to do. Fight her, sleep with her... just don't fall in love with her, okay?"
    • Chicken Fingers (Chester Figueroa): a homeless local vigilante and Throatcutter Hill's self-appointed protector, and Harley's scruffy sidekick and friend. She buys them both overpriced smoothies, then destroys the smoothie shop. His origin: he convinced locals he didn't belong in an institution by saving them from the Refuse Men, a sanitation-worker mob.
    """,
)

book.entry(
    "Friends with Detriments, DC K.O., Batquinn & the Ivy Breakup (2025–2026)",
    ["Friends with Detriments", "DC K.O.", "K.O. tournament", "Zatanna fight", "alpha energy", "omega energy",
     "split into two", "Batquinn", "Harq Knight", "Silent Sentinel", "Penny Plunderer", "Mayor Ivy", "Ivy is mayor",
     "Ivy became mayor", "broke up with Ivy", "breakup with Ivy", "Poison Ivy #43", "Bad Seeds", "date with Klang",
     "date to the death", "Justice League Unlimited", "JLU", "We Are Yesterday"],
    order=71,
    folder=ALLIN,
    tag="event",
    sticky=2,
    description="Harley Quinn vol. 4 #50–62 and events: DC K.O., alpha/omega energy, Chicken Fingers' powers, Ivy's election and their breakup, Batquinn, dating Klang.",
    content="""
    [2025–2026: Harley Quinn vol. 4 #50–62, DC K.O., Poison Ivy #42–43, Justice League Unlimited]
    • "Friends with Detriments" (#50–57, art by Carlos Olivares): the Throatcutter Hill saga continues. Harley juggles her feud-flirtation with Althea Klang, her friendship with Chicken Fingers, and her relationship with Ivy.
    • DC K.O. (2025–26): a cosmic fighting tournament. Harley faces Zatanna: she wins round one with a throat punch, loses round two to a hard punch to the face, copies Zatanna's magic in round three, and still loses. Afterwards all the fighters carry alpha and omega energy. In Harley it split her into two beings until the energy was absorbed by Chicken Fingers, who is now superpowered, an optimistic Superman-style counterpart to Harley.
    • Justice League Unlimited (vol. 2, 2024–): Harley is loosely affiliated with the sprawling new JLU and appears in its "We Are Yesterday" time-travel story.
    • The Ivy breakup: in Poison Ivy (G. Willow Wilson) Ivy wins election as Mayor of Gotham. In Poison Ivy #43 (2026) she tells Harley she can't allow anything to put the job at risk, meaning Harley's unpredictability at televised events. It isn't that being mayor matters more than Harley; she needs the job. Harley walks out of the mayor's office and the relationship ends. Both are heartbroken. Ivy's rule leads into the "Bad Seeds" crisis, with the Bat-Family hunted as outlaws and Gotham threatened with a primeval plant apocalypse.
    • Rebound and reinvention: Harley and Althea Klang go on a first date "to the death" (#59). In #60 Harley dons a homemade cape and cowl as the brooding "Batquinn", the "Harq Knight", a Silent Sentinel of Throatcutter Hill parodying The Dark Knight Returns, while Chicken Fingers plays the hopeful hero and the Penny Plunderer causes trouble.
    """,
)

book.entry(
    "Current Status Snapshot (present day, 2026)",
    ["current status", "where does Harley live", "where she lives", "what is Harley doing", "present day",
     "status quo"],
    order=35,
    folder=ALLIN,
    tag="lore",
    sticky=2,
    description="One-glance summary of Harley's present-day canon situation, for grounding a modern-set chat.",
    content="""
    [Harley Quinn — Where Things Stand (Prime Earth, 2026)]
    • Home base: Gotham City, around Throatcutter Hill, the grimy neighborhood she has adopted and defends from gentrification. She works as a freelance "destructive agent" and occasional costumed vigilante (lately the self-serious "Batquinn").
    • Love life: freshly broken up with Poison Ivy, who is now Mayor of Gotham and ended it over the optics of dating Harley. It is raw. Harley is dating, fighting and flirting with Althea Klang, the real-estate supervillain behind the gentrification.
    • Friends and allies: Chicken Fingers (superpowered since DC K.O.), Kevin (ex-Joker henchman and her loyal pal), Catwoman, the Bat-Family (a wary alliance; Batman grudgingly believes she has changed), Zatanna, and her Coney Island family (Big Tony, Coach, Tina of Apokolips and the rest) from afar. Bud and Lou are with her; Bernie is always with her.
    • Family: mother Sharon died of cancer (2019). Father Nick and brothers Barry, Frankie and Ezzie live in Florida.
    • The Joker: long over. She actively opposes him and his imitators (e.g., Punchline).
    • Career: PhD psychologist with a record as both an Arkham doctor and an inmate. She still does therapy informally with everyone she meets.
    If the user sets the chat in another era (the Coney Island landlady years, the Suicide Squad, the classic Joker days), use that era's entry instead.
    """,
)
