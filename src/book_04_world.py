from lb import Book

book = Book(
    "Harley Quinn — 04 Places, Groups & Things",
    """
    The world around Harley Quinn: the places she has lived, worked, been locked up
    in and blown up, the gangs and teams she has belonged to, and the objects and
    substances tied to her story. Entries trigger on place and object names.
    """,
    category="world",
    tags=["Harley Quinn", "DC Comics", "locations", "organizations", "items"],
    scan_depth=5,
    token_budget=3000,
    entry_limit=8,
)

HOMES = book.folder("01 · Harley's Homes & Hideouts")
GOTHAM = book.folder("02 · Gotham City Locations")
NYC = book.folder("03 · Brooklyn & New York Locations")
GROUPS = book.folder("04 · Organizations & Gangs")
THINGS = book.folder("05 · Objects & Substances")

# ─────────────────────────────── HOMES ───────────────────────────────

book.entry(
    "Harley's Homes Through the Years",
    ["her apartment", "her home", "where she lived", "hideout", "hideouts", "Jake's Joke Shop", "H.Q.H.Q.",
     "Glover Building", "storage unit", "where she's lived"],
    order=60,
    folder=HOMES,
    tag="location",
    sticky=2,
    description="Timeline of every place Harley has called home, from Joker hideouts to Coney Island to Gotham today.",
    content="""
    [Harley's Homes — Timeline]
    • Childhood: the Quinzel family home in Brooklyn (Canarsie, later Bensonhurst).
    • College: Gotham; a gymnast in the dorms.
    • The Joker years: a string of Joker hideouts in abandoned funhouses, toy factories and warehouses. Harley Loves Joker adds Jake's Joke Shop, a secret luxury hideout she had the Carpenter build (pool, hyena run, big-top bedroom, $3 million bill).
    • Solo, 2000–01: H.Q.H.Q. in Gotham's Glover Building, base of the Quinntets. It was a sleepover venue with her "wild new digs".
    • Metropolis, 2002: the late Ms. Chance's apartment, shared with Ivy, next door to Jimmy Olsen.
    • Arkham cells: many times, including a voluntary year.
    • Gotham City Sirens, 2009–11: the Riddler's townhouse (squatting), then the abandoned Gotham City Shelter for Cats and Dogs, then the closed Gotham County Arboretum, all shared with Ivy and Catwoman.
    • New 52, 2011–13: Belle Reve cells, then a storage-unit crash pad full of "treasures", which the Joker bombed.
    • Coney Island, 2013–2020: her own four-story building (see its entry), the fourth-floor penthouse loft with a roof deck. Later a separate "secret headquarters" clubhouse near Coach and the Gang.
    • Gotham, 2021–: back in the city, in modest apartments and then a home shared with Poison Ivy (2022–25). Eden, Ivy's hidden forest under the city, is always a refuge.
    • Present (2026): after the breakup with Ivy she is based around Throatcutter Hill, working out of her "destructive agency".
    Decor, wherever she is: stolen trophies, comics, stuffed animals, dog beds, weapons in the fridge, and Bernie on a shelf of honor.
    """,
)

book.entry(
    "The Coney Island Building",
    ["Coney Island building", "her building", "the penthouse", "the loft", "fourth floor", "express elevator",
     "landlady", "Coney Island apartment", "Madame Macabre's", "House of Wax", "House of Wax and Murder",
     "freak show floor", "Coney Island Freakfest", "her roof"],
    order=61,
    folder=HOMES,
    tag="location",
    sticky=2,
    description="Layout, tenants, businesses and history of the four-story Coney Island building Harley inherited.",
    content="""
    [Harley's Coney Island Building (2013–2020)]
    Inherited from an anonymous former Arkham patient via lawyer Robert Coachman, with back taxes, real-estate taxes, insurance and upkeep attached.
    Layout:
    • Ground floor, commercial: the Coney Island Freakfest and Burlesque (freak show and theater; Big Tony takes tickets) and Madame Macabre's House of Wax and Murder (wax figures of killers such as Jeffrey Dahmer, Albert Fish, Gilles de Rais and the Joker; the basement has tunnels leading all over).
    • Second floor: eight apartments, mostly rented to performers. Tenants include Big Tony, Queenie, Goat Boy, Madame Macabre and her son Mason, Eggy (Egg Fu), Rodney, and at times Sy Borgman.
    • Third floor: storage and lumber, which Ivy turned into an indoor dog park with grass and trees for Harley's rescue pack.
    • Fourth floor: entirely Harley's. A huge loft/penthouse with a private express elevator and roof access. The roof holds her sun and moon-bathing spot, potted plants from Ivy, and the Scatapult.
    Life there: rent is due on the first (Harley forgets to collect). The water heater bursts; assassins come through the kitchen window; there is a morgue fridge; Christmas dinners end in fire. The view is the boardwalk, the Wonder Wheel, the beach and the Atlantic. In 2018 a mini-volcano appeared offshore (Minor Disaster).
    """,
)

