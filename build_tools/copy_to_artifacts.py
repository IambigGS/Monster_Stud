import os
import shutil

artifact_dir = os.path.join(
    os.environ.get("USERPROFILE", ""),
    ".gemini", "antigravity", "brain", "6383a5b5-e6fb-4d16-880d-1d7cdc4144d7"
)
os.makedirs(artifact_dir, exist_ok=True)

files = ['01_game_intro_video.png', '02_title_screen.png', '03_main_stable_view.png']
for name in files:
    src = os.path.join('test_screenshots', name)
    dst = os.path.join(artifact_dir, name)
    shutil.copyfile(src, dst)
    print(f"Copied {name} to {dst} ({os.path.getsize(dst):,} bytes)")
