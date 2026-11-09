# -*- coding: utf-8 -*-
"""
Script to apply Phase 2 & Phase 3 updates to web/index.html cleanly with UTF-8 encoding.
"""
import re
import sys

def main():
    path = "web/index.html"
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    print(f"Original length: {len(content)} chars")

    # 1. Update Title and Viewport
    content = content.replace(
        '<meta name="viewport" content="width=device-width, initial-scale=1.0">',
        '<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover, user-scalable=no">'
    )
    content = content.replace(
        '<title>Monster Stud - Tester Edition (Fresh Start)</title>',
        '<title>Monster Stud — Genetic League</title>'
    )

    # 2. Add Mobile Safe Area & Bottom Tab Navigation CSS
    mobile_css = """
/* S21 / A71 Safe Area & Mobile Bottom Navigation */
body {
  padding-top: env(safe-area-inset-top, 0px);
  padding-bottom: env(safe-area-inset-bottom, 0px);
  padding-left: env(safe-area-inset-left, 0px);
  padding-right: env(safe-area-inset-right, 0px);
}
@media (max-width: 768px) {
  .tabs {
    position: fixed !important;
    bottom: 0 !important;
    left: 0 !important;
    right: 0 !important;
    z-index: 9999 !important;
    margin: 0 !important;
    padding: 8px 10px calc(8px + env(safe-area-inset-bottom, 0px)) !important;
    background: rgba(14, 19, 32, 0.96) !important;
    backdrop-filter: blur(12px) !important;
    -webkit-backdrop-filter: blur(12px) !important;
    border-top: 1px solid #3b4560 !important;
    display: flex !important;
    flex-wrap: nowrap !important;
    overflow-x: auto !important;
    -webkit-overflow-scrolling: touch !important;
    gap: 8px !important;
    box-shadow: 0 -4px 16px rgba(0,0,0,0.5) !important;
  }
  .tabs::-webkit-scrollbar { display: none; }
  .tabs { -ms-overflow-style: none; scrollbar-width: none; }
  .tab {
    flex: 0 0 auto !important;
    font-size: 13px !important;
    padding: 9px 13px !important;
    white-space: nowrap !important;
  }
  main {
    padding-bottom: calc(75px + env(safe-area-inset-bottom, 0px)) !important;
  }
}
.pill.bgm-pill { cursor: pointer; user-select: none; transition: transform .12s, border-color .12s; }
.pill.bgm-pill:hover { border-color: var(--gold); transform: translateY(-1px); }
"""
    content = content.replace('</head>', f'<style id="mobile-s21-optimizations">{mobile_css}</style>\n</head>')

    # 3. Add BGM pill in the sovereign banner header
    old_resources = '<div class="pill save-pill" id="autosaveStatus"'
    new_resources = '<button type="button" class="pill bgm-pill" id="bgmToggleBtn" title="Toggle background music" aria-label="Toggle background music"><span class="pill-icon" aria-hidden="true">🎵</span><b id="bgmToggleLabel">BGM ON</b></button>\n    <div class="pill save-pill" id="autosaveStatus"'
    if old_resources in content:
        content = content.replace(old_resources, new_resources, 1)
        print("Added BGM toggle pill to header.")
    else:
        print("Warning: old_resources not found for BGM pill")

    # 4. Save Key and Origin updates
    content = content.replace(
        'const SAVE_KEY="monsterStudTesterCareerSaveV1";',
        'const SAVE_KEY="monsterStudCareerSaveV1";'
    )
    content = content.replace(
        'const SAVE_BACKUP_KEY="monsterStudTesterCareerSaveV1_backup";',
        'const SAVE_BACKUP_KEY="monsterStudCareerSaveV1_backup";'
    )
    content = content.replace(
        'const LEGACY_SAVE_KEYS=[];',
        'const LEGACY_SAVE_KEYS=["monsterStudTesterCareerSaveV1","monsterStudTesterCareerSaveV1_backup","monsterStudCareerSave"];'
    )
    content = content.replace(
        'function isPermanentSaveOrigin(){return location.protocol==="http:"&&location.hostname==="127.0.0.1"&&location.port==="8765";}',
        'function isPermanentSaveOrigin(){return true;}'
    )
    content = content.replace(
        'game.stableName="Testers Stable";',
        'game.stableName="The Newblood Stable";'
    )

    # 5. Fix prompt() in fresh() and add showGamePrompt
    old_fresh_prompt = 'let chosen="";try{chosen=window.prompt("Name your monster stable:","The Newblood Stable")||""}catch(e){}\n game.stableName=chosen.trim().slice(0,42)||"The Newblood Stable";'
    new_fresh_default = 'game.stableName="The Newblood Stable";'
    if old_fresh_prompt in content:
        content = content.replace(old_fresh_prompt, new_fresh_default)
        print("Replaced fresh() window.prompt.")
    else:
        print("Notice: fresh prompt pattern was slightly different, checking regex...")
        content = re.sub(
            r'let chosen="";try\{chosen=window\.prompt\("Name your monster stable:","The Newblood Stable"\)\|\|""\}catch\(e\)\{\}\s*game\.stableName=chosen\.trim\(\)\.slice\(0,42\)\|\|"The Newblood Stable";',
            'game.stableName="The Newblood Stable";',
            content
        )

    # Add showGamePrompt and update renameStable
    game_prompt_fn = """
function showGamePrompt(title, message, defaultValue, onConfirm){
 const prior = document.getElementById("gameDialogOverlay"); if (prior) prior.remove();
 const overlay = document.createElement("div"); overlay.id = "gameDialogOverlay"; overlay.className = "game-dialog-overlay";
 overlay.innerHTML = '<div class="game-dialog-card" role="dialog" aria-modal="true"><div class="game-dialog-heading"><div class="game-dialog-emblem" aria-hidden="true">🏛️</div><div><div class="game-dialog-kicker">MONSTER STUD</div><h2>' + esc(title || 'Input') + '</h2></div></div><p class="game-dialog-message">' + esc(message || '') + '</p><div style="margin: 14px 0;"><input type="text" id="gamePromptInput" style="width:100%;box-sizing:border-box;padding:10px 14px;border-radius:8px;border:1px solid #48546a;background:#141927;color:#f4f6ff;font-size:15px;font-weight:600;" maxlength="42" value="' + esc(defaultValue || '') + '"></div><div class="game-dialog-actions"><button type="button" class="btn secondary" id="gamePromptCancel">Cancel</button><button type="button" class="btn" id="gamePromptConfirm">Confirm</button></div></div>';
 document.body.appendChild(overlay);
 const input = overlay.querySelector('#gamePromptInput');
 const close = () => { if (overlay.isConnected) overlay.remove(); document.body.style.overflow = ''; document.removeEventListener('keydown', onKey); };
 const onKey = event => {
   if (event.key === 'Escape') close();
   if (event.key === 'Enter') confirm();
 };
 const confirm = () => {
   const val = input ? input.value : '';
   close();
   if (typeof onConfirm === 'function') onConfirm(val);
 };
 overlay.querySelector('#gamePromptCancel').addEventListener('click', close);
 overlay.querySelector('#gamePromptConfirm').addEventListener('click', confirm);
 overlay.addEventListener('click', event => { if (event.target === overlay) close(); });
 document.addEventListener('keydown', onKey);
 document.body.style.overflow = 'hidden';
 if (input) { input.focus(); input.select(); }
}
"""
    old_rename = "function renameStable(){const entered=prompt('Choose your stable name:',game.stableName||'The Newblood Stable');if(entered===null)return;const name=entered.trim().slice(0,42);if(!name)return alert('Stable name cannot be blank.');game.stableName=name;game.league.participants.filter(p=>p.monsterId).forEach(p=>p.stableName=name);save();showMessage(`Stable renamed to ${name}.`);}"
    new_rename = """function renameStable(){
 showGamePrompt('Rename Stable', 'Choose your stable name:', game.stableName || 'The Newblood Stable', function(entered){
   if(entered === null || entered === undefined) return;
   const name = entered.trim().slice(0, 42);
   if(!name) return showGameDialog('Invalid Name', 'Stable name cannot be blank.');
   game.stableName = name;
   game.league.participants.filter(p => p.monsterId).forEach(p => p.stableName = name);
   save();
   showMessage(`Stable renamed to ${name}.`);
 });
}"""
    if old_rename in content:
        content = content.replace(old_rename, game_prompt_fn + "\n" + new_rename)
        print("Replaced renameStable with styled in-game modal.")
    else:
        print("Warning: old_rename not matched exactly")

    # 6. Audio Manager and Ducking
    bgm_manager_code = """
// Ambient Main Menu Soundtrack Manager with Ducking
const bgmManager = {
  audio: null,
  muted: false,
  baseVolume: 0.25,
  duckedVolume: 0.05,
  init() {
    if (this.audio) return;
    this.audio = new Audio('assets/soundtrack/MainGameMenu-background-track.mp3');
    this.audio.loop = true;
    this.audio.volume = this.baseVolume;
    this.updateUi();
  },
  play() {
    this.init();
    if (!this.muted) {
      const p = this.audio.play();
      if (p && typeof p.catch === 'function') p.catch(() => {});
    }
  },
  pause() {
    if (this.audio) this.audio.pause();
  },
  duck() {
    if (this.audio && !this.muted) {
      this.audio.volume = this.duckedVolume;
    }
  },
  restore() {
    if (this.audio && !this.muted) {
      this.audio.volume = this.baseVolume;
      if (this.audio.paused) this.play();
    }
  },
  toggle() {
    this.init();
    this.muted = !this.muted;
    if (this.muted) {
      this.audio.pause();
    } else {
      this.audio.volume = this.baseVolume;
      this.play();
    }
    this.updateUi();
  },
  updateUi() {
    const label = document.getElementById('bgmToggleLabel');
    const btn = document.getElementById('bgmToggleBtn');
    if (label) label.textContent = this.muted ? 'BGM OFF' : 'BGM ON';
    if (btn) btn.setAttribute('aria-pressed', String(!this.muted));
  }
};
document.addEventListener('DOMContentLoaded', () => {
  const btn = document.getElementById('bgmToggleBtn');
  if (btn) btn.addEventListener('click', () => bgmManager.toggle());
});
"""
    # Insert bgmManager right before setupMonsterStudIntro
    content = content.replace(
        "// Monster Stud title screen: dismiss the full-screen splash and reveal the existing game.",
        bgm_manager_code + "\n// Monster Stud title screen: dismiss the full-screen splash and reveal the existing game."
    )

    # In setupMonsterStudIntro, inside startGame(): call bgmManager.play()
    old_start_game = "intro.classList.add('is-leaving');\n    document.body.style.overflow = previousOverflow;"
    new_start_game = "intro.classList.add('is-leaving');\n    bgmManager.play();\n    document.body.style.overflow = previousOverflow;"
    content = content.replace(old_start_game, new_start_game)

    # 7. Intro Video Sound button labels & unmuted start
    content = content.replace(
        'soundButton.textContent = video.muted ? "?? Enable sound" : "?? Mute sound";',
        'soundButton.textContent = video.muted ? "🔊 Sound On" : "🔇 Mute";'
    )
    content = content.replace(
        "soundButton.textContent = video.muted ? '?? Enable sound' : '?? Mute sound';",
        "soundButton.textContent = video.muted ? '🔊 Sound On' : '🔇 Mute';"
    )

    # 8. Touch-friendly Gene Tooltips
    old_tooltip_touch_check = "if(event.pointerType==='touch')return;\n    const el=event.target.closest&&event.target.closest(selector);if(!el)return;\n    show(el,event.clientX,event.clientY);"
    new_tooltip_touch_code = """if(event.pointerType==='touch')return;
    const el=event.target.closest&&event.target.closest(selector);if(!el)return;
    show(el,event.clientX,event.clientY);"""
    # Add click handler for touch tap-to-toggle
    old_tooltip_hide_events = "document.addEventListener('focusout',event=>{\n    const el=event.target.closest&&event.target.closest(selector);if(el)hide(el);\n  },true);"
    new_tooltip_hide_events = """document.addEventListener('focusout',event=>{
    const el=event.target.closest&&event.target.closest(selector);if(el)hide(el);
  },true);
  document.addEventListener('click', event => {
    const el = event.target.closest && event.target.closest(selector);
    if(el) {
      if(activeTarget === el) {
        hide(el);
      } else {
        const r = el.getBoundingClientRect();
        show(el, r.left + r.width / 2, r.bottom + 6);
      }
    } else {
      hide();
    }
  }, true);"""
    if old_tooltip_hide_events in content:
        content = content.replace(old_tooltip_hide_events, new_tooltip_hide_events)
        print("Added touch click toggle for gene tooltips.")
    else:
        print("Warning: old_tooltip_hide_events not matched exactly")

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

    print("Phase 2 & Phase 3 general updates written successfully.")

if __name__ == "__main__":
    main()