book.entry(
    "Eden — Ivy's Hidden Forest",
    ["Eden", "hidden forest", "underground forest", "garden under Gotham", "Ivy's garden"],
    order=62,
    folder=HOMES,
    tag="location",
    sticky=2,
    description="Eden: the secret forest Poison Ivy grew beneath Gotham as a refuge for Harley.",
    content="""
    [Eden]
    A lush, secret forest that Poison Ivy grew in a hidden space beneath Gotham City as a safe haven for Harley: a green, living sanctuary no one else knows how to find, full of fruit, flowers and soft moss. During the Joker War (2020) Harley sheltered a battered Batman there. Punchline tracked them down and tried to torch it, and Harley answered with a flamethrower.
    Emotional meaning: proof, in root and leaf, that Ivy loves her. After the 2026 breakup, visiting Eden would hurt, and the question of whether Ivy would let it wither or keep it alive for her is a painful one.
    Also Ivy's classic lairs over the years: greenhouses, a toxic-waste dump (where she first nursed Harley back to health), Robinson Park, and the Gotham County Arboretum.
    """,
)

# ─────────────────────────────── GOTHAM ───────────────────────────────

book.entry(
    "Gotham City — Harley's View",
    ["Amusement Mile", "Robinson Park", "Crime Alley", "Iceberg Lounge", "back in Gotham", "about Gotham",
     "this city"],
    order=63,
    folder=GOTHAM,
    tag="location",
    sticky=2,
    description="Gotham City from Harley's point of view: her old stomping grounds, notable locations, and her current relationship with the city.",
    content="""
    [Gotham City, through Harley's eyes]
    Her adopted city, full of bad memories. "This city is messed up in the head. I can officially give it that diagnosis because I'm a doctor."
    Key spots in her story:
    • Arkham Asylum and Arkham Tower; Ace Chemicals; Blackgate Penitentiary (see their entries).
    • Robinson Park: where the Joker's rocket crashed in No Man's Land, and where Ivy found and saved her.
    • Amusement Mile: a boardwalk-style carnival strip, perfect for clown crime. She fought Two-Face here in 2023.
    • Iceberg Lounge: the Penguin's club, a regular haunt in the Joker days.
    • Wayne Manor: she robbed the Halloween gala (2001), and has never been let back in.
    • Gotham University / Gotham State University: her alma mater. Gotham City Community College, where she taught Abnormal Psych on community service.
    • Throatcutter Hill: her current turf.
    • The sewers ("I may be in the sewer, but you better get your mind out") and the old funhouses and toy factories used as Joker hideouts.
    Relationship with Gotham now: she came back in 2021 to atone and help it heal from the Joker War. The GCPD distrusts her, the Bat-Family tolerates her, and the neighborhoods she protects love her. Under Mayor Ivy (2026) the city is lurching toward a plant-choked crisis ("Bad Seeds").
    """,
)

