# Monster Stud — Vision, Ideas & Requirements Log

> **Purpose**: This is our living notepad for everything you talk about—raw ideas, feature tweaks, UI preferences, audio/video plans, and long-term thoughts. Nothing here gets built until you explicitly say to act on it.

---

## 1. Core Vision & Non-Negotiables
- **Source of Truth Game Engine**: [`game_source/v 2.0-MonsterStud_Tester_Edition_Fresh_Season_1_2026-11-07.html`](file:///c:/bgs/all%20myAssets/0myApps-All/Adams-Games/DragonCopper-app/Adams-Monsters-Ink%20app/game_source/v%202.0-MonsterStud_Tester_Edition_Fresh_Season_1_2026-11-07.html)
- **Visual Assets**: The 97 extracted `.webp` artworks in [`media_assets/extracted_art/`](file:///c:/bgs/all%20myAssets/0myApps-All/Adams-Games/DragonCopper-app/Adams-Monsters-Ink%20app/media_assets/extracted_art) are complete (no new monsters were added in later HTML updates).
- **Audio & Cinematics to Preserve**:
  - Suno arena-metal soundtrack ([`MP3-Trailer-Opt1-V3-30secs-Primal Apex.mp3`](file:///c:/bgs/all%20myAssets/0myApps-All/Adams-Games/DragonCopper-app/Adams-Monsters-Ink%20app/media_assets/soundtrack/MP3-Trailer-Opt1-V3-30secs-Primal%20Apex.mp3)).
  - Google Flow Intro & V1–V3 cutscene bibles/continuity trackers in [`cinematic_production/`](file:///c:/bgs/all%20myAssets/0myApps-All/Adams-Games/DragonCopper-app/Adams-Monsters-Ink%20app/cinematic_production).
- **Target Goal**: Native Android Game (`.apk` + future-proof structure).

---

## 2. Incoming User Thoughts & Brainstorming Log
*(As you share thoughts, I will log and organize them here by timestamp/topic without acting prematurely.)*

| ID | Status | Category | Note / Requirement |
| :--- | :--- | :--- | :--- |
| `IDEA-001` | 📌 Baseline | Workspace | Keep workspace clean; legacy files archived in `legacy_archive/`. |
| `IDEA-002` | ✅ Confirmed | Art Assets | Creator Adam confirmed no new monsters added. All 96 creature/archetype artworks in `media_assets/extracted_art` match the HTML dictionaries 1:1. |
| `IDEA-003` | ✅ Resolved | Art Assets | The post-video Title Screen image ("Click to start") was identified and saved as `media_assets/title_screen.webp` (543 KB). No re-extraction or scraping needed. |
| `IDEA-004` | 💡 Idea | Audio / Music | User added `MainGameMenu-background-track.mp3` to `media_assets/soundtrack/`. Plays on loop in the background across main game menus (subtle/low ambient volume, quietened down from original recording). Pauses or ducks when other specific audio/cutscenes trigger. |
| `IDEA-005` | 💡 Idea | Audio / Intro | Sound should be **enabled by default** when opening the game and playing the intro cutscene (with a toggle to mute), reversing the current HTML behavior which starts muted with an "Enable sound" button. (In Android WebView, this is solved natively via `setMediaPlaybackRequiresUserGesture(false)`). |
| `IDEA-006` | 🎯 Target Device | Hardware / Platform | **Primary Target Device: Samsung Galaxy S21 (Adam's phone)**. Specs baseline: 1080×2400 resolution (~20:9 aspect ratio), 120Hz dynamic AMOLED, Snapdragon 888 / Exynos 2100, 8GB RAM, Android 11–14/15. Optimize touch hitboxes, font legibility, smooth 60–120fps UI performance, and status bar / camera punch-hole safe areas specifically for this device profile first. |
| `IDEA-007` | 📱 Secondary Device | Hardware / Platform | **Secondary Test Device: Samsung Galaxy A71 (Your phone)**. Specs: 1080×2400 (~20:9 ratio, identical display resolution/aspect ratio to the S21), 6.7" Super AMOLED Plus 60Hz, Snapdragon 730, 6–8GB RAM, Android 10–13. Because both phones share the exact same 1080×2400 aspect ratio, UI layouts and scaling tuned for the S21 will naturally translate 1:1 to the A71, while the A71 ensures mid-range Snapdragon 730 performance remains silky smooth. |
| `IDEA-008` | 🌐 Tertiary Targets | Cross-Platform | **Unified Core (`web/`) for PC & Telegram Mini-App (Tertiary to Android APK)**: Structure the game as a clean, platform-agnostic `web/` core bundle so it first powers the primary Android APK (tuned for S21/A71), while remaining 100% ready to run on PC (browser or standalone desktop app) and deploy as a Telegram Channel Mini-App with near-zero extra work. |
| `IDEA-009` | ✅ Approved for Build | Branding / Home Screen | **App Icon & Label**: Label the installed Android app **`Monster Stud`** (fits cleanly under the icon on S21/A71 without `...` truncation). Confirmed using `primal_apex.webp` framed as the adaptive Android launcher icon. |
| `IDEA-010` | ✅ Approved for Build | Cutscenes / Combat | **Conditional V3 Mortal Kombat Finisher Cutscene**: Using `media_assets/video_clips/Monster_Stud_Battle_Scene_01-v3_20261107223758.mp4` (preserving the full 34s original file untouched!). When a Common Dire Wolf (player) defeats a Common War Rhino (opponent): play **Exchange 1** (Rhino wins exchange) and **Exchange 2** (Wolf comeback) in the 2D arena, then for **Exchange 3** seamlessly cut to the **final 16 seconds (`0:18–0:34`)** of the V3 video (`video.currentTime = 18`) showing the Ravager awakening and *"Hellfang Spine-Breaker"* K.O. fatality. |
| `IDEA-011` | ✅ Approved for Build | Mobile UX / Layout | **Orientation & Navigation**: Default to Portrait mode for comfortable one-handed S21/A71 play (while allowing smooth auto-rotation to Landscape for wide tables/combat if the user rotates their phone), and replace the 3-row wrapping top tabs on mobile viewports with a sleek, thumb-friendly sticky navigation bar/strip. |
| `IDEA-012` | ✅ Approved for Build | Branding & Saves | **Production Identity & Cross-Device Backup**: Remove `"Tester Edition"` branding so the title reads **`Monster Stud — Genetic League`**, use a permanent production save key, and ensure the JSON **"Save / Download Backup"** and **"Load Backup"** buttons work natively on Android so Adam can transfer careers between PC and his S21. |
| `IDEA-013` | ✅ Approved for Build | Native Game Feel | **Tactile Haptics & Screen Wake**: Add subtle native haptic vibration ticks on arena combat collisions, K.O. finishes, and Genesis Core rare gene awakenings, and keep the screen awake (`FLAG_KEEP_SCREEN_ON` / WakeLock) during video playback and full-season auto-simulations. |
| `IDEA-014` | 💡 Audited / Confirmed | Save Persistence Across 3 Builds | **Cross-Platform Save Persistence**: Audited and confirmed that career progress (`localStorage` + `monsterStudCareerSaveV1`) persists automatically across all 3 platforms: (1) Windows Desktop EXE (`%LOCALAPPDATA%\DragonCopper\MonsterStud\`), (2) Android APK (`/data/data/com.dragoncopper.monsterstud/` with AndroidBridge file backup), and (3) Telegram Mini App / GitHub Pages (HTTPS origin storage + optional `Telegram.WebApp.CloudStorage`). Confirmed decision to skip PC emulator in favor of direct testing on real hardware (A71/S21) to save tokens and prevent CPU stalls. |

---

## 3. Open Questions & Parking Lot
- `Q-004` (Future Polish): When reopening the game with an existing save, should the app offer an instant "Resume Career" bypass on the title screen so players don't need to watch/skip the opening video every time?
