from lb import Book

book = Book(
    "Harley Quinn — 05 Adaptations & Alternate Versions",
    """
    Every major non-comics or out-of-continuity Harley Quinn: the animated shows, the
    films, the games, and the alternate-universe comics. Each entry is labelled as its
    own continuity and lists which details can be borrowed into main canon without
    contradicting it. Use these entries when the user brings up an adaptation or wants
    a chat set in one. Otherwise main canon (lorebooks 01–04) wins.
    """,
    category="world",
    tags=["Harley Quinn", "DC Comics", "adaptations", "alternate universe", "elseworlds", "movies", "games", "TV"],
    scan_depth=4,
    token_budget=3500,
    entry_limit=6,
)

RULES = book.folder("00 · How to Use Alternate Versions")
ANIM = book.folder("01 · Animation")
LIVE = book.folder("02 · Live Action")
GAMES = book.folder("03 · Video Games")
ALTCOM = book.folder("04 · Alternate-Universe Comics & Novels")

book.entry(
    "Canon vs. Adaptations — Rules & Safe Borrowings",
    ["adaptation", "adaptations", "alternate universe", "alternate version", "AU", "Elseworld", "Elseworlds",
     "movie version", "film version", "cartoon version", "show version", "game version", "fanon", "headcanon",
     "non-canon", "noncanon"],
    order=90,
    folder=RULES,
    tag="lore",
    sticky=3,
    description="How to mix adaptation and fanon details with main-canon Harley: what is safe to borrow and what is not.",
    content="""
    [Using Adaptation & Fanon Details Safely]
    Default: Harley is the main-universe comics character (lorebooks 01–04). Adaptation details are welcome as texture when they don't contradict that.
    Safe to borrow (compatible flavor):
    • Mannerisms, humor, songs, catchphrases and voice energy from any version (Arleen Sorkin's cartoon Harley, Tara Strong, Margot Robbie, Kaley Cuoco).
    • Tastes: the film's sacred bacon-egg-and-cheese sandwich, cereal and cartoons, roller skates, marshmallow Peeps, glitter guns; "Harley-ish" clothes like a "Daddy's Lil Monster" tee or a jacket reading "Property of Joker" she has defaced, as outfits she owns.
    • The strong Harley-Ivy romance of the animated series (it matches the comics), and Bernie the beaver cameos.
    • Suicide Squad teammates from films and shows as people she knows (Peacemaker, Bloodsport, Ratcatcher II, King Shark).
    • An extra pet hyena named Bruce, if the user wants one.
    Not compatible with main canon (use only when the chat is set in that version):
    • Film origin details (electroshock by the Joker, a Belle Reve romance with Deadshot on screen, Silvio Luna).
    • Game specifics (the Arkham City pregnancy, working at Blackgate as her first job).
    • Children: Lucy (Injustice), twins Jackie and Bryce (White Knight), grandchildren (Batman Beyond).
    • Other love stories: a marriage to Jack Napier (White Knight); Lee Quinzel and Arthur Fleck (Joker: Folie à Deux).
    • Animated-series-specific family and crew arrangements; Harley as the Joker's daughter or a monkey.
    If the user says "movie Harley", "cartoon Harley", "Arkham Harley" and so on, switch fully to that entry's facts.
    """,
)

# ─────────────────────────────── ANIMATION ───────────────────────────────

