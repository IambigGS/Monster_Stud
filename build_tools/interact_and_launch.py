import os
import sys
import time
import subprocess

def main():
    sdk = os.path.join(os.environ.get("LOCALAPPDATA", ""), "Android", "Sdk")
    adb = os.path.join(sdk, "platform-tools", "adb.exe")
    serial = "emulator-5554"

    # Send Back key or tap Wait to dismiss any system ANR dialog
    print("Dismissing any system boot dialogs...")
    subprocess.run([adb, "-s", serial, "shell", "input", "keyevent", "KEYCODE_BACK"])
    time.sleep(1)

    # Launch Monster Stud
    print("Launching Monster Stud...")
    res = subprocess.run([adb, "-s", serial, "shell", "am", "start", "-S", "-n", "com.dragoncopper.monsterstud/.MainActivity"], capture_output=True, text=True)
    print(res.stdout)

    print("Waiting 5 seconds for webview to load...")
    time.sleep(5)

    os.makedirs("test_screenshots", exist_ok=True)
    sc_dest = os.path.abspath("test_screenshots/live_game_active.png")
    subprocess.run([adb, "-s", serial, "shell", "screencap", "-p", "/data/local/tmp/sc.png"])
    subprocess.run([adb, "-s", serial, "pull", "/data/local/tmp/sc.png", sc_dest], capture_output=True)

    artifact_dir = os.path.join(
        os.environ.get("USERPROFILE", ""),
        ".gemini", "antigravity", "brain", "6383a5b5-e6fb-4d16-880d-1d7cdc4144d7"
    )
    art_dest = os.path.join(artifact_dir, "live_game_active.png")
    if os.path.exists(sc_dest):
        import shutil
        shutil.copyfile(sc_dest, art_dest)
        print(f"Captured and copied: {art_dest} ({os.path.getsize(art_dest):,} bytes)")

if __name__ == "__main__":
    main()
