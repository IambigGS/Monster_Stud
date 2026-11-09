# Monster Stud — Step-by-Step Build Blueprint & Guardrails

> **CRITICAL RULES FOR ANY AGENT / MODEL EXECUTING THIS BUILD**:
> 1. **NEVER delete, overwrite, or trim original files in `game_source/` or `media_assets/`.** Always copy or reference them into the build directory (`web/` and `android/`).
> 2. **NEVER re-extract the 96 creature/archetype `.webp` images from the HTML base64.** They already exist 1:1 on disk inside `media_assets/extracted_art/` (`all_species_tiers/`, `special_genes/`, `standard_art/`, `arena/`) and `media_assets/title_screen.webp`. Simply map the JS dictionaries (`GENE_ART_ASSETS`, `STANDARD_ART_ASSETS`, `SPECIES_TIER_ASSETS`) to load the local `.webp` paths!
> 3. **NEVER trim or re-encode `media_assets/video_clips/Monster_Stud_Battle_Scene_01-v3_20261107223758.mp4`.** Keep the full 34-second file intact and use `video.currentTime = 18.0` in JS for the Exchange 3 finisher.
> 4. **Preserve 100% of Adam's core game math, genetics, 35 loci, league rules, Cup rules, and RPS/scouting formulas.** Only enhance the asset loading, audio/video hooks, mobile UX, and native Android bridge.

---

## Phase 1: Unpack the Unified `web/` Core (Zero-Bloat Bundle)
1. Create a clean `web/` directory that will serve Android APK (`src/main/assets/web/`), PC browser/desktop, and Telegram Mini-App.
2. **Extract the Opening Video Once**:
   - Decode `MONSTER_STUD_OPENING_VIDEO_BASE64` (Line 6855 of `game_source/v 2.0-MonsterStud_Tester_Edition_Fresh_Season_1_2026-11-07.html`) into a single file: `media_assets/video_clips/opening_intro.mp4` (and copy to `web/assets/video/opening_intro.mp4`).
3. **Wire Existing Art Assets Directly (No Re-Extraction)**:
   - Copy `media_assets/extracted_art/*`, `media_assets/title_screen.webp`, `media_assets/soundtrack/*`, and `media_assets/video_clips/*` into `web/assets/`.
   - Replace the massive inline base64 strings in `web/index.html` (`Line 533` arena bg, `Line 1911` title screen img, `Line 2680` `GENE_ART_ASSETS`, `Line 2682` `STANDARD_ART_ASSETS`, `Line 2684` `SPECIES_TIER_ASSETS`, `Line 6855` `MONSTER_STUD_OPENING_VIDEO_BASE64`) with clean relative file paths (`assets/art/...`, `assets/video/...`).
   - Result: `index.html` drops from **13.4 MB to ~400 KB** and boots instantaneously.

---

## Phase 2: Audio, Video & Conditional V3 Mortal Kombat Finisher
1. **Intro Video Unmuted by Default (`IDEA-005` / `TECH-007`)**:
   - In `setupMonsterStudVideoIntro()`, start `<video id="gameOpeningVideo" src="assets/video/opening_intro.mp4">` with `video.muted = false` by default and change the button label to `🔊 Sound On` / `🔇 Mute`.
   - In Android `MainActivity.kt`, set `webView.settings.mediaPlaybackRequiresUserGesture = false` so unmuted playback works from frame 1.
2. **Ambient Main Menu Soundtrack (`IDEA-004` / `DEC-004`)**:
   - Load `assets/soundtrack/MainGameMenu-background-track.mp3` as a looping `<audio>` instance (`volume = 0.25`).
   - Start playing as soon as the user clicks past the Title Screen (`#gameIntroScreen`) into the main game.
   - **Auto-Ducking**: Pause or duck (`volume = 0.05`) when a combat animation or video cutscene plays; smoothly restore to `0.25` when returning to menus. Add a compact BGM toggle pill in the header.