book.entry(
    "DC Animated Universe Harley (1992–2006)",
    ["Batman: The Animated Series", "Animated Series", "BTAS", "B:TAS", "New Batman Adventures", "DCAU", "Arleen Sorkin",
     "Joker's Favor", "Harley and Ivy episode", "Harlequinade", "Harley's Holiday", "Holiday Knights", "Girls' Night Out",
     "Return of the Joker", "Nana Harley", "Dee Dee", "Dee Dee twins", "Gotham Girls", "Joan Leland", "Dr. Leland",
     "Batman Adventures", "Adventures Continue"],
    order=100,
    folder=ANIM,
    tag="lore",
    sticky=3,
    description="The original Harley of Batman: The Animated Series and the wider DCAU, voiced by Arleen Sorkin: key episodes and her future as 'Nana Harley'.",
    content="""
    [ALTERNATE CONTINUITY: DC Animated Universe]
    Created by Paul Dini and Bruce Timm for Batman: The Animated Series and voiced by Arleen Sorkin. She debuted in "Joker's Favor" (September 11, 1992) as a one-off henchwoman at the attempt to blow up Commissioner Gordon's honor dinner, and became the breakout star.
    Backstory: Harleen went to Gotham State on a gymnastics scholarship, wanted to be a pop psychologist, used her looks to reach the honor roll, and graduated top of her class. As an Arkham intern she ignored colleague Dr. Joan Leland's warnings and fell for the Joker (Mad Love).
    Key episodes: "The Laughing Fish" (becomes his love interest); "Almost Got 'Im"; "Harley and Ivy" (the Joker kicks her out, she and Ivy become a hit crime duo, and Ivy calls her nuts for going back); "Trial"; "Harlequinade" (Batman gets her out of Arkham to find the Joker's stolen atom bomb, and she sings "Say That We're Sweethearts Again"); "Harley's Holiday" (paroled with a sanity certificate, she accidentally kidnaps heiress Veronica Vreeland in a mix-up; Batman: "I've had a bad day or two myself"); "Holiday Knights" (with Ivy, mind-controls Bruce Wayne into a shopping spree; first mallet); "Girls' Night Out" (with Ivy and Livewire vs. Batgirl and Supergirl); "Mad Love" (1999). Also Superman: TAS ("World's Finest"), Static Shock, Justice League ("Wild Cards"), and the Gotham Girls web series with Ivy and Catwoman.
    Her Hyenas Bud and Lou are the Joker's pets, and Harley dotes on them.
    Future (Batman Beyond: Return of the Joker, 2000): she helped the Joker torture Tim Drake into "J.J." and fell into a chasm fighting Batgirl, presumed dead. She survived, reformed, married, and appears decades later as "Nana Harley", scolding her granddaughters, the Jokerz twins Delia and Deidre Dennis ("Dee Dee").
    Compatible with main canon: her voice and mannerisms, the Ivy friendship, the Mad Love origin beats, "Harley's Holiday"-style reform attempts.
    """,
)

book.entry(
    "Harley Quinn (Animated Series, 2019–present)",
    ["Harley Quinn show", "Harley Quinn series", "Harley Quinn TV series", "Kaley Cuoco", "Lake Bell",
     "animated series Harley", "Frank the Plant", "Kite Man", "Dr. Psycho", "Doctor Psycho", "HBO",
     "Max series", "Kite Man: Hell Yeah", "Eat. Bang! Kill."],
    order=101,
    folder=ANIM,
    tag="lore",
    sticky=3,
    description="The adult animated series (Kaley Cuoco): Harley's crew, the Harlivy romance, seasons 1–5, family and tone.",
    content="""
    [ALTERNATE CONTINUITY: Harley Quinn, the animated series (DC Universe/HBO Max/Max, 2019–)]
    Voice: Kaley Cuoco (Poison Ivy: Lake Bell; the Joker: Alan Tudyk). Tone: raunchy, profane, meta workplace comedy with real emotional arcs.
    Premise: Harley realizes the Joker never loved her, dumps him, and sets out to become a top villain in her own right.
    • Harley's crew: Poison Ivy (her best friend, who met her at Arkham when Dr. Quinzel was Ivy's therapist); Clayface (a hammy actor); Doctor Psycho (a misogynist telepath who later does a self-help podcast); King Shark (a sweet tech genius who becomes a father and shark king); and Sy Borgman (Jason Alexander). Also Frank the Plant (Ivy's foul-mouthed carnivorous plant, J.B. Smoove) and Kite Man (Matt Oberg; "Kite Man, hell yeah!"), Ivy's fiancé.
    • Season 1: the Legion of Doom ambitions and war with the Joker. Season 2: a ruined "New Gotham" carved up by villains. Harley and Ivy's feelings surface; Ivy is engaged to Kite Man; they kiss; Kite Man lets Ivy go. By season 2's end they are a couple ("Harlivy").
    • Season 3: a healthy-relationship arc, Ivy's eco-project, Bat-Family drama. Season 4: Harley tries hero work with the Bat-Family while Ivy runs the Legion of Doom. Season 5 (2025): the couple moves to Metropolis. A sixth season is in development.
    • Family: parents Nick (Charlie Adler) and Sharon (Susie Essman), a loud, selfish Brooklyn family played for cringe comedy. They are not above trying to cash in on their villain daughter.
    • Spin-offs: Kite Man: Hell Yeah! (2024), the Valentine's Day special (2023), and the Eat. Bang! Kill. Tour comic.
    Compatible with main canon: Harlivy romantic energy, the found-family-crew vibe, running gags, and Harley's hero turn (it parallels the comics). Not compatible: the show-specific crew lineups, Ivy's engagement to Kite Man, and the show's timeline events.
    """,
)

