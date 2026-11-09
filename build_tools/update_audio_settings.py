import os
import re

html_path = os.path.join('web', 'index.html')
with open(html_path, 'r', encoding='utf-8') as f:
    c = f.read()

# 1. Update button markup
c = c.replace(
    '<button type="button" class="video-intro-control" id="videoIntroSoundBtn" aria-label="Enable video sound">🔊 Enable sound</button>',
    '<button type="button" class="video-intro-control" id="videoIntroSoundBtn" aria-label="Toggle video sound">🔊 Sound: ON</button>'
)

# 2. Update setSoundLabel
old_label = '''  function setSoundLabel(){
    if (!soundButton) return;
    soundButton.textContent = video.muted ? "🔊 Enable sound" : "🔇 Mute sound";
    soundButton.setAttribute('aria-label', video.muted ? 'Enable video sound' : 'Mute video sound');
  }'''

new_label = '''  function setSoundLabel(){
    if (!soundButton) return;
    soundButton.textContent = video.muted ? "🔇 Sound: OFF" : "🔊 Sound: ON";
    soundButton.setAttribute('aria-label', video.muted ? 'Turn sound on' : 'Turn sound off');
  }'''

if old_label not in c:
    old_label = old_label.replace('\n', '\r\n')
    new_label = new_label.replace('\n', '\r\n')

assert old_label in c, "Could not find setSoundLabel in web/index.html"
c = c.replace(old_label, new_label, 1)

# 3. Add touch/click unmute listener on document so first user interaction immediately enables sound if browser blocked initial autoplay
old_playback = '''    const startPlayback = video.play();
    if (startPlayback && typeof startPlayback.then === 'function') {
      startPlayback.then(() => {
        setSoundLabel();
      }).catch(() => {
        // Browsers commonly block sound on first load: retry muted so the video still autoplays.
        video.muted = true;
        setSoundLabel();
        const mutedPlayback = video.play();
        if (mutedPlayback && typeof mutedPlayback.catch === 'function') {
          mutedPlayback.catch(() => {
            if (hint) hint.textContent = 'CLICK TO CONTINUE TO THE TITLE SCREEN';
            showTitleScreen();
          });
        }
      });
    }'''

new_playback = '''    const startPlayback = video.play();
    if (startPlayback && typeof startPlayback.then === 'function') {
      startPlayback.then(() => {
        video.muted = false;
        setSoundLabel();
      }).catch(() => {
        // In restrictive browser environments without gesture, retry muted and listen for first touch to unmute
        video.muted = true;
        setSoundLabel();
        const mutedPlayback = video.play();
        if (mutedPlayback && typeof mutedPlayback.catch === 'function') {
          mutedPlayback.catch(() => {
            if (hint) hint.textContent = 'CLICK TO CONTINUE TO THE TITLE SCREEN';
            showTitleScreen();
          });
        }
        const unmuteOnGesture = () => {
          if (!finished && video) {
            video.muted = false;
            setSoundLabel();
          }
          document.removeEventListener('pointerdown', unmuteOnGesture, true);
          document.removeEventListener('keydown', unmuteOnGesture, true);
        };
        document.addEventListener('pointerdown', unmuteOnGesture, true);
        document.addEventListener('keydown', unmuteOnGesture, true);
      });
    }'''

if old_playback not in c:
    old_playback = old_playback.replace('\n', '\r\n')
    new_playback = new_playback.replace('\n', '\r\n')

assert old_playback in c, "Could not find startPlayback in web/index.html"
c = c.replace(old_playback, new_playback, 1)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(c)

print("web/index.html sound configuration updated successfully!")
