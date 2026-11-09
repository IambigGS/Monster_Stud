# Exhaustive Source & Asset Catalog — Monster Stud: Genetic League & Legends Arena

All **97 unique embedded `.webp` artworks** (118 total extracted files including the starter trio convenience folder) and **100% of the game mechanics, tabs, genetics, power-ups, and competitive tiers** from [`Monster_Stud_Seven_Competition_Tabs_Reordered.html`](file:///c:/bgs/all%20myAssets/0myApps-All/flow-automation-sandbox/stories/Monster_Stud%20-%20V2/raw_assets/Monster_Stud_Seven_Competition_Tabs_Reordered.html) are cataloged below inside [`stories/Monster_Stud - V2/raw_assets/extracted_art/`](file:///c:/bgs/all%20myAssets/0myApps-All/flow-automation-sandbox/stories/Monster_Stud%20-%20V2/raw_assets/extracted_art).

> **UI-Border Note from Visual Inspection**: The extracted creature `.webp` files in `all_species_tiers/` and `special_genes/` have a baked-in 2D rectangular card border/frame around the portrait. Rather than uploading framed 2D cards directly into Google Flow, we use the exact physical, anatomical, and lighting descriptives below to generate clean, borderless `Nano Banana 2` foundation assets (`@char_`, `@set_`, `@prop_`) in matching `8k dark-fantasy realism`.

---

## 1. Complete Game Architecture, 8 Core Tabs & Power-Up Mechanics

- **Game Title & Tagline**: *Monster Stud — Genetic League & Legends Arena* (`"Breed the anatomy. Inherit the weapons. Raise a champion."`)
- **Starting State**: The player manages **The Newblood Stable** (limit: **6 live monsters**, starting with **500 gold** and **3 Common Starters**: a Dragon, a Stegosaurus, and a Dire Wolf, each starting at Age 1/10, Generation 0, Grade D, ~69–71 Combat Rating).
- **The 8 Interactive Game Tabs**:
  1. **My Stable (`stable`)**: Displays up to 6 live monster cards with their live Combat Rating (`CR`) banner at the top of the portrait, Genetic Rarity badge (`COM`, `UNC`, `RAR`, `EPC`, `LEG`), 4-slot Special Gene strip (`Mythic`, `Colossus`, `Ravager`, `Phantom`), inherited anatomy weapon tags (`Horns`, `Claws`, `Fangs`, `Armour`, `Wings`, `Spines`), 5 core combat stats vs. individual genetic ceilings, remaining genetic growth bar, and League XP milestone tracker. Monsters retire after 10 seasons (Age 10/10) and can be sold for gold or archived to the Legends Arena.
  2. **Breeding Lab (`breed`)**: Pairs `Parent A` + `Parent B` for **1,000 gold** (no breeding cooldown) to birth a new offspring with an auto-generated compound name (from 79 prefixes, 84 middles, 68 suffixes, and 80 species-specific tokens). Offspring inherit 1 of 2 alleles per gene from each parent across **35 tracked genetic loci**, blending parent stats with random variation, **Genetic Legacy** carryover (`+power/defence/speed/vitality/technique` from veteran parents), a **25% chance of a named Birth Mutation** (`+1` to `+3` stat & ceiling boost), and an independent **1.2% chance per Special Gene** to discover a new recessive carrier allele.
  3. **Leagues & International Championships (`league`)**:
     - **The 5 Domestic Divisions** (20 monsters per division, 19-bout round-robin season, `-9` to `+9` independent form roll per bout; Top 3 promote, Bottom 3 relegate):
       - **Division 5** (Target CR `100`, Min Potential `0`, AI Roster: 100% Common, Bout Win: `+10g`, Podium: `100/50/25g`)
       - **Division 4** (Target CR `200`, Min Potential `75`, AI Roster: 100% Common, Bout Win: `+20g`, Podium: `200/100/50g`)
       - **Division 3** (Target CR `300`, Min Potential `90`, AI Roster: 50% Uncommon / 50% Common, Bout Win: `+30g`, Podium: `400/200/100g`)
       - **Champions Division** (Target CR `400`, Min Potential `120`, AI Roster: 50% Rare / 50% Uncommon, Bout Win: `+40g`, Podium: `800/400/200g`; promotion into Premier requires a Special-Gene carrier or expressed gene)
       - **Premier Division** (Target CR `500`, Min Potential `145`, AI Roster: 100% Rare, Bout Win: `+50g`, Podium: `2,000/1,000/500g`; 1st place qualifies for Europe)
     - **The 2 International Knockout Championships** (4 rounds: Round of 16 → Quarter-Final → Semi-Final → Final; single elimination):
       - **European Championship** (Target CR `600`, Entry Gate: Win Premier + express at least **2 of the 4 Special Genes**; AI Opponents: Epic 1-gene expressed; Bout Win: `+100g`; Title Prize: **`10,000g`**)
       - **World Championship** (Target CR `700`, Entry Gate: Win Europe + possess **Primal Apex** with **all 4 Special Genes expressed**; AI Opponents: Epic 2-to-3-gene hybrids; Bout Win: `+200g`; Title Prize: **`25,000g`**)
     - **Cinematic Live Combat Visualizer**: Full-bleed split-screen arena clash (`side-player` cyan accent vs. `side-opponent` ember-orange accent) with live health bars, 3-stage lunges, central gold `VS` medallion, impact shockwaves, floating damage popups, and `KNOCKOUT` / `VICTORY` banners.
  4. **Legends Arena (`legends`)**: Eternal Hall of Fame where Age-10 retired veterans are archived with their peak-era genome and combat stats frozen forever, allowing exhibition dream matches between historical stable legends.
  5. **Monster Market & Supplies (`market`)**:
     - **4 Fixed Monster Market Tiers** (auto-replenished upon purchase):
       - **Common Offer (`1,000g`)**: No mutations, no special genes.
       - **Uncommon Offer (`2,000g`)**: 1 guaranteed Standard Birth Mutation.
       - **Rare Offer (`3,000g`)**: 2 guaranteed Standard Birth Mutations (no special genes).
       - **Premium Offer (`5,000g`)**: 1 guaranteed Special-Gene **carrier** allele `[100, 0]` (never pre-expressed), essential for breeding expressed `[100, 100]` hybrids.
     - **Supplies — Training Manual (`500g`)**: Upgrades a chosen stat (`Power`, `Defence`, `Speed`, `Vitality`, or `Technique`) by up to **`+2` points** directly toward the monster's genetic ceiling.
  6. **Economy (`economy`)**: Full financial ledger tracking Opening Balance, Total Income, Total Spending, Net Change, category rules, and the last 40 timestamped transactions.
  7. **Bloodline & Records (`records`)**: Multi-generational family tree, lifetime breeding counter, career win/loss percentage, domestic/European/World title tally, stable renaming, and JSON backup save/load.
  8. **Gene Art Studio (`geneArt`)**: Interactive visual encyclopedia showcasing all 10 base species across all 7 visual power-up tiers, plus the 4 Special Genes and all 11 multi-gene hybrid combinations.

---

## 2. The 5 Core Combat Stats, 35 Genetic Loci & 4 Power-Up Pathways

### A. The 5 Core Combat Stats & Grades
- **Power (`power`)**: Physical striking force and damage dealt; boosted by `horns`, `claws`, `fangs`, `muscle`, `Mythic (+2)`, and `Ravager (+3)`.
- **Defence (`defence`)**: Damage reduction and plating resistance; boosted by `armor`, `spines`, `scales`, `Mythic (+1)`, and `Colossus (+3)`.
- **Speed (`speed`)**: Initiative, strike tempo, and dodge rate; boosted by `wings`, `agility`, `biped (>60 = +1)`, and `Phantom (+3)`.
- **Vitality (`vitality`)**: Maximum health and durability; boosted by `size`, `armor`, `Mythic (+2)`, and `Colossus (+2)`.
- **Technique (`technique`)**: Critical strike accuracy and combat precision; boosted by `precision`, `claws`, `Mythic (+1)`, `Ravager (+1)`, and `Phantom (+1)`.
- **Overall Combat Rating (`CR`) & Grades**: Sum of effective combat stats (`Grade D`: ≤100 · `Grade C`: 101–200 · `Grade B`: 201–300 · `Grade A`: 301–400 · `Grade S`: 401+).

### B. The 4 Ways a Monster Powers Up (The Core Progression Loop)
1. **Training Manuals (`+2` Stat Surge)**: Spending 500g in the Market/Supplies tab to train `Power`, `Defence`, `Speed`, `Vitality`, or `Technique` up to the monster's genetic potential ceiling.
2. **League XP Milestones & Seasonal Aging**: Fighting league bouts earns League XP (`+1` stat point every `100 XP`), while surviving each season ages the monster (`+1 Age` up to 10) and triggers `+2` natural seasonal stat growth ticks toward its genetic ceiling.
3. **15 Named Birth Mutations (25% Birth Chance or Market Uncommon/Rare)**:
   - *Power Mutations*: **Razor Claws** (`+1 Power`, `+12 claws`), **Heavy Horns** (`+2 Power`, `+15 horns`), **Crushing Fangs** (`+3 Power`, `+18 fangs`, `+5 claws`).
   - *Defence Mutations*: **Tough Hide** (`+1 Defence`, `+10 armor`, `+5 scales`), **Armoured Shell** (`+2 Defence`, `+16 armor`, `+10 scales`), **Fortress Plates** (`+3 Defence`, `+20 armor`, `+14 spines`).
   - *Speed Mutations*: **Light Feet** (`+1 Speed`, `+12 agility`), **Long Legs** (`+2 Speed`, `+16 limbLength`, `+8 agility`), **Spring Tendons** (`+3 Speed`, `+20 agility`, `+12 limbLength`).
   - *Vitality Mutations*: **Dense Frame** (`+1 Vitality`, `+10 size`), **Powerful Heart** (`+2 Vitality`, `+15 size`, `+5 muscle`), **Titan Heart** (`+3 Vitality`, `+20 size`, `+8 muscle`).
   - *Technique Mutations*: **Keen Senses** (`+1 Technique`, `+12 sensory`, `+4 precision`), **Battle Instinct** (`+2 Technique`, `+15 brain`, `+8 precision`), **Perfect Coordination** (`+3 Technique`, `+18 dexterity`, `+14 precision`).
4. **Recessive Special-Gene Expression & Multi-Gene Hybrid Synergy**:
   - Carrying one copy (`[100, 0]`) makes a monster a **Rare Carrier**. Pairing two carriers in the Breeding Lab can express two copies (`[100, 100]`), triggering a dramatic visual and stat transformation:
     - **1 Expressed Gene (`Epic`)**: Grants the gene's signature stat bonus and elemental aura.
     - **2 Expressed Genes (`Epic 2-Gene Hybrid`, qualifies for Europe)**: Grants both gene bonuses **plus `+1` to all 5 stats** (`+5 CR` synergy).
     - **3 Expressed Genes (`Epic 3-Gene Hybrid`)**: Grants all three gene bonuses **plus `+2` to all 5 stats** (`+10 CR` synergy).
     - **All 4 Expressed Genes (`Legendary — PRIMAL APEX`, qualifies for World Championship)**: Grants all four gene bonuses **plus `+3` to all 5 stats** (`+15 CR` synergy) and unlocks the ultimate 4-element obsidian Primal Apex form.

---

## 3. Environment Foundation Assets — The 7-Stage Power-Up Colosseums & Breeding Lab (`@set_...`)

- **Original Extracted Arena Reference**: [`colosseum_arena.webp`](file:///c:/bgs/all%20myAssets/0myApps-All/flow-automation-sandbox/stories/Monster_Stud%20-%20V2/raw_assets/extracted_art/arena/colosseum_arena.webp)
- **Shared Colosseum Architectural Blueprint**:
  - Symmetrical low-angle view across a circular stone battle ring in the foreground leading to wide central stone steps and a towering arched iron portcullis beast-gate, flanked by two colossal warrior statues and tall vertical banners, enclosed by curved multi-tiered arched spectator galleries and parapet fire braziers under a night sky.
- **The 7 Power-Up Colosseum Stages (Matching the 7 Competitive Tiers)**:
  1. **Stage 1 — Common Colosseum (`@set_colosseum_common`)**: Weathered sandstone and rough-hewn grey stone Colosseum with simple timber-and-iron portcullis gate, unpolished stone guardian statues, dusty cracked flagstone ring, tattered earthy-brown banners, and warm amber wood-fire braziers. *(Division 5 / 4 — Target CR 100–200)*
  2. **Stage 2 — Uncommon Colosseum (`@set_colosseum_uncommon`)**: Ancient moss-draped olive stone and hammered bronze Colosseum with creeping vines, glowing moss-green and amber alchemical fire braziers, and olive-and-bronze banners. *(Division 3 — Target CR 200–300)*
  3. **Stage 3 — Rare Colosseum (`@set_colosseum_rare`)**: Silver-inlaid grey stone Colosseum with sharp metallic crests, silver-armoured guardian statues, roaring cobalt-blue fire braziers, and cobalt-blue and silver heraldic banners. *(Champions / Premier — Target CR 300–400)*
  4. **Stage 4 — Epic Colosseum (`@set_colosseum_epic`)**: Black basalt and spiked dark-iron fortress Colosseum with heavy armoured gate plates, roaring crimson-red and molten-ember braziers, and blood-crimson banners. *(Premier / Europe Contender — Target CR 400–500)*
  5. **Stage 5 — Legendary Colosseum (`@set_colosseum_legendary`)**: Polished black-marble and ornate gilded-gold Colosseum with towering solid-gold warrior statues, blazing solar-gold fire braziers, and regal black-and-gold banners. *(Domestic / Continental Champion — Target CR 500–600)*
  6. **Stage 6 — European Champion Colosseum (`@set_colosseum_champion`)**: Gleaming platinum-and-silver grand stadium with crystalline arches, blazing electric-cyan plasma braziers, and luminous cyan geometric battle ring. *(European Championship — Target CR 600)*
  7. **Stage 7 — World Primal Apex Colosseum (`@set_colosseum_primal`)**: Jagged black obsidian Colosseum surging with all four special-gene energy streams (royal-purple Mythic, emerald Colossus, molten-crimson Ravager, and electric-cyan Phantom) blazing in the braziers and glowing through the obsidian floor runes. *(World Championship — Target CR 700)*
- **Additional Game Environment — The Genetic Breeding & Alchemy Chamber (`@set_breeding_lab`)**:
  - Derived from the `Breeding Lab` & `Gene Art Studio` tabs: A vaulted dark-stone and brass genetic sanctuary inside the Colosseum undercroft, featuring twin circular stone parent pedestals linked by glowing floor channels to a central sunken birthing/mutation crucible ring, surrounded by tall alchemical glass gene-columns pulsing with dormant violet, emerald, molten-crimson, and cyan bioluminescence.

---

## 4. All 10 Base Creature Species Across All 7 Evolution/Power-Up Tiers (70 Artworks in `all_species_tiers/`)

Every one of the 10 base species has **7 distinct extracted `.webp` artworks** (`_common`, `_uncommon`, `_rare`, `_epic`, `_legendary`, `_champion`, `_primal`) inside [`stories/Monster_Stud - V2/raw_assets/extracted_art/all_species_tiers/`](file:///c:/bgs/all%20myAssets/0myApps-All/flow-automation-sandbox/stories/Monster_Stud%20-%20V2/raw_assets/extracted_art/all_species_tiers):

### How the 7 Visual Power-Up Tiers Transform Every Species
- **Tier 1 — `Common` (`<species>_common.webp` · CR < 150)**: Earthy browns, weathered ochre, and charcoal greys; natural unarmoured hide/scales/feathers, simple bone horns and claws, grounded rookie silhouette.
- **Tier 2 — `Uncommon` (`<species>_uncommon.webp` · CR 150–249)**: Moss green, olive, and tarnished bronze; thicker muscular mass, heavier osteoderms/scales, sharper secondary horn ridges and longer talons.
- **Tier 3 — `Rare` (`<species>_rare.webp` · CR 250–349)**: Cobalt blue, slate, and polished silver; metallic-sheen scales/fur/plates, elongated silver-tipped horns and crests, and cold azure eye/seam highlights.
- **Tier 4 — `Epic` (`<species>_epic.webp` · CR 350–449)**: Charcoal black and volcanic crimson; heavy spiked dark-iron/basalt armour plating, glowing molten-orange and crimson magma fissures erupting along the neck, spine, and joints.
- **Tier 5 — `Legendary` (`<species>_legendary.webp` · CR 450–549)**: Regal obsidian black and burnished imperial gold; ornate gilded armour plates, swept-back golden crown horns, and radiant solar-gold firelight pulsing between scale seams.
- **Tier 6 — `European Champion` (`<species>_champion.webp` · CR 550–649)**: Gleaming platinum, mirror-silver, and diamond-ice; crystalline dorsal crests, razor-sharp silver-white plating, and blazing electric-cyan plasma aura.
- **Tier 7 — `World Primal Apex` (`<species>_primal.webp` · CR 650+)**: Jagged black volcanic obsidian infused with surging multicoloured cosmic energy (magenta-violet, electric cyan, molten gold, and emerald) blazing from the horns, spine plates, wing membranes, and eyes.

### The 10 Base Species Profiles & Anatomical Weapons
1. **Dragon (`dragon_common.webp` → `dragon_primal.webp` · Base Stats: `14 PWR / 11 DEF / 11 SPD / 13 VIT / 11 TEC` · Starter #1)**:
   - *Anatomy*: Muscular wyvern-dragon with wide leathery bat-like wings (`wings: 68`) tipped with thumb spurs, powerful hindlegs, raptorial foreclaws (`claws: 75`), long whipping tail (`tail: 78`), heavy reptile scales (`scales: 72`), swept-back crown horns (`horns: 74`), and fanged jaws (`fangs: 79`).
   - *7-Tier Visual Arc*: Progresses from weathered bronze-brown wyvern (`dragon_common`) → olive-and-moss scaled drake (`dragon_uncommon`) → cobalt-blue and silver frost-crest dragon (`dragon_rare`) → black-and-lava-crimson dreadwing with glowing dorsal magma vents (`dragon_epic`) → gilded solar-gold imperial dragon (`dragon_legendary`) → platinum-and-ice-cyan crystalline champion dragon (`dragon_champion`) → obsidian-and-neon-violet/cyan Primal Apex dragon (`dragon_primal`).
2. **Stegosaurus (`stegosaurus_common.webp` → `stegosaurus_primal.webp` · Base Stats: `10 PWR / 17 DEF / 6 SPD / 16 VIT / 8 TEC` · Starter #2)**:
   - *Anatomy*: Low-slung, heavily armoured quadruped herbivore tank (`armor: 84`, `Vitality: 16`, `Defence: 17`) on four pillar legs with blunt stone-crushing claws, featuring a signature double row of oversized diamond dorsal plates along its arched spine, a spiked thagomizer tail, and a rugged horned beak (`nasal horn + twin brow horns`).
   - *7-Tier Visual Arc*: Progresses from pebbly moss-green hide with bronze-brown dorsal plates (`stegosaurus_common`) → deep forest-olive hide with jagged verdigris plates (`stegosaurus_uncommon`) → slate-blue hide with silver-edged cobalt dorsal shields (`stegosaurus_rare`) → blackened basalt hide with glowing magma-cracked crimson dorsal plates (`stegosaurus_epic`) → black-and-gold imperial fortress plating (`stegosaurus_legendary`) → silver-platinum hide with glowing cyan crystal dorsal fins (`stegosaurus_champion`) → obsidian hide with blazing magenta-violet and cyan rune-lit dorsal crystals (`stegosaurus_primal`).
3. **Wolf / Dire Wolf (`wolf_common.webp` → `wolf_primal.webp` · Base Stats: `12 PWR / 9 DEF / 15 SPD / 11 VIT / 14 TEC` · Starter #3)**:
   - *Anatomy*: Lean, hyper-agile quadruped canid predator (`claws: 80`, `fangs: 76`, `mane: 58`) in a low coiled stance, with thick scarred forelegs, razor-clawed paws, a jagged bristling shoulder/neck mane, pointed ears, and a long snarling fanged muzzle.
   - *7-Tier Visual Arc*: Progresses from ash-grey and charcoal fur with silver-white bristling mane (`wolf_common`) → moss-tinted timber wolf with olive-bronze ruff (`wolf_uncommon`) → frost-blue and silver-furred dire wolf (`wolf_rare`) → charred-black hellhound with glowing ember-crimson mane fissures (`wolf_epic`) → royal gold-and-black armoured war-wolf (`wolf_legendary`) → platinum-white wolf wreathed in electric-cyan lightning (`wolf_champion`) → shadow-obsidian dire wolf surging with violet and electric-blue astral fire (`wolf_primal`).
4. **Gorilla (`gorilla_common.webp` → `gorilla_primal.webp` · Base Stats: `16 PWR / 12 DEF / 7 SPD / 17 VIT / 8 TEC`)**:
   - *Anatomy*: Massive knuckle-walking upright bruiser (`Power: 16`, `Vitality: 17`) with colossal boulder shoulders, thick craggy forearm plating, sagittal skull crest, sunken fierce eyes, and earth-shattering fists.
   - *7-Tier Visual Arc*: Earthy stone-brown silverback with rough bone shoulder ridges (`gorilla_common`) → moss-and-olive crag ape (`gorilla_uncommon`) → cobalt-and-silver ironback titan (`gorilla_rare`) → volcanic black basalt ape with glowing lava shoulder cracks (`gorilla_epic`) → gilded gold-armoured war ape (`gorilla_legendary`) → platinum-and-cyan plasma silverback (`gorilla_champion`) → obsidian multi-gene apex titan (`gorilla_primal`).
5. **Tiger (`tiger_common.webp` → `tiger_primal.webp` · Base Stats: `11 PWR / 8 DEF / 16 SPD / 10 VIT / 15 TEC`)**:
   - *Anatomy*: Low-prowling striped feline assassin (`Speed: 16`, `Technique: 15`) with swept-back dorsal spine quills along its shoulder blades, oversized saber-like canine fangs, white cheek ruff, and massive retractable foreclaws.
   - *7-Tier Visual Arc*: Warm ochre-gold and black striped saber-tiger (`tiger_common`) → jungle-olive and moss predator (`tiger_uncommon`) → cobalt-blue and silver-striped stalker (`tiger_rare`) → black-and-molten-crimson hellcat (`tiger_epic`) → burnished gold-and-onyx sovereign tiger (`tiger_legendary`) → silver-white and electric-cyan lightning tiger (`tiger_champion`) → obsidian and neon-violet/cyan apex saber-tiger (`tiger_primal`).
6. **Rhino (`rhino_common.webp` → `rhino_primal.webp` · Base Stats: `13 PWR / 17 DEF / 6 SPD / 16 VIT / 7 TEC`)**:
   - *Anatomy*: Colossal four-legged siege juggernaut (`Defence: 17`, `horns: 88`, `armor: 50`) with interlocking riveted hide plates, a massive upward-curving primary nasal horn, secondary brow horn, and spiked shoulder hump.
   - *7-Tier Visual Arc*: Weathered iron-grey and dusty bronze-plated war rhino (`rhino_common`) → moss-green stone-hide rhino (`rhino_uncommon`) → silver-and-cobalt steelhorn (`rhino_rare`) → black iron and magma-crimson siege rhino (`rhino_epic`) → gilded gold imperial juggernaut (`rhino_legendary`) → platinum-and-cyan crystalhorn (`rhino_champion`) → obsidian cosmic-horn apex juggernaut (`rhino_primal`).
7. **T. Rex (`trex_common.webp` → `trex_primal.webp` · Base Stats: `17 PWR / 10 DEF / 9 SPD / 14 VIT / 8 TEC`)**:
   - *Anatomy*: Towering bipedal apex theropod (`Power: 17`, `fangs: 78`, `tail: 85`, `scales: 82`) with a massive box-shaped crushing skull, rows of serrated ivory teeth, swept-back neck spines, small two-fingered forelimbs, and muscular taloned hindlegs.
   - *7-Tier Visual Arc*: Earthy brown-and-grey pebbled tyrant dinosaur (`trex_common`) → olive-and-moss swamp rex (`trex_uncommon`) → cobalt-blue and silver crest rex (`trex_rare`) → charred black and glowing lava-crimson tyrant (`trex_epic`) → gilded gold-and-black sovereign rex (`trex_legendary`) → platinum and electric-cyan storm rex (`trex_champion`) → obsidian and violet/cyan Primal Apex tyrant (`trex_primal`).
8. **Snake / Giant Serpent (`snake_common.webp` → `snake_primal.webp` · Base Stats: `9 PWR / 8 DEF / 14 SPD / 9 VIT / 18 TEC`)**:
   - *Anatomy*: Coiled, towering limbless viper (`Technique: 18`, `tail: 96`, `scales: 88`, `fangs: 72`) with diamond-patterned dorsal scales, ribbed ventral belly plates, swept-back head-crest horns, glowing slit eyes, and enormous curved Sabre-venom fangs.
   - *7-Tier Visual Arc*: Tan-and-charcoal diamondback serpent (`snake_common`) → moss-green and olive viper (`snake_uncommon`) → cobalt-blue and silver serpent (`snake_rare`) → black basalt and molten-lava serpent (`snake_epic`) → gilded gold-and-onyx royal cobra (`snake_legendary`) → platinum and electric-cyan plasma serpent (`snake_champion`) → obsidian and neon-violet/cyan apex wyrm-serpent (`snake_primal`).
9. **Bird / War Raptor (`bird_common.webp` → `bird_primal.webp` · Base Stats: `9 PWR / 8 DEF / 18 SPD / 9 VIT / 15 TEC`)**:
   - *Anatomy*: Fierce avian sky-hunter (`Speed: 18`, `Technique: 15`) with broad layered primary flight feathers, spiked feather-crest crown, hooked raptorial beak, muscular feathered legs, and razor-sharp golden talons, plus a long whip-like barbed tail.
   - *7-Tier Visual Arc*: Earthy brown-and-taupe war eagle (`bird_common`) → olive-and-moss forest raptor (`bird_uncommon`) → cobalt-blue and silver storm hawk (`bird_rare`) → crimson-and-black ember phoenix-raptor (`bird_epic`) → radiant gold-and-black imperial thunderbird (`bird_legendary`) → platinum and electric-cyan tempest raptor (`bird_champion`) → obsidian and violet/cyan cosmic apex raptor (`bird_primal`).
10. **Triceratops (`triceratops_common.webp` → `triceratops_primal.webp` · Base Stats: `14 PWR / 16 DEF / 7 SPD / 15 VIT / 8 TEC`)**:
    - *Anatomy*: Broad, heavily armoured quadruped ceratopsian (`Defence: 16`, `Vitality: 15`, `Power: 14`) featuring a scalloped bone neck-frill, two long forward-thrusting brow horns, a stout nasal horn, parrot-like crushing beak, and jagged dorsal spine plates rising behind the frill.
    - *7-Tier Visual Arc*: Weathered sandstone-brown and grey three-horned tank (`triceratops_common`) → moss-green and bronzehorn ceratopsian (`triceratops_uncommon`) → cobalt-blue and silver-frilled triceratops (`triceratops_rare`) → black basalt and molten-crimson siege triceratops (`triceratops_epic`) → gilded gold-and-black royal frill triceratops (`triceratops_legendary`) → platinum and cyan-crystal frill champion (`triceratops_champion`) → obsidian and neon-violet/cyan Primal Apex ceratopsian (`triceratops_primal`).

---

## 5. All 15 Special-Gene & Multi-Gene Hybrid Showcase Artworks (`special_genes/`)

Extracted into [`stories/Monster_Stud - V2/raw_assets/extracted_art/special_genes/`](file:///c:/bgs/all%20myAssets/0myApps-All/flow-automation-sandbox/stories/Monster_Stud%20-%20V2/raw_assets/extracted_art/special_genes). In gameplay, expressing these recessive genes `[100, 100]` applies their elemental colour/energy overlay to any monster's species portrait, while the `Gene Art Studio` showcases their **15 bespoke concept illustrations**:

### A. The 4 Pure Recessive Special Genes (1-Gene Expressed — `Epic`)
1. **Mythic (`mythic.webp` · `+2 PWR, +1 DEF, +2 VIT, +1 TEC`)**:
   - *Visual Descriptive*: A royal-purple and deep indigo dragon-drake wreathed in cosmic violet fire and floating starlight motes, with jagged amethyst crystal wing-spurs and glowing violet eyes.
2. **Colossus (`colossus.webp` · `+3 DEF, +2 VIT`)**:
   - *Visual Descriptive*: A massive, heavy-plated stone-and-earth behemoth quadruped with towering translucent emerald-green crystal shards erupting along its spine, moss-draped boulder hide, curved ivory tusks, and glowing emerald eyes.
3. **Ravager (`ravager.webp` · `+3 PWR, +1 TEC`)**:
   - *Visual Descriptive*: A volcanic black-basalt predatory drake with deep molten-red and bright orange lava fissures cracking across its muscular chest, shoulders, and legs, crowned with blazing fire-mane flames and a whip-like flame tail.
4. **Phantom (`phantom.webp` · `+3 SPD, +1 TEC`)**:
   - *Visual Descriptive*: A sleek, spectral ice-white and electric-cyan predator with translucent ghostly plasma tendrils streaming from its back, multi-pronged ice-crystal horns, and blinding cyan bioluminescent veins across its limbs.

### B. The 6 Two-Gene Hybrid Combinations (`+1 All Stats` Synergy — Qualifies for European Championship)
5. **Astral Titan (`astral_titan.webp` · `Mythic + Colossus`)**:
   - *Visual Descriptive*: Heavy quadruped titan clad in gilded gold and royal-purple stone armour, with half its dorsal spine erupting in glowing violet amethyst crystals and the forequarters surging with bright emerald-green crystal spikes.
6. **Ember Wraith (`ember_wraith.webp` · `Mythic + Ravager`)**:
   - *Visual Descriptive*: Obsidian-scaled predator engulfed in dual-tone hot magenta-violet and molten lava-orange flames, with glowing magma cracks along its limbs and a blazing neon-pink horn crown.
7. **Void Strider (`void_strider.webp` · `Mythic + Phantom`)**:
   - *Visual Descriptive*: Midnight-indigo cosmic stalker with a sweeping scorpion-like tail, wreathed in deep nebula-violet starlight and razor-thin ribbons of golden-white astral lightning.
8. **Stoneblaze (`stoneblaze.webp` · `Colossus + Ravager`)**:
   - *Visual Descriptive*: Hulking jade-green stone behemoth whose interlocking emerald-and-bronze armour plates are split open by roaring rivers of lava-orange fire erupting from its back and jaws.
9. **Frostguard (`frostguard.webp` · `Colossus + Phantom`)**:
   - *Visual Descriptive*: Heavy silver-stone fortress beast bristling with jagged glacial-ice and luminous turquoise-cyan crystal spires across its back, shoulders, and horned skull.
10. **Stormfire (`stormfire.webp` · `Ravager + Phantom`)**:
    - *Visual Descriptive*: Dark volcanic predator coursing with dual-elemental arcs of bright molten-gold fire along its lower body and crackling electric-blue lightning bolts whipping across its back and tail.

### C. The 4 Three-Gene Hybrid Combinations (`+2 All Stats` Synergy — World Championship Opponent Tier)
11. **Celestial Guardian (`celestial_guardian.webp` · `Mythic + Colossus + Phantom`)**:
    - *Visual Descriptive*: Majestic winged crystal dragon-guardian with pearlescent silver-white plating, prismatic stained-glass wings of emerald-green, violet, and cyan, and a radiant halo of pastel starlight.
12. **Inferno Sovereign (`inferno_sovereign.webp` · `Mythic + Colossus + Ravager`)**:
    - *Visual Descriptive*: Colossal black-iron and burnished-gold juggernaut dragon crowned with towering golden-flame horns and overlapping crimson-and-gold fortress plates radiating furnace heat.
13. **Phantom Reaper (`phantom_reaper.webp` · `Mythic + Ravager + Phantom`)**:
    - *Visual Descriptive*: Shadow-black void drake with a scythe-tipped crimson tail, neon-magenta and electric-cyan dorsal plasma fins, and molten-red claw markings.
14. **Titan Storm (`titan_storm.webp` · `Colossus + Ravager + Phantom`)**:
    - *Visual Descriptive*: Heavy steel-and-stone armoured beast surging simultaneously with turquoise-cyan frost-lightning along its dorsal crystal crest and molten-amber fire along its chest and forelimbs.

### D. The Ultimate 4-Gene Phenotype (`+3 All Stats` Synergy — Qualifies for World Championship)
15. **Primal Apex (`primal_apex.webp` · `Mythic + Colossus + Ravager + Phantom` — All 4 Expressed · `Legendary`)**:
    - *Visual Descriptive*: Symmetrical front-facing portrait of the ultimate World Championship sovereign — a colossal black-obsidian winged dragon-titan with a diamond cyan chest-core and a curved crown of obsidian horns, its four massive spread wings and shoulders Simultaneously radiating all four elemental gene streams: **emerald-green Colossus crystal energy** (upper left), **royal-purple Mythic nebula lightning** (lower left/inner), **blazing golden-orange & crimson Ravager magma fire** (center/upper right), and **electric-cyan Phantom plasma** (right wing).

---

## 6. The 11 Standard & Legacy Archetype Artworks (`standard_art/`)

Extracted from `STANDARD_ART_ASSETS` into [`stories/Monster_Stud - V2/raw_assets/extracted_art/standard_art/`](file:///c:/bgs/all%20myAssets/0myApps-All/flow-automation-sandbox/stories/Monster_Stud%20-%20V2/raw_assets/extracted_art/standard_art) (full-bleed 16:9 Colosseum portraits without white card borders):
1. **`standard_common.webp`**: Agile moss-green and yellow-bellied rookie lizard-drake with swept-back head spines in a torchlit stone arena.
2. **`standard_scorcher.webp`**: Fierce crimson-and-orange feathered raptor-drake with hooked beak and serrated tail spines in the torchlit arena.
3. **`standard_stalker.webp`**: Muscular charcoal-and-silver dire wolf with glowing ice-blue eyes and trailing blue spirit-wisps across its back.
4. **`standard_bulwark.webp`**: Heavy stone-brown quadruped tank with glowing emerald-green crystal dorsal spikes and curved brow/nasal horns.
5. **`standard_elite.webp`**: Armoured bronze-and-obsidian drake with curved golden horns and bright electric-blue energy vents along its spine and tail.
6. **`standard_champion.webp`**: Knuckle-walking volcanic black-stone gorilla-golem with glowing molten-orange magma veins across its chest and crested skull.
7. **`common_stoneback.webp`**: Heavy bronze-and-sandstone armoured quadruped ankylosaur-drake with a spiked shell and horned reptilian snout.
8. **`common_swiftfang.webp`**: Lean bipedal/semi-quadruped bronze-scaled raptor-lizard with a row of sharp dorsal spines and long grasping foreclaws.
9. **`common_horncrest.webp`**: Heavily plated bronze quadruped beast with twin swept-back ivory brow horns and serrated back plates.
10. **`common_dustrunner.webp`**: Low-slung desert-ochre armoured lizard-beast with overlapping shingle scales and an upturned snout horn.
11. **`common_ironhide.webp`**: Massive thick-plated bronze-and-iron quadruped charger with a sharp upward nasal horn and spiked shoulder plates.

---

## 7. Cartridge Inventory Tracker: "Featured in V1" vs. "Still on the Bench (Unused / Ready for V2+)"

### ✅ Featured in V1 (`Monster_Stud_Opening_Trailer_Scene_01` — 34s, 5 Clips)
- **Audio Spine**: [`MP3-Trailer-Opt1-V3-30secs-Primal Apex.mp3`](file:///c:/bgs/all%20myAssets/0myApps-All/flow-automation-sandbox/stories/Monster_Stud%20-%20V2/raw_assets/MP3-Trailer-Opt1-V3-30secs-Primal Apex.mp3) (`33.6s` duration, snapped to `34.0s` on the 2-second grid).
- **Environment Used (1 of 7 Stages)**:
  - `@set_colosseum_common` (Stage 1 Common Colosseum — sandstone/grey stone, amber wood-fire braziers, rising portcullis beast-gate).
- **Characters Used (3 of 10 Species, Tier 1 Common Only)**:
  - `@char_dragon_body` (Tier 1 Common Starter Dragon).
  - `@char_stego_body` (Tier 1 Common Starter Stegosaurus).
  - `@char_wolf_body` (Tier 1 Common Starter Dire Wolf).
- **Narrative Beats Used in V1**:
  - Aerial approach & dive into the Stage 1 Common Colosseum (`clip_01`, `clip_02`), followed by individual rookie introductions of the Common Dragon (`clip_03`), Common Stegosaurus (`clip_04`), and Common Dire Wolf + Trio Standoff (`clip_05`).
  - *(Note: V1 did NOT show what the game is actually about—breeding/genetics, training/mutation power-ups, combat clashes, or evolving up through the tiers into Special-Gene / Primal Apex champions!)*

### 🚀 Still on the Bench (Unused in V1 — Ready to Mine for V2!)
1. **The Core Gameplay & Power-Up Mechanics**:
   - **Genetic Breeding & Inheritance (`@set_breeding_lab`)**: Pairing two parents to pass down horns, claws, armour, wings, and recessive Special Genes into a newborn champion.
   - **The 4 Power-Up Transformations**:
     - *Training & Stat Surge*: Boosting `Power`, `Defence`, `Speed`, `Vitality`, and `Technique` up to genetic ceilings.
     - *15 Named Birth Mutations*: Erupting bigger `Heavy Horns`, `Razor Claws`, `Fortress Plates`, `Spring Tendons`, and `Titan Heart`.
     - *7-Tier Visual Evolution*: Upgrading the Starter Trio (or any of the 10 species) from **Tier 1 Common** → **Tier 2 Uncommon** → **Tier 3 Rare** → **Tier 4 Epic** → **Tier 5 Legendary** → **Tier 6 European Champion** → **Tier 7 World Primal Apex** (`dragon_primal.webp`, `stegosaurus_primal.webp`, `wolf_primal.webp`).
     - *The 4 Special Genes & 15 Hybrid/Apex Forms*:
       - Single Genes: **Mythic** (royal purple), **Colossus** (emerald crystal), **Ravager** (molten crimson), **Phantom** (electric ice-cyan).
       - 2-Gene Hybrids: **Astral Titan**, **Ember Wraith**, **Void Strider**, **Stoneblaze**, **Frostguard**, **Stormfire**.
       - 3-Gene Hybrids: **Celestial Guardian**, **Inferno Sovereign**, **Phantom Reaper**, **Titan Storm**.
       - Ultimate 4-Gene Sovereign: **Primal Apex (`primal_apex.webp`)** — obsidian armour surging with all 4 elemental energy streams at once.
2. **The Remaining 6 Power-Up Colosseum Arenas**:
   - Stage 2 Uncommon (`@set_colosseum_uncommon`), Stage 3 Rare (`@set_colosseum_rare`), Stage 4 Epic (`@set_colosseum_epic`), Stage 5 Legendary (`@set_colosseum_legendary`), Stage 6 European Champion (`@set_colosseum_champion`), and Stage 7 World Primal Apex Colosseum (`@set_colosseum_primal` — obsidian stadium with 4-colour elemental braziers and glowing floor runes).
3. **The Other 7 Base Creature Species (Across All 7 Tiers)**:
   - **Gorilla**, **Tiger**, **Rhino**, **T. Rex**, **Snake**, **Bird**, and **Triceratops**, plus the 11 `standard_art/` arena archetypes (`standard_scorcher`, `standard_stalker`, `standard_bulwark`, `standard_elite`, `standard_champion`, etc.).
4. **Live Arena Combat & League Climb**:
   - Head-to-head gladiator clashes, elemental shockwaves, knockout blows, climbing from Division 5 → Premier → European Championship → World Championship, and archiving eternal champions into the **Hall of Legends**.