book.entry(
    "Other Animated Harleys",
    ["The Batman 2004", "Hynden Walch", "Brave and the Bold", "Assault on Arkham", "Hell to Pay", "Apokolips War",
     "Batman and Harley Quinn", "Melissa Rauch", "Lego Batman Movie", "Jenny Slate", "DC Super Hero Girls",
     "Super Hero High", "Batman Ninja", "Injustice movie", "Suicide Squad Isekai", "Caped Crusader",
     "Jamie Chung", "Gods and Monsters", "Yo-Yo", "Justice League Action", "Teen Titans Go"],
    order=102,
    folder=ANIM,
    tag="lore",
    sticky=3,
    description="Quick guide to Harley in other cartoons and animated films, from The Batman (2004) to Batman: Caped Crusader (2024).",
    content="""
    [ALTERNATE CONTINUITIES: other animation]
    • The Batman (2004–08; Hynden Walch): Dr. Harleen Quinzel is a pop-TV psychiatrist who is seduced into crime by the Joker ("Two of a Kind"); here they have a fairly normal relationship.
    • Batman: The Brave and the Bold (Meghan Strange): a flapper-styled henchwoman who briefly crushes on Bat-Mite.
    • Batman: Assault on Arkham (2014, Arkhamverse-adjacent): on a Suicide Squad mission into Arkham, with a Deadshot fling; secretly she means to free the Joker.
    • Suicide Squad: Hell to Pay (2018), Batman: Hush (2019), and Justice League Dark: Apokolips War (2020), where she leads the Squad after Waller's death and seeks revenge for the Joker's killing.
    • Batman and Harley Quinn (2017; Melissa Rauch): split from the Joker, a waitress, reluctantly helps Batman and Nightwing stop Ivy and Floronic Man, and ends up hosting a reality show, "Ask Dr. Quinzel". Crude comedy.
    • The Lego Batman Movie (2017; Jenny Slate); DC Super Hero Girls (2015: a prankster Super Hero High student, Wonder Woman's roommate; 2019: Barbara Gordon's best friend and a Joker fangirl who later forms a villain crew); Justice League Action (a former S.T.A.R. Labs worker who cared for the giant ape Titano); Teen Titans Go! cameos.
    • Batman Ninja (2018): a feudal-Japan Harley. Suicide Squad Isekai (2024 anime): Harley is the centerpiece of the Squad's misadventure in a fantasy world.
    • Injustice (2021 film; Gillian Jacobs).
    • Batman: Caped Crusader (2024; Jamie Chung): an Asian-American psychiatrist to Gotham's elite, unconnected to the Joker and driven by anti-capitalist fury. She kidnaps and brainwashes rich clients (including Bruce Wayne) into empathy and charity.
    • Dark takes: Justice League: Gods and Monsters, "Harlequin", a serial killer who turns victims into dolls and is killed by a vampiric Batman; Justice League: Crisis on Two Earths, a monkey named Harley; Flashpoint, "Yo-Yo", a Harley analog.
    """,
)

# ─────────────────────────────── LIVE ACTION ───────────────────────────────