book.entry(
    "Arkham Asylum & Arkham Tower",
    ["Arkham", "Arkham Asylum", "Arkham Tower", "the asylum", "padded cell", "straitjacket", "Blackgate", "orderlies",
     "Dr. Arkham", "Jeremiah Arkham", "inmate", "patient files"],
    order=64,
    folder=GOTHAM,
    tag="location",
    sticky=2,
    description="Arkham Asylum, where Harley worked, fell for the Joker and was imprisoned; Arkham Tower; Blackgate.",
    content="""
    [Arkham Asylum]
    Gotham's notorious hospital for the criminally insane, and the place Harley's life changed. It has been her workplace (intern, then psychologist), her crime scene (she freed the Joker more than once), her cell (many stays: straitjacket, muzzle, padded rooms, including a voluntary year seeking parole), and her battlefield (the 2011 takeover with the Joker, and a Scatapult-assisted break-in to rescue Ivy).
    Harley's memories of it: the smell of disinfectant and fear; night-shift orderlies; the first time he smiled at her through the glass; a stolen rose; the Ventriloquist being kind in her first lonely week; Dr. Sterano stealing her notes; therapy sessions with a young Jason Todd.
    Arkham Tower (2021–22): after Arkham's destruction, Hugo Strange's facility was reborn as Arkham Tower, a new open-to-the-public mental-health center using the Arkham name. Harley's return to practicing psychology was tied to it, which raised uncomfortable questions for her about whether Gotham should keep the name at all.
    Blackgate Penitentiary: Gotham's regular prison. In the Arkham games, pre-villain Dr. Quinzel worked there. In comics it is where Punchline was held and seized control.
    """,
)

book.entry(
    "Ace Chemicals",
    ["Ace Chemicals", "Ace Chemical", "chemical plant", "chemical factory", "the vats", "Ace Chemical Processing"],
    order=65,
    folder=GOTHAM,
    tag="location",
    sticky=2,
    description="Ace Chemicals: the plant where the Joker was 'born' and where Harley was plunged into a vat.",
    content="""
    [Ace Chemicals]
    The Ace Chemical Processing Plant in Gotham, where the Joker's origin happened when he fell into a vat. In New 52 canon the Joker took Harleen there the night she freed him, called it "her birthday", and plunged her into a vat, bleaching her skin white and "freeing" her. It is also where Harley, dressed in the Joker's old Red Hood costume, lured Batman into a chemical trap (2012). During the Joker War it was Joker Venom central until it blew up.
    For Harley it is a charged place: a baptism she didn't choose (or did, depending on how she tells it that day), and the symbol of everything she has walked away from. Adaptations also lean on it: the 2016 film shows her swan-diving into a vat there by choice, and in the 2020 film she blows the plant up to announce her breakup.
    """,
)

book.entry(
    "Throatcutter Hill",
    ["Throatcutter Hill", "her neighborhood", "gentrification", "smoothie shop", "destructive agency office"],
    order=66,
    folder=GOTHAM,
    tag="location",
    sticky=2,
    description="Throatcutter Hill: the gritty Gotham neighborhood Harley adopted and defends against Althea Klang's gentrification.",
    content="""
    [Throatcutter Hill]
    A notoriously dangerous Gotham neighborhood and Harley's favorite: grimy, cheap, full of oddballs, strays, dive bars, bodegas and people the rest of the city forgot. By 2024 real-estate supervillain Althea Klang had gentrified it beyond recognition: boutique smoothie bars, luxury condos, rising rents, and people pushed out.
    Harley made it her cause. She runs a "destructive agency" (her Chandler-style private-eye parody) from the neighborhood, smashes Klang's businesses, fights the Refuse Men sanitation mob, sides with the locals, and patrols it with Chicken Fingers, its homeless self-appointed protector. In 2026 it is the beat of her brooding "Batquinn" persona.
    Suggested flavor (not canon specifics): noir voice-over, neon, rain, graffiti with her diamonds, longtime locals who feed and shelter her, and new-money joggers who cross the street when they see her.
    """,
)

# ─────────────────────────────── NYC ───────────────────────────────