3. **Conditional V3 Mortal Kombat Finisher (`IDEA-010` / `DEC-004`)**:
   - In `playPlayerCombatAnimation()` (Lines 5430–5566), detect the exact condition:
     - `speciesKeyForMonster(leftMonster) === 'wolf'` AND `rarityLabel(leftMonster) === 'Common'`
     - `speciesKeyForMonster(rightMonster) === 'rhino'` AND `rarityLabel(rightMonster) === 'Common'`
     - `leftWins === true` (Player's Dire Wolf wins the bout)
   - When true:
     - **Exchange 1 (`FIRST CLASH`)**: 2D Arena shows the War Rhino winning the opening exchange (Wolf takes the heavier hit).
     - **Exchange 2 (`TURNING POINT`)**: 2D Arena shows the Dire Wolf roaring back with a counter-strike (Rhino takes the heavier hit and staggers).
     - **Exchange 3 (`FINISHING BLOW — HELLFANG SPINE-BREAKER`)**: Instead of standard 2D stage-3 shake, open the inline/overlay video player loading `assets/video/Monster_Stud_Battle_Scene_01-v3_20261107223758.mp4` at **`video.currentTime = 18.0`**, playing the final 16 seconds (`0:18–0:34`: Ravager bloodline awakening + corkscrew crater slam K.O. fatality), then reveal the Victory card!

---

## Phase 3: Samsung Galaxy S21 / A71 Mobile UX & Production Polish
1. **Production Identity & Save Key (`IDEA-012` / `DEC-005`)**:
   - Update document `<title>` and metadata from `"Monster Stud — Tester Edition (Fresh Start)"` to **`Monster Stud — Genetic League`**.
   - Use production save key `SAVE_KEY = "monsterStudCareerSaveV1"` with fallback migration from `"monsterStudTesterCareerSaveV1"`.
   - Remove the localhost `127.0.0.1:8765` warning check (`isPermanentSaveOrigin()`) when running in the app/unified build.
2. **S21 / A71 Viewport (1080×2400, 20:9) & Sticky Navigation (`IDEA-011` / `DEC-003`)**:
   - Respect safe-area insets (`env(safe-area-inset-top)`, `env(safe-area-inset-bottom)`) for the S21/A71 top camera punch-hole and bottom gesture bar.
   - On mobile viewports (`@media (max-width: 768px)`), style `<nav class="tabs">` as a sleek, thumb-friendly bottom/sticky horizontal navigation bar instead of wrapping into 3 tall rows at the top.
3. **Touch-Friendly Gene Tooltips & No Native `alert()`/`prompt()` (`TECH-002`, `TECH-003`)**:
   - In `setupGlobalGeneHoverTooltips()` (Line 7060), allow tap-to-toggle on touchscreens (`pointerType === 'touch'`) so tapping any `.gene-tag` or `.portrait-gene-mark` shows the gene popup cleanly, and tapping elsewhere dismisses it.
   - Replace remaining `alert()` calls in `leagueFight()` and `prompt()` in `renameStable()` with styled in-game modals (`showGameDialog`).

---

## Phase 4: Native Android APK Packaging (`android/`)
1. **Android Project Configuration**:
   - App Name: **`Monster Stud`**
   - Package ID: `com.dragoncopper.monsterstud`
   - Launcher Icon: Generated adaptive & round icons from `media_assets/extracted_art/special_genes/primal_apex.webp`.
   - Orientation: `fullSensor` (defaults cleanly to Portrait for one-handed S21 play, rotates smoothly to Landscape when the phone is turned sideways).
2. **Native Bridge & Hardware Features (`IDEA-013`, `TECH-006`)**:
   - Hardware Back Button: Calls JS hook to close open overlays/modals first, or switch back to `My Stable` tab, before prompting to exit.
   - Native Haptics (`AndroidBridge.vibrate(ms)`): Subtle haptic feedback on combat hits, K.O. slam, and Genesis Core discoveries.
   - Screen Wake (`keepScreenOn = true`): Keeps screen awake during intro video and full-season simulations.
   - Native Save Backup Export / Import: Bridges `"Save / Download Backup"` and `"Load Backup"` buttons to Android's native file picker / share sheet, plus mirrors `localStorage` saves to internal app storage (`filesDir/save_backup.json`).
3. **Build & Verify `.apk`**:
   - Compile standalone installable `.apk` (`MonsterStud-S21-Release.apk`) ready to install on Adam's Samsung Galaxy S21 and your Samsung Galaxy A71.