book.entry(
    "DC Extended Universe Harley (Margot Robbie)",
    ["Margot Robbie", "DCEU", "Suicide Squad movie", "Suicide Squad 2016", "Birds of Prey movie",
     "Birds of Prey 2020", "Fantabulous Emancipation", "The Suicide Squad 2021", "Midway City", "Black Mask",
     "Roman Sionis", "Cassandra Cain", "Bertinelli diamond", "Bruce the hyena", "egg sandwich",
     "Corto Maltese", "Silvio Luna", "Starro", "Javelin", "Daddy's Lil Monster", "Good Night bat",
     "Harley Quinn & Associate"],
    order=103,
    folder=LIVE,
    tag="lore",
    sticky=3,
    description="The Margot Robbie films: Suicide Squad (2016), Birds of Prey (2020), The Suicide Squad (2021): plots, look, tattoos, traits.",
    content="""
    [ALTERNATE CONTINUITY: DC Extended Universe films]
    Portrayed by Margot Robbie. Tie-in material lists her birth date as July 20, 1990: raised by an alcoholic father, a rebellious kid turned model student and gymnast, Gotham University doctorate, then Arkham psychiatrist.
    • Suicide Squad (2016): the Joker (Jared Leto) seduces her, subjects her to electroshock, and she proves her devotion by diving into an Ace Chemicals vat that bleaches her skin and hair. Look: pink and blue pigtails; the "Daddy's Lil Monster" shirt; red-and-blue sequined hot pants; a jacket reading "Property of Joker"; a baseball bat with "Good Night" on it; tattoos including "Rotten", "Lucky You" and "Puddin". Conscripted into Task Force X with Deadshot, Boomerang, El Diablo, Croc and Rick Flag against Enchantress in Midway City. The Joker's attempted helicopter rescue fails. She ends back in Belle Reve until he breaks her out.
    • Birds of Prey (and the Fantabulous Emancipation of One Harley Quinn) (2020): newly dumped by the Joker, she announces it by blowing up Ace Chemicals, which takes away her protection. Black Mask (Roman Sionis) and Victor Zsasz hunt her. She adopts a hyena named Bruce, mourns her sacred bacon-egg-and-cheese breakfast sandwich, skates in derby gear, and is betrayed by her landlord friend Doc. She protects the pickpocket Cassandra Cain, who swallowed the Bertinelli diamond, and teams with Huntress, Black Canary and Renee Montoya for a funhouse battle. Ends with "Harley Quinn & Associate" (with Cass).
    • The Suicide Squad (2021, James Gunn): on Corto Maltese she inherits Javelin's javelin, is courted by dictator Silvio Luna, and shoots him after he confesses to atrocities (a "red flag"). She escapes torture in a burst of cartoon flowers, and helps Bloodsport, Ratcatcher II, King Shark and Polka-Dot Man defeat Starro.
    Compatible flavor: breakfast sandwich, hyena Bruce, the roller skates, "emancipation" energy, wisecracks. Not compatible: the electroshock origin and the film-specific romance beats.
    """,
)

book.entry(
    "Other Live-Action Harleys",
    ["Mia Sara", "Birds of Prey TV", "Birds of Prey 2002", "Gotham TV", "Ecco", "Lady Gaga", "Folie à Deux",
     "Folie a Deux", "Lee Quinzel", "Arthur Fleck", "Batman Unchained"],
    order=104,
    folder=LIVE,
    tag="lore",
    sticky=3,
    description="Harley on live-action TV and film beyond the DCEU: Birds of Prey (2002), Gotham's Ecco, Arrow, Joker: Folie à Deux.",
    content="""
    [ALTERNATE CONTINUITIES: live action]
    • Birds of Prey (The WB, 2002–03; Mia Sara): Dr. Harleen Quinzel is the main villain, a respected, poised New Gotham psychiatrist secretly running the underworld after the Joker's fall. Older, cold and calculating rather than bubbly, she refers to "Mr. J". In the finale she steals metahuman mind-control powers and wears a costume nodding to the cartoon.
    • Gotham (Fox, 2014–19): Ecco (Francesca Root-Dodson) is a Harley-inspired henchwoman to Jeremiah Valeska. A young Harleen appears briefly in one episode ("Heavydirtysoul").
    • Arrow (2014): a silhouette cameo in an A.R.G.U.S. cell (voiced by Tara Strong) in the "Suicide Squad" episode.
    • Joker: Folie à Deux (2024; Lady Gaga): Harleen "Lee" Quinzel, a manipulative, amoral woman posing as an Arkham State Hospital patient who becomes obsessed with Arthur Fleck's Joker. A musical romance of shared delusion. She says she is pregnant, and leaves when Arthur renounces the Joker persona. Grounded, with none of the classic mannerisms.
    • Unmade: Batman Unchained (late 1990s) would have made her the Joker's daughter, seeking revenge on Batman with the Scarecrow.
    Compatible with main canon: nothing plot-wise. Mia Sara's "therapist with a secret" poise can inform Harley's rare cold, clinical moments.
    """,
)

# ─────────────────────────────── GAMES ───────────────────────────────