book.entry(
    "Coney Island & Brooklyn Landmarks",
    ["boardwalk", "the boardwalk", "Cyclone", "Wonder Wheel", "Luna Park", "Nathan's", "Scare-O-Rama",
     "Brighton Beach", "Sheepshead Bay", "Bay Ridge", "Mill Basin", "Prospect Park", "Prospect Park Zoo",
     "Kensington", "Fire Island", "Rikers Island", "Steeplechase", "Coney Island landmarks"],
    order=67,
    folder=NYC,
    tag="location",
    sticky=2,
    description="Coney Island and New York City places from Harley's Brooklyn years.",
    content="""
    [Harley's New York]
    • Coney Island: boardwalk (the Riegelmann Boardwalk), beach, amusement rides (the Cyclone roller coaster, the Wonder Wheel, Luna Park; the Scare-O-Rama dark ride where an assassin once jumped her), hot-dog stands (Nathan's; Nate Man the vendor), the seal pool at the aquarium (where she threw Ivy's love-berry plant), and the old Steeplechase Park mascot, a grinning "funny face" clown that looks uncomfortably like the Joker. She watches sunrises from the boardwalk with Sy.
    • Brooklyn neighborhoods: Canarsie (where she was born), Bensonhurst (the family home), Sheepshead Bay (singles bar), Bay Ridge (diner), Mill Basin (a Russian agent's mansion, blown up), Kensington (the Rubensteins), Brighton Beach, and Prospect Park Zoo (a Russian-spy showdown with freed animals).
    • Elsewhere in the city: Manhattan (Tanduuri 2 Die 4; the corrupt mayor's office), Staten Island (Edwin's cage; Fresh Kills as a Scatapult target), Rikers Island (her father's and Mason's prison), Fire Island (where Mason was murdered), the Brooklyn Bridge (accidentally Scatapulted), and the J train (hit dead on).
    • Belt Parkway (the Skate Club route) and Kingsborough (the morgue fridge; the Kingsborough Killers derby team).
    """,
)

book.entry(
    "Free Spirit Assisted Living Home & Skate Club",
    ["Free Spirit", "Free Spirit Assisted Living Home", "nursing home", "assisted living", "retirement home",
     "Skate Club", "roller rink", "first rule of Skate Club", "Brooklyn Bruisers"],
    order=68,
    folder=NYC,
    tag="location",
    sticky=2,
    description="Harley's two Coney-era workplaces: the Free Spirit Assisted Living Home and the roller-derby rinks and underground Skate Club.",
    content="""
    [Free Spirit Assisted Living Home]
    A Brooklyn home for the elderly where "Dr. Quinzel" worked as the resident therapist, in a lab coat and full-body makeup. Supervisor: the demanding Dr. Hertz. Friend and coworker: nurse Sakim. Special wing: patients who are a danger to themselves, which piqued her interest. Notable patients: Ida Rubenstein (Alzheimer's; Harley bulldozed her "neglectful" family's house before reading the file), Mrs. Abby (whom Harley revived after someone stole her medical equipment), Seymour Bupkin (bondage-gear enthusiast), and Sy Borgman. Harley loves the old folks: she listens to their stories, avenges them and smuggles them snacks.
    [Roller Derby & Skate Club]
    • Brooklyn Bruisers: her official derby league team, captained by Summer Daze. She won her tryout as the last skater standing. Derby name "Killer Kwinn". Wins pay a share of the door; losses pay in drinks and medical supplies. She was kicked off for playing croquet with an opponent's head.
    • Skate Club: Summer's underground, no-rules derby, reached via the Belt Parkway. The first rule of Skate Club is you don't talk about Skate Club. Anyone on wheels can compete and bets fly. Harley exploded an unbeaten giantess, Maria Monsterella, with explosive toothpaste (and was disqualified on a technicality).
    """,
)

book.entry(
    "Metropolis & the Daily Planet (Harley's stint)",
    ["Daily Planet", "Metropolis", "Planet newsroom", "Lois Lane", "Special Crimes Unit", "Centennial Park"],
    order=69,
    folder=NYC,
    tag="location",
    sticky=2,
    description="Harley's Metropolis chapter: the Daily Planet love column, the apartment near Jimmy Olsen, Superman trouble.",
    content="""
    [Metropolis]
    In 2002 Harley and Ivy fled Gotham's bounty for the Big Apricot. After a fight with Thorn in Centennial Park and a run from the Special Crimes Unit, Harley took over a dead woman's apartment as her "niece" Holly Chance, next door to Jimmy Olsen, and pheromoned her way into a job as the Daily Planet's love-advice columnist under Perry White. She met Clark Kent without a clue.
    Her advice column was a romantic war zone. Bizarro fell for her, and Superman ended her scheme. She has been back since: Daily Planet intern (for a day in 2018), Legion of Doom and Justice League adventures, and in the animated series' fifth season she and Ivy moved to Metropolis.
    """,
)

# ─────────────────────────────── GROUPS ───────────────────────────────

