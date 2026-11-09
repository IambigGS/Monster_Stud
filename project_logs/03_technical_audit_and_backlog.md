# Monster Stud — Technical Audit & Android Backlog

> **Purpose**: Tracks technical findings from the codebase analysis and the concrete engineering tasks we will eventually tackle when building the Android app. Nothing here is executed until approved.

---

## Technical Findings from Master Build (`V4-Adam`)

| ID | Area | Finding | Planned Android Resolution (When Ready) | Status |
| :--- | :--- | :--- | :--- | :--- |
| `TECH-001` | Performance & RAM | HTML file was **13.4 MB** because `MONSTER_STUD_OPENING_VIDEO_BASE64` and artworks were base64 strings. | Extracted video, audio, and `.webp` files to native local assets. `web/index.html` reduced to 724 KB. | ✅ Completed |
| `TECH-002` | Touch UX | `setupGlobalGeneHoverTooltips()` explicitly ignored touch. | Added tap-to-toggle support on `.gene-tag` and `.portrait-gene-mark` for mobile touchscreens. | ✅ Completed |
| `TECH-003` | Native Dialogs | A few actions called browser `prompt()` or `alert()`. | Replaced native browser alerts/prompts with custom in-game modal cards (`showGamePrompt`, `showGameDialog`). | ✅ Completed |
| `TECH-004` | Save System | Used `monsterStudTesterCareerSaveV1` and checked localhost origin. | Switched to permanent `monsterStudCareerSaveV1` save key with backup fallbacks and AndroidBridge sharing. | ✅ Completed |
| `TECH-005` | Mobile Layout | Desktop layout needed safe area insets and mobile navigation for Samsung S21 / A71. | Added `viewport-fit=cover`, CSS `env(safe-area-inset-*)`, and sleek sticky bottom mobile navbar. | ✅ Completed |
| `TECH-006` | Hardware Back Button | Pressing Back on Android WebView by default exited the app. | Hooked AndroidBridge back button to dismiss modals/overlays before exiting. | ✅ Completed |
| `TECH-007` | Intro Audio Autoplay | HTML started video muted with "Enable sound" button. | Added unmuted autoplay with dedicated sound toggles and background soundtrack ducking. | ✅ Completed |
| `TECH-008` | Windows Desktop Standalone | Need a standalone Windows desktop executable that requires zero external dependencies, no local machine references, and minimal download size. | Packaged `web/` into a lightweight native Windows WebView2 single-file executable (`builds/windows-exe/MonsterStud-v1.0.0.exe`, 91.7 MB self-contained). | ✅ Completed |
| `TECH-009` | Telegram Mini App (TMA) & Web Standalone | Need a portable web zip and Telegram WebApp SDK support for group chat bot integration. | Packaged `builds/web-standalone/MonsterStud-Web-v1.0.0.zip` (42.8 MB) with Telegram WebApp SDK auto-init and full deploy documentation. | ✅ Completed |
| `TECH-010` | Samsung S21 Startup Crash | `MainActivity.java` threw unhandled runtime security exceptions on Samsung One UI 6 (Knox) due to `setShowWhenLocked(true)` and `setTurnScreenOn(true)`. | Removed screen-waking/lockscreen calls, defensively guarded `setImmersiveMode()`, added global uncaught exception interceptor, and compiled `v1.0.1` APK (`versionCode 2`). | ✅ Completed |