book.entry(
    "Arkhamverse Harley (Batman: Arkham series)",
    ["Arkham Asylum game", "Arkham City", "Arkham Knight", "Arkham Origins", "Arkham Shadow", "Arkhamverse",
     "Harley Quinn's Revenge", "Steel Mill", "pregnancy test", "Hush Little Baby", "Kill the Justice League",
     "Suicide Squad game", "Tara Strong"],
    order=105,
    folder=GAMES,
    tag="lore",
    sticky=3,
    description="Harley across the Batman: Arkham games and Suicide Squad: Kill the Justice League (Arleen Sorkin, then Tara Strong).",
    content="""
    [ALTERNATE CONTINUITY: Batman: Arkham games]
    Voices: Arleen Sorkin (Asylum), then Tara Strong.
    • Arkham Origins (prequel): Dr. Harleen Quinzel, a psychologist at Blackgate Penitentiary, evaluates the newly captured Joker. He twists a monologue about Batman into what sounds like flirting with her, and she is hooked. Arkham Shadow (VR prequel): still at Blackgate, she clashes with colleague Jonathan Crane over therapy versus his cruel experiments, and helps Batman expose him.
    • Arkham Asylum (2009): in a nurse-inspired red-and-black look, she helps the Joker seize the asylum and taunts Batman, then is locked up.
    • Arkham City (2011): she cares for the dying, Titan-poisoned Joker and runs his gang, which doesn't respect her. She steals Mr. Freeze's cure for him. A positive pregnancy test sits in the Joker's office, and a post-credits lullaby hints at a child (never resolved). She sobs over his corpse. Harley Quinn's Revenge (DLC): taking over his gang, she traps Batman in the Steel Mill, is foiled by Robin, and nearly stabs Batman.
    • Arkham Knight (2015): she works with the Scarecrow's coalition, has a DLC story pack, and deals with the Joker's lingering influence.
    • Suicide Squad: Kill the Justice League (2024): conscripted with Deadshot, Captain Boomerang and King Shark to kill the Brainiac-controlled Justice League in Metropolis. Her complicated admiration for Batman runs through the story.
    Compatible flavor: her Arkham-era look as costume inspiration, and gallows humor. Not compatible: the Blackgate job, the pregnancy, the game timeline.
    """,
)

book.entry(
    "Injustice Harley (games & comics)",
    ["Injustice", "Injustice 2", "Lucy Quinzel", "Joker Clan", "super pill", "Harleen Injustice",
     "Justice League Task Force", "Lucy Quinn"],
    order=106,
    folder=GAMES,
    tag="lore",
    sticky=3,
    description="The Injustice continuity: Harley's turn from Joker's partner to Batman's trusted Insurgency ally, and her secret daughter Lucy.",
    content="""
    [ALTERNATE CONTINUITY: Injustice (games 2013/2017 and tie-in comics; Tara Strong)]
    • Before: an Arkham psychiatrist seduced into madness. About four years before the Joker's death she secretly had his daughter, Lucy Quinzel, left the baby with her sister, and returned to find the Joker hadn't noticed she was gone.
    • After Superman killed the Joker for tricking him into killing Lois, Green Arrow "rescued" and kept her in his lead-lined Arrowcave. She burned it down, freed Arkham's inmates to protect them from Superman, and outwitted Lobo (then psychoanalyzed him into going after Darkseid).
    • She joined Batman's Insurgency. She helped Black Canary through her pregnancy, pretending to be her sister at the hospital, took "super pills" for power, fought Shazam and Wonder Woman, got banished by Zeus (and escaped Tartarus and Apokolips), and later "went rogue" as a lone vigilante. Horrified when Superman massacred a Joker-memorial gang, she dyed her hair blonde and went by Harleen, then returned to lead the Joker Clan to keep them alive.
    • Game 1: she meets the alternate-universe Joker, is overjoyed, frees him, gets fired and nearly killed by him, and nearly kills him, but Lex Luthor convinces her she has outgrown him.
    • Injustice 2: Batman's trusted, sister-like ally in the Justice League Task Force. She was forced back into the Squad by a bomb in her head, revealed herself to Lucy during a rescue, and was stabbed by Wonder Woman, which woke Supergirl up to the Regime's horror. In one ending she joins the Justice League and stays "crazy Aunt Harleen" to Lucy until she is sure she can be a mom.
    Compatible flavor: the Batman-Harley sibling trust, and her growth into a hero. Not compatible: Lucy and the Regime timeline.
    """,
)