book.entry(
    "Suicide Squad / Task Force X — How It Works",
    ["Task Force X", "neck bomb", "nanobomb", "micro-bomb", "the Wall", "how the Suicide Squad works"],
    order=70,
    folder=GROUPS,
    tag="organization",
    sticky=2,
    description="The government black-ops team of expendable villains Harley has been forced into; rules, bombs, prison.",
    content="""
    [Task Force X — the Suicide Squad]
    Amanda Waller's black-ops unit of imprisoned supervillains, sent on deniable suicide missions in exchange for reduced sentences. Leverage: explosives implanted in their necks or heads (nanobombs or micro-bombs), detonated for disobedience or escape. Home base: Belle Reve Penitentiary, a swamp prison in Louisiana.
    Harley's service: drafted in 2011 after her arrest, and one of the Squad's most frequent members through the New 52 and Rebirth (2011–2020), with later appearances. Classic missions: Basilisk terrorists, zombie-virus outbreaks, Mayan sacrifice survival, the Justice League vs. Suicide Squad war.
    Her part in it: comic relief, loose cannon, psychologist, and the most likely member to hug a teammate or stab the mission plan. She famously escaped when a guard disabled her bomb and started a prison riot.
    Adaptations: the Squad is also central to her film (2016, 2021), game (Kill the Justice League, 2024) and animated appearances (Assault on Arkham, Hell to Pay, Suicide Squad Isekai).
    """,
)

book.entry(
    "The Joker's Gang & Clown Henchmen",
    ["Joker's gang", "Joker gang", "clown gang", "Joker goons", "Clownhunter", "Joker's henchmen"],
    order=71,
    folder=GROUPS,
    tag="organization",
    sticky=2,
    description="The Joker's gang of clown-masked henchmen: Harley's former coworkers, and the ex-members she now tries to save.",
    content="""
    [The Joker's Gang]
    The rotating army of clown-masked, disposable thugs who serve the Joker. For years Harley was his lieutenant over them. She bossed them around, befriended a few, and watched him kill them on a whim. In "The Clown at Midnight" (2007) he planned to murder all his old henchmen, and her.
    Notable ex-members in her life: Lewis LeBeau and Buster (who followed her into the Quinntets); Kevin (her best friend since 2021, reformed); Keepsake (turned into her obsessive enemy); Punchline (his true-believer protégée, her nemesis); and countless nameless goons from Joker War, whom she tried to steer away from him.
    Clownhunter: a young vigilante who hunts Joker clowns with a batarang-studded bat. Harley's attitude toward him is complicated, since she once was one.
    Harley's current stance: every clown who wants out deserves a second chance, and everyone who stays in gets the mallet.
    """,
)

book.entry(
    "Other Teams & Affiliations",
    ["Secret Six", "Secret Society", "Legion of Doom", "Hall of Doom", "Sinestro Corps", "Female Furies",
     "Justice League Unlimited", "Bureau of Sovereignty", "Sanctuary", "Sinn-Dicate", "her teams",
     "teams she's been on"],
    order=72,
    folder=GROUPS,
    tag="organization",
    sticky=2,
    description="Index of every team and group Harley has belonged to or been linked with, plus Sanctuary.",
    content="""
    [Harley's Teams & Affiliations — Index]
    • The Joker's gang (lieutenant, 1990s–2000s).
    • The Quinntets (her own gang, 2001–02).
    • Secret Six (briefly; quit, ca. 2008).
    • Secret Society of Super-Villains; Legion of Doom (villain-era alliances; the animated series' Legion of Doom).
    • Gotham City Sirens (with Ivy and Catwoman, 2009–11).
    • Suicide Squad / Task Force X (2011–2020 and on and off since); Suicide Squad Seven; Task Force XL; Task Force XX (Batwing's reformed-villain team, 2022).
    • Gang of Harleys (her Brooklyn protégées, 2015–).
    • Female Furies ("Hammer Harleen", briefly, 2018); Sinestro Corps (briefly deputized); Green Lantern ring (borrowed once).
    • Birds of Prey (the Black Label Harley Quinn & the Birds of Prey, 2020; the 2020 film).
    • Justice League (assorted team-ups); Justice League Unlimited (loosely, 2024–); Bureau of Sovereignty (formerly).
    • Batman Family (probationary ally, 2021–).
    Sanctuary: a secret Kansas trauma-therapy center for heroes run with Batman, Superman and Wonder Woman's backing. Ivy was a patient and Harley snuck in to be with her, which made her a survivor and a suspect in the massacre (Heroes in Crisis, 2018).
    """,
)

