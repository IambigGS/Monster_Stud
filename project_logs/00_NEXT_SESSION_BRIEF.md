# Monster Stud — Next Session Brief & Handoff

> **To any Agent greeting Steve**:
> Whenever Steve returns and says *"hi"*, *"hello"*, *"oy oy"*, or similar, greet him warmly and start your response with the **TL;DR** below, followed by the **Details & Next Steps**.

---

## TL;DR
Monster Stud has been committed and pushed live to GitHub (`https://github.com/IambigGS/Monster_Stud.git`). The GitHub Actions workflow (`deploy.yml`) is publishing `web/` to the `gh-pages` branch, serving the game at `https://IambigGS.github.io/Monster_Stud/`. The Android APK `v1.0.1` (with the Samsung S21 crash fix) and Windows standalone EXE `v1.0.0` (with unmuted sound) are built and ready. All that remains is connecting the live GitHub Pages URL to `@BOT_AWOTBOT` in Telegram!

---

## Details & Next Steps

### 1. Live Infrastructure & Deliverables
- **GitHub Repository**: [github.com/IambigGS/Monster_Stud](https://github.com/IambigGS/Monster_Stud)
- **Live Web / Telegram Mini App URL**: `https://IambigGS.github.io/Monster_Stud/`
- **Native Android APK v1.0.1**: [`builds/apk/MonsterStud-v1.0.1.apk`](file:///c:/bgs/all%20myAssets/0myApps-All/Adams-Games/DragonCopper-app/Adams-Monsters-Ink%20app/builds/apk/MonsterStud-v1.0.1.apk) (45.4 MB, Samsung One UI 6 / S21 crash fix active).
- **Standalone Windows EXE**: [`builds/windows-exe/MonsterStud-v1.0.0.exe`](file:///c:/bgs/all%20myAssets/0myApps-All/Adams-Games/DragonCopper-app/Adams-Monsters-Ink%20app/builds/windows-exe/MonsterStud-v1.0.0.exe) (91.7 MB, unmuted autoplay flag active).
- **Web Standalone Bundle**: [`builds/web-standalone/MonsterStud-Web-v1.0.0.zip`](file:///c:/bgs/all%20myAssets/0myApps-All/Adams-Games/DragonCopper-app/Adams-Monsters-Ink%20app/builds/web-standalone/MonsterStud-Web-v1.0.0.zip).

---

### 2. Immediate Next Step: Connect to Telegram Bot
1. In BotFather on Telegram:
   - Run `/mybots` $\rightarrow$ Select `@BOT_AWOTBOT`
   - Go to **Bot Settings** $\rightarrow$ **Menu Button** (or `/newapp`)
   - Set the Mini App URL to:
     `https://IambigGS.github.io/Monster_Stud/`
2. Test opening the bot in Telegram on your phone or PC!