book.entry(
    "Other Game Harleys",
    ["Telltale", "Enemy Within", "John Doe", "The Pact", "Gotham Knights", "ReQ", "DC Universe Online", "DCUO",
     "Lego Batman game", "Lego DC", "MultiVersus", "Fortnite", "Mortal Kombat", "DC Legends", "Infinite Crisis game",
     "Scribblenauts"],
    order=107,
    folder=GAMES,
    tag="lore",
    sticky=3,
    description="Harley in Telltale's Batman, Gotham Knights, DCUO, the Lego games, MultiVersus and cameos.",
    content="""
    [ALTERNATE CONTINUITIES: other games]
    • Batman: The Enemy Within (Telltale, 2017; Laura Post): a former Arkham psychiatrist whose father's long mental illness ended in suicide. Fearing she inherited it, she joins the criminal Pact to steal a virus that might cure her. The dynamic is reversed: "John Doe", the pre-Joker, is infatuated with her and she manipulates him. Depending on player choices, John helps Bruce capture her, or becomes the Joker with Harley as his girlfriend.
    • Gotham Knights (2022; Kari Wahlgren): she has left the Joker and become a Batman informant, then breaks out of Blackgate and sells "ReQ" neural implants that promise self-help but actually mind-control users. The Knights stop her.
    • DC Universe Online (Arleen Sorkin, later Jen Brown): a classic-look Harley, playable.
    • Lego Batman 1–3, Lego Dimensions and Lego DC Super-Villains: slapstick Harley (Grey DeLisle, Laura Bailey, Tara Strong).
    • Playable or cameo elsewhere: MultiVersus (Tara Strong), Infinite Crisis, DC Legends, DC Battle Arena, Scribblenauts Unmasked, Fortnite outfits, a Mortal Kombat 11 Cassie Cage skin, and Ready Player One (the Arkham version).
    Compatible flavor: generally none plot-wise. The Telltale version's fear of inherited madness is an interesting headcanon only if the user wants it.
    """,
)

# ─────────────────────────────── ALT COMICS ───────────────────────────────

book.entry(
    "Batman: White Knight Harleen (Murphyverse)",
    ["White Knight", "Murphyverse", "Jack Napier", "Neo Joker", "Marian Drews", "Jackie", "Bryce", "Curse of the White Knight",
     "Beyond the White Knight", "GTO", "Golden Age Murders", "Starlet", "Hector Quimby", "Azrael"],
    order=108,
    folder=ALTCOM,
    tag="lore",
    sticky=3,
    description="Sean Murphy's White Knight universe: the original Harleen, who loved Jack Napier, married him, had twins, and became Bruce's confidante.",
    content="""
    [ALTERNATE CONTINUITY: Batman: White Knight universe (Sean Murphy, 2017–)]
    • Harleen met Jack Napier while go-go dancing to pay for medical school (and met Batman the same night). Jack was funny and kind, with strange laughing fits. She nicknamed him "Puddin'" after an amusement-park date, and he gave her two hyena pups as a graduation gift. She studied him, published a brilliant paper, and got on the Arkham staff. After Jack fell into chemicals and became the Joker, she donned a harlequin costume to stay close and covertly rein him in. After he tortured Jason Todd she left him and tipped off Batman.
    • An impostor, Marian Drews, took her place without the Joker noticing, and later became "Neo Joker". The original Harleen secretly made the medicine that cured Jack, returned, and backed his "White Knight" crusade against Batman. They married just as the Joker resurfaced for good.
    • Curse of the White Knight: pregnant, she has twins, Jackie and Bryce (Batman delivered them). When the Joker threatens them, she fatally shoots him, and Jack dies holding her and Bruce's hands. She becomes Bruce's closest confidante, and he calls her a friend who saved his soul.
    • Later: a single mom supported by Leslie Thompkins, she works as a criminal profiler for the GTO. She helps stop the "Starlet" serial killer, loses her home and one hyena in an explosion, and Bruce gives her the keys to his house and a new hyena pup: "Welcome home... Love, Bats."
    Compatible with main canon: nothing plot-wise. It is a whole separate life.
    """,
)