# ─────────────────────────────── THINGS ───────────────────────────────

book.entry(
    "Joker Venom & Laughing Gas",
    ["Joker Venom", "Joker gas", "laughing gas", "Smylex", "Joker toxin", "rictus grin", "laughing to death"],
    order=73,
    folder=THINGS,
    tag="item",
    sticky=2,
    description="Joker Venom: the Joker's lethal laughing toxin; Harley's immunity, her ability to brew it and make antidotes.",
    content="""
    [Joker Venom]
    The Joker's signature poison: a gas or liquid that causes uncontrollable laughter, a frozen rictus grin and usually death, in endless variants (Smylex, a hallucinogenic Joker serum, Punchline's blend "tweaked with a bit of Fear Toxin, and a little bit of Venom").
    Harley and Venom:
    • She is immune, thanks to Ivy's serum. She was the only one standing after a Joker-gas attack at Deadshot's funeral.
    • She is the only person besides the Joker known to brew it. She reverse-engineered the formula and developed an antitoxin.
    • During the Joker War her concoction helped Batman shake off Punchline's hallucinogenic Joker serum.
    • She was framed with Smylex for a murder in 2019.
    • She hates the smell. It is a sensory trigger that drags up the old days.
    """,
)

book.entry(
    "The Scatapult",
    ["Scatapult", "poop catapult", "catapult"],
    order=74,
    folder=THINGS,
    tag="item",
    sticky=2,
    description="The Scatapult: the rooftop catapult Big Tony built to fling Harley's pets' poop across New York; also a Harley launcher.",
    content="""
    [The Scatapult]
    A rooftop catapult on Harley's Coney Island building, designed by Harley and built by Big Tony (with a $20,000 electronic guidance system bought with pawned Russian-spy rings), to dispose of the mountains of waste from her dozens of rescue dogs. Harley unveiled it with a picnic.
    Greatest hits: the first bag missed Fresh Kills and hit the Brooklyn Bridge; one splattered a Coney Island roller coaster; one hit the moving J train dead on; one volley hit the windows of DC Comics' Manhattan offices mid-pitch (a fourth-wall gag); an assassin was loaded in and launched into a blimp and a biplane propeller; and Harley launched herself, with a stolen parachute, across the Hudson toward Gotham to rescue Ivy, crashing through a pizzeria roof. Queenie runs when it is fired. Hipsters who insult Canarsie get targeted.
    """,
)

book.entry(
    "Harley's Trophies, Keepsakes & Odd Possessions",
    ["keepsakes", "trophies", "souvenirs", "treasures", "dessert tray", "Apokolips hammer", "Challenge Belt",
     "flaming sword", "Clatterbuck comics"],
    order=75,
    folder=THINGS,
    tag="item",
    sticky=2,
    description="Notable objects Harley owns or has owned: Bernie, the stolen giant heist prop, Brekemoff's rings, cosmic gear, fan comics and more.",
    content="""
    [Harley's Stuff]
    • Bernie the Beaver (see Relationships), her most treasured possession.
    • Her "treasures": a storage-unit hoard of junk and mementos, mostly lost to the Joker's bomb in 2013. She dragged what was left to Brooklyn on a motorbike.
    • An oversized prop from the Finger Warehouse (a museum of giant heist props) that reminded her of her first boyfriend, the only thing she took (2001).
    • Ivana Brekemoff's rings, swiped from a falling Russian spy and pawned for $140,000 plus a samurai sword.
    • Old red-and-black jester outfits in the closet (nostalgia hazard).
    • Meredith Clatterbuck's "Harley Quinn" fan comics, which bend reality. She read them to her dying mother.
    • Cosmic leftovers: the Apokoliptian hammer (lost), the Challenge Belt and the Angel of Retribution's armor and flaming sword (handed to Mirand'r), a fused red and black lantern ring won in an online auction, a cosmic treadmill ride, and a Cosmic Carrot (eaten).
    • A morgue refrigerator; a samurai sword; a pizza cutter with history; roller skates; a derby helmet; a mech suit.
    • The dessert tray the Moonlighter's captain gave her for saving the cruise.
    """,
)
