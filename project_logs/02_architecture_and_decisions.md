# Monster Stud — Architecture & Decisions Log (ADR)

> **Purpose**: Tracks every confirmed technical, design, and gameplay decision we lock in, along with why we chose it and what we ruled out.

---

## Confirmed Decisions

### `DEC-001` — Single Source of Truth & Clean Directory Layout (2026-11-08)
- **Status**: ✅ Locked In & Implemented
- **Decision**: Use `v 2.0-MonsterStud_Tester_Edition_Fresh_Season_1_2026-11-07.html` as the sole master HTML build. Segregate all October duplicates and `Monster_Stud - V2` into `legacy_archive/`. Organize active project into `game_source/`, `media_assets/`, `cinematic_production/`, and `project_logs/`.
- **Why**: Prevents version confusion and accidental edits to outdated files.

### `DEC-006` — Primary Target Device Baseline: Samsung Galaxy S21 (2026-11-08)
- **Status**: ✅ Locked In
- **Decision**: Design, scale, and test the APK targeting the **Samsung Galaxy S21** as the reference standard (Android 11–14+, 1080×2400 resolution, ~20:9 ratio, top camera punch-hole), with the **Samsung Galaxy A71** (same 1080×2400 20:9 resolution) as secondary test device.
- **Why**: Ensures the game feels like a flawless, tailored handheld console experience on Adam's exact daily phone and yours, while standard Android responsive scaling ensures it runs cleanly across other modern phones.

### `DEC-007` — Unified Cross-Platform Core (`web/`) for Android APK + PC + Telegram Mini-App (2026-11-08)
- **Status**: ✅ Locked In
- **Decision**: Maintain a single, clean `web/` game core that is packaged into the native Android APK first, while preserving desktop responsiveness (for PC play) and lightweight compatibility for future deployment as a Telegram Channel Mini-App.
- **Why**: Avoids maintaining separate codebases; gives us fast PC testing during development and effortless Telegram Mini-App support later at zero extra cost.

### `DEC-003` — Mobile Orientation & Navigation Bar (2026-11-08)
- **Status**: ✅ Locked In
- **Decision**: Use `fullSensor` / unlocked orientation (defaulting naturally to Portrait for one-handed management, while supporting Landscape when rotated) and convert the 9 navigation tabs on mobile screens into a sleek, thumb-accessible horizontal swipe/bottom navigation bar so it never wraps into 3 tall rows at the top of the S21 screen.
- **Why**: Best of both worlds for gameplay and UX—one-handed comfort in Portrait with full widescreen visibility when rotated, plus maximum vertical screen space.

### `DEC-004` — Audio & Conditional Cutscene Architecture (2026-11-08)
- **Status**: ✅ Locked In
- **Decision**:
  1. **Intro Video**: Starts **unmuted by default** on launch (`setMediaPlaybackRequiresUserGesture(false)`), with a Mute toggle button.
  2. **Main Menu BGM**: `MainGameMenu-background-track.mp3` loops quietly in the background (~25% volume) across menu tabs, automatically ducking/pausing when videos or combat sequences play.
  3. **Conditional V3 Mortal Kombat Finisher Cutscene**: When a **Common Dire Wolf** (Player) defeats a **Common War Rhino** (Opponent), **Exchange 1** (Rhino wins exchange) and **Exchange 2** (Wolf comeback) play in the 2D arena, and **Exchange 3** seamlessly transitions into the **final 16 seconds (`0:18–0:34`)** of [`Monster_Stud_Battle_Scene_01-v3_20261107223758.mp4`](file:///c:/bgs/all%20myAssets/0myApps-All/Adams-Games/DragonCopper-app/Adams-Monsters-Ink%20app/media_assets/video_clips/Monster_Stud_Battle_Scene_01-v3_20261107223758.mp4) using HTML5 video timecode seeking (`video.currentTime = 18.0`) so the full 34-second original `.mp4` file remains 100% untouched on disk.
- **Why**: Preserves the exact narrative choreography of the V3 cutscene (*"Hellfang Spine-Breaker"*) so it feels like an authentic, jaw-dropping special event rather than a generic clip that doesn't match the fighters on screen.

### `DEC-005` — Production Title, Save Persistence & Portable JSON Backups (2026-11-08)
- **Status**: ✅ Locked In
- **Decision**: Strip `"Tester Edition"` branding in favor of **`Monster Stud — Genetic League`** (launcher label: **`Monster Stud`**, icon: `primal_apex.webp`). Use dual save persistence (`localStorage` + native Android file mirror) and bridge the `"Save / Download Backup"` and `"Load Backup"` buttons to Android's native file picker / share sheet.
- **Why**: Protects career progress from accidental OS cache clearing and lets Adam move his save file between PC and his Galaxy S21 effortlessly.

---

## Pending Decisions (To Discuss When Ready)
- **`DEC-002` (Pending)**: Android Packaging Toolchain (Native Android Gradle WebView wrapper vs. Capacitor—will select whichever compiles cleanest locally).