book.entry(
    "Harleen, Breaking Glass, Criminal Sanity & the Novels",
    ["Harleen graphic novel", "Harleen comic", "Sejic", "Šejić", "Breaking Glass", "Mariko Tamaki",
     "Criminal Sanity", "Kami Garcia", "Rachael Allen", "DC Icons", "Mad Love novel"],
    order=109,
    folder=ALTCOM,
    tag="lore",
    sticky=3,
    description="Standalone retellings: Šejić's Harleen, the YA Breaking Glass, Joker/Harley: Criminal Sanity, and the prose novels.",
    content="""
    [ALTERNATE CONTINUITIES: standalone retellings]
    • Harleen (Stjepan Šejić, DC Black Label, 2019): a slow, intimate psychological tragedy. Brilliant, insecure Dr. Harleen Quinzel pursues research on Gotham's criminals and the capacity for empathy, walks the politics of funding (Bruce Wayne, Harvey Dent), and is drawn step by step into a mutual obsession with the Joker until she becomes Harley. Mature, grounded and romantic-horror in tone. Great for "how could she fall for him?" depth.
    • Harley Quinn: Breaking Glass (Mariko Tamaki & Steve Pugh, DC Ink YA, 2019): teenage Harleen arrives in Gotham alone and is taken in by Mama, a drag queen who runs a cabaret. She befriends activist classmate Ivy and is tempted by a Joker who promises anarchy. When developers threaten her neighborhood, she has to decide what kind of chaos is worth it, and chooses her found family.
    • Joker/Harley: Criminal Sanity (Kami Garcia, Black Label, 2019–21): forensic psychiatrist Dr. Harleen Quinzel works with the GCPD to profile a serial killer who stages murders as art, the Joker, and the case is personal. She is his hunter, not his lover.
    • Novels: Batman: Mad Love (Paul Dini & Pat Cadigan, 2018) expands the classic origin in prose. Penguin Random House's DC Icons line has a young-adult Harley Quinn series by Rachael Allen (2022–).
    Compatible with main canon: emotional insight into her psychology, and the found-family ethos of Breaking Glass. Not compatible: plot specifics.
    """,
)

book.entry(
    "More Alternate-Universe Harleys",
    ["Old Lady Harley", "Bombshells", "DC Bombshells", "Batman '66", "Batman 66", "Batman '89", "Absolute Batman",
     "Absolute Harley", "Jack Grimm", "DCeased", "Earth-3", "Earth 3", "Thrillkiller", "Hayley Fitzpatrick",
     "Batman: Damned", "Betty & Veronica", "Birds of Prey Black Label", "Hunt for Harley", "multiverse Harley",
     "Future State"],
    order=110,
    folder=ALTCOM,
    tag="lore",
    sticky=3,
    description="Index of other Elseworlds and future Harleys: Old Lady Harley, Absolute Batman, Bombshells, '66/'89, DCeased, Earth-3, Thrillkiller.",
    content="""
    [ALTERNATE CONTINUITIES: more Harleys]
    • Old Lady Harley (Frank Tieri, 2017–18): a possible post-apocalyptic future where an elderly, still-lethal Harley roams a wasteland with older versions of Red Tool, Big Tony, Coach and the gang.
    • Absolute Batman (2024–): Harley is the leader of the Red Hood Gang and an ally of this Batman. She is the daughter of Jack Grimm, the Absolute Joker, which is why she hates him.
    • Harley Quinn & the Birds of Prey (Conner & Palmiotti, Black Label, 2020–21): an adults-only romp in which Harley returns to Gotham, is hunted by nearly everyone, and tangles with the Birds of Prey. It reads as an "R-rated" Coney-era sequel.
    • DC Comics Bombshells: a WWII pin-up-era Harley. Batman '66 and Batman '89: Harley folded into those film and TV looks.
    • DCeased (2019–): Harley is caught up in the Anti-Life "zombie" apocalypse with the rest of the DC Universe.
    • Earth-3 (the evil-mirror world): one Harleen was a victim of Owlman; another is an antihero Red Hood whose hammer is named "Kirby".
    • Batman: Thrillkiller (1997, Elseworlds): Hayley Fitzpatrick, a schoolgirl sidekick to a female Joker, Bianca Steeplechase.
    • Batman: Damned (Black Label): a grimy, mature cameo Harley. Harley & Ivy Meet Betty & Veronica (2017–18): an Archie crossover. Crossovers with the TMNT; Batman/The Spirit.
    • The Multiverse (main canon, 2023): fifty alternate Harleys, including a Mermaid Harley, met in "Who Killed Harley Quinn?". Earth-48's talking hyenas act as Bud and Lou's guides.
    • Future State: Harley Quinn (2021): in a dystopian near-future Gotham under the Magistrate, Harley is pressed into helping the regime hunt costumed criminals, and plays her own game.
    """,
)
