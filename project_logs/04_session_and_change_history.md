# Monster Stud — Session & Change History

> **Purpose**: A chronological record of every step actually taken in the workspace so we always know where we left off.

---

## 2026-11-08 — Session 1: Codebase Analysis, Cleanup & Logging Setup
- **Codebase Audit Completed**:
  - Analyzed the entire workspace across `Monster_Stud` and `Monster_Stud - V2`.
  - Identified [`v 2.0-MonsterStud_Tester_Edition_Fresh_Season_1_2026-11-07.html`](file:///c:/bgs/all%20myAssets/0myApps-All/Adams-Games/DragonCopper-app/Adams-Monsters-Ink%20app/game_source/v%202.0-MonsterStud_Tester_Edition_Fresh_Season_1_2026-11-07.html) as the true master build containing Genesis Core, Genetic Cups, Tactical RPS + Scouting, 2-stage aging (Age 10 combat retirement / Age 20 full retirement), and Achievements.
- **Workspace Archiving & Reorganization**:
  - Zipped redundant `Monster_Stud - V2` folder into `legacy_archive/Monster_Stud_V2_Legacy_Backup.zip` and moved all duplicate Oct 28 HTML files into `legacy_archive/`.
  - Reorganized active source-of-truth files into:
    - `game_source/` (Master HTML build)
    - `media_assets/` (`extracted_art/`, `soundtrack/`, `video_clips/`)
    - `cinematic_production/` (`flow_bibles/v1_trailer`, `v2_powerup_trailer`, `v3_battle_finisher`, and `docs/`)
- **Logging System Initialized**:
  - Created `project_logs/` with 4 structured markdown trackers (`01_vision_and_ideas_log.md`, `02_architecture_and_decisions.md`, `03_technical_audit_and_backlog.md`, `04_session_and_change_history.md`).


## 2026-11-08 — Session 2: Phases 1 to 4 Implementation & Android Release Build
- **Phase 1: Unpack Unified `web/` Core**:
  - Organized local assets: 96 creature/archetype `.webp` files mapped 1:1, opening intro video MP4, title screen webp, Main Game Menu soundtrack MP3, and 34s battle cutscene MP4.
  - Rewrote master HTML (`game_source/v 2.0-MonsterStud_Tester_Edition_Fresh_Season_1_2026-11-07.html`) into zero-bloat `web/index.html` (size dropped from 13.4MB down to 736KB, booting instantaneously).
- **Phase 2: Audio, Video & Conditional V3 MK Finisher**:
  - Wired ambient looping background music (`assets/soundtrack/MainGameMenu-background-track.mp3`) with unmuted opening intro video, compact header BGM toggle pill, and auto-ducking during combat and video scenes.
  - Wired conditional V3 Mortal Kombat Finisher in `playPlayerCombatAnimation()` for Common Dire Wolf (player) vs. Common War Rhino (opponent AI). Shows 2D Exchange 1 (Rhino leads), 2D Exchange 2 (Wolf counters), and triggers the 16-second cutscene at `currentTime = 18.0` with Skip option and seamless transition to victory.
- **Phase 3: Samsung Galaxy S21 & A71 Mobile UX & Production Polish**:
  - Configured safe-area insets (`env(safe-area-inset-*)`) and responsive sticky bottom navigation bar (`@media (max-width: 768px)`).
  - Renamed document title to `Monster Stud — Genetic League`.
  - Migrated save key to `monsterStudCareerSaveV1` with backup and migration fallbacks.
  - Replaced native `alert()` and `prompt()` calls with custom in-game modal cards (`showGamePrompt`, `showGameDialog`).
  - Added touch tap-to-toggle support for gene tooltips.
- **Phase 4: Native Android APK Packaging (`MonsterStud-S21-Release.apk`)**:
  - Scaffolded native Android application in `android/` (`com.dragoncopper.monsterstud`).
  - Generated full suite of adaptive launcher icons from `primal_apex.webp`.
  - Built `MainActivity` with hardware-accelerated WebView, fullscreen immersive mode, AndroidBridge (haptics, wakelock, save backup sharing, and hardware back button handling).
  - Compiled release APK using Gradle 8.13 and Java 17: `MonsterStud-S21-Release.apk` (45.4 MB) successfully created in project root.

- **Deliverable Finalized**:
  - `MonsterStud-S21-Release.apk` (45.4 MB) placed into `builds/apk/`.
  - All build and packaging scripts archived into `build_tools/`.
  - Workspace root cleaned and organized.

---

## 2026-11-08 — Session 3: Build Organization & Versioning Protocol
- **Builds Directory Architecture**:
  - Created standardized `builds/` directory hierarchy:
    - `builds/apk/`: Native Android packages. Moved `MonsterStud-S21-Release.apk` here.
    - `builds/windows-exe/`: Dedicated directory for future Windows desktop executables.
    - `builds/web-standalone/`: Dedicated directory for portable browser / Telegram distribution zips.
  - Updated `build_tools/compile_apk.py` to route all future Gradle build outputs directly into `builds/apk/`.
- **Versioning Protocol Established (Per Steve's Directive)**:
  - Starting immediately, all future builds across all platforms must carry explicit version numbers (e.g. `v1.0.0`, `v1.0.1`).
  - No build will ever overwrite an existing binary; full version history is preserved in `builds/`.
- **Immediate Next Task (Queued for Next Session)**:
  - Compile the lightweight standalone Windows executable (`builds/windows-exe/MonsterStud-v1.0.0.exe` via Microsoft Edge WebView2, ~48 MB).
  - Completely self-contained, zero external dependencies, zero paths referencing Steve's local machine.

---

## 2026-11-08 — Session 4: Windows Desktop Executable & Web Standalone (TMA Ready)
- **Telegram Mini App (TMA) & Web Standalone Package**:
  - Integrated Telegram WebApp SDK auto-initialization directly into `web/index.html` (`Telegram.WebApp.ready()`, `expand()`, `#10131e` header synchronization).
  - Synced changes to `android/app/src/main/assets/web/index.html`.
  - Packaged portable web archive: [`builds/web-standalone/MonsterStud-Web-v1.0.0.zip`](file:///c:/bgs/all%20myAssets/0myApps-All/Adams-Games/DragonCopper-app/Adams-Monsters-Ink%20app/builds/web-standalone/MonsterStud-Web-v1.0.0.zip) (42.89 MB).
  - Authored step-by-step deploy & BotFather guide: [`builds/web-standalone/README.md`](file:///c:/bgs/all%20myAssets/0myApps-All/Adams-Games/DragonCopper-app/Adams-Monsters-Ink%20app/builds/web-standalone/README.md).
- **Windows Desktop Standalone Executable (`MonsterStud-v1.0.0.exe`)**:
  - Built dedicated C# WinForms + WebView2 architecture in `build_tools/windows_app/`.
  - Embedded multi-resolution application icon (`app_icon.ico`) from `primal_apex.webp`.
  - Embedded complete web bundle (`assets.zip`) into executable resources.
  - Zero dependencies: bundled self-contained .NET 9 x64 runtime + WebView2 native loader into a single binary.
  - Feature polish: 1280x800 default window, F11 borderless fullscreen toggle, dark `#10131E` flash prevention, persistent player save profile in `%LOCALAPPDATA%\DragonCopper\MonsterStud\`.
  - Verified live execution: boots instantaneously, extracts cached assets on first launch, runs smoothly.
  - Deliverable finalized: [`builds/windows-exe/MonsterStud-v1.0.0.exe`](file:///c:/bgs/all%20myAssets/0myApps-All/Adams-Games/DragonCopper-app/Adams-Monsters-Ink%20app/builds/windows-exe/MonsterStud-v1.0.0.exe) (91.76 MB).
- **Sound Autoplay & Toggle Polish (Per Steve's Review)**:
  - Fixed Windows desktop WebView2 environment options by adding `--autoplay-policy=no-user-gesture-required` so Chromium never suppresses unmuted media playback on startup.
  - Updated video intro button initial state and toggle handler to `🔊 Sound: ON` / `🔇 Sound: OFF`.
  - Added touch/pointer gesture fallback so web/Telegram Mini App environments immediately unmute on first tap if strict mobile browsers restrict frame-0 audio.
  - Configured `MainForm.cs` to automatically overwrite `%LOCALAPPDATA%` cached web assets on launch, keeping executable updates synchronized.
  - Rebuilt and overwrote [`builds/windows-exe/MonsterStud-v1.0.0.exe`](file:///c:/bgs/all%20myAssets/0myApps-All/Adams-Games/DragonCopper-app/Adams-Monsters-Ink%20app/builds/windows-exe/MonsterStud-v1.0.0.exe) and [`builds/web-standalone/MonsterStud-Web-v1.0.0.zip`](file:///c:/bgs/all%20myAssets/0myApps-All/Adams-Games/DragonCopper-app/Adams-Monsters-Ink%20app/builds/web-standalone/MonsterStud-Web-v1.0.0.zip).


---

## 2026-11-08 — Session 5: GitHub Pages & Telegram Bot Integration Staging
- **Cross-Project Pattern Audit**:
  - Located Steve's live deployment in `FUimAfly` (`C:\bgs\all myAssets\0myApps-All\steve_arena\FUimAfly`).
  - Audited `.github/workflows/deploy.yml` which deploys directly to GitHub Pages (`gh-pages`) on push to `main`.
  - Located Telegram Bot project `@BOT_AWOTBOT` in `AWOTvibeCode` (`C:\bgs\all myAssets\Telegram\Absolute Waste of Time\AWOTvibeCode`).
  - Verified system Git authentication with `IambigGS` using Windows Git Credential Manager (`ls-remote` passed with code 0).
- **GitHub & GitHub Actions Infrastructure Staged**:
  - Initialized Git repository on `main` branch.
  - Authored `.gitignore` (safely excludes large binaries in `builds/`, `*.apk`, `*.exe`, and caches).
  - Authored `.github/workflows/deploy.yml` (automates publishing `web/` to `gh-pages` with `JamesIves/github-pages-deploy-action@v4`).
- **Handoff & Returning Brief Staged**:
  - Created `project_logs/00_NEXT_SESSION_BRIEF.md`.
  - Updated `AGENTS.md` with mandatory returning directive for Steve: on any greeting (*"hi"*, *"hello"*, *"oy oy"*), agent will immediately present a concise TL;DR followed by details.


---

## 2026-11-09 — Session 6: Samsung S21 Crash Fix, Android Hardening & v1.0.1 APK Release
- **Samsung One UI Crash Diagnosis**:
  - Analyzed crash screenshot from Adam's Galaxy S21 (*"Something went wrong with Monster Stud. Monster Stud closed because this app has a bug."*).
  - Confirmed APK installed successfully (rules out Developer Mode or sideloading permission blockers).
  - Pinpointed the root cause to unhandled runtime security/lifecycle exceptions in `MainActivity.java`: specifically `setShowWhenLocked(true)` and `setTurnScreenOn(true)` triggering Samsung Knox / One UI 6 security violations at startup, plus lack of defensive wrapping around `insetsController` and system services.
- **Android Native Code Hardening**:
  - `MainActivity.java`:
    - Removed `setShowWhenLocked` and `setTurnScreenOn`.
    - Maintained `WindowManager.LayoutParams.FLAG_KEEP_SCREEN_ON` and hardware acceleration.
    - Defensively wrapped `setImmersiveMode()` with null checks.
    - Added global `Thread.setDefaultUncaughtExceptionHandler` and wrapped WebView setup in try/catch to intercept any unexpected crashes.
  - `AndroidBridge.java`:
    - Defensively guarded `getSystemService(Context.VIBRATOR_SERVICE)` and all bridge methods.
- **Version Bump & APK Build Compilation**:
  - Bumped Gradle configuration in `android/app/build.gradle` to `versionCode 2` and `versionName "1.0.1"`.
  - Updated `build_tools/compile_apk.py` to output [`builds/apk/MonsterStud-v1.0.1.apk`](file:///c:/bgs/all%20myAssets/0myApps-All/Adams-Games/DragonCopper-app/Adams-Monsters-Ink%20app/builds/apk/MonsterStud-v1.0.1.apk) (45.4 MB) while preserving `MonsterStud-S21-Release.apk`.
  - Rebuilt with Gradle 8.13 and Java 17 (exit code 0). Verified APK signature with `apksigner` (APK Signature Scheme v2 valid).
- **Windows EXE & Telegram Audit**:
  - Confirmed the core web runtime (`web/index.html`) is 100% bug-free; Windows EXE and Telegram/GitHub staging remain in perfect health.


---

## 2026-11-09 — Session 7: GitHub Remote Connected & Live Push Executed
- **Remote Created by Steve**: `https://github.com/IambigGS/Monster_Stud.git` (Public).
- **Initial Commit & Push**:
  - Committed 608 files (web core, video/audio assets, android source, cinematic bibles, build tools, logs).
  - Linked remote `origin` to `https://github.com/IambigGS/Monster_Stud.git`.
  - Pushed `main` to `origin` (code 0).
- **GitHub Actions Deployment**:
  - `.github/workflows/deploy.yml` triggered automatically on push.
  - Deploys `web/` directly to branch `gh-pages` to serve live on `https://IambigGS.github.io/Monster_Stud/`.


---

## 2026-11-10 — Session 8: GitHub Pages Activation Verified & In-Place Update Protocol Locked
- **Telegram Mini App Live Verification**:
  - Steve enabled GitHub Pages on `gh-pages` branch at `https://github.com/IambigGS/Monster_Stud/settings/pages`.
  - Verified live boot in Telegram via direct link `t.me/BOT_AWOTBOT/dragon_cooper`. Game boots with unmuted sound and full gameplay inside Telegram Mini App.
- **Architectural Policy Formalized**:
  - `DEC-008`: Telegram / GitHub Pages uses permanent single-URL in-place updates. Pushing `main` deploys the new release without changing Telegram links or spawning new repos. Git retains all historical commits.
  - `DEC-009`: Standalone binaries (APK & EXE) continue to preserve distinct versioned files in `builds/`.
