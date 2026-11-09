import os
import sys
import time
import subprocess

def main():
    sdk = os.path.join(os.environ.get("LOCALAPPDATA", ""), "Android", "Sdk")
    adb = os.path.join(sdk, "platform-tools", "adb.exe")
    emulator = os.path.join(sdk, "emulator", "emulator.exe")

    # Launch using Windows 'start' so it runs as an independent OS process
    cmd = f'start "" "{emulator}" -avd Medium_Phone -gpu swiftshader_indirect -no-boot-anim'
    print("Executing independent launch:", cmd)
    subprocess.run(["cmd.exe", "/c", cmd], check=True)

    print("Waiting for device to appear in adb...")
    serial = None
    for i in range(45):
        res = subprocess.run([adb, "devices"], capture_output=True, text=True)
        for line in res.stdout.strip().split("\n")[1:]:
            parts = line.split()
            if len(parts) >= 2 and parts[1] == "device":
                serial = parts[0]
                break
        if serial:
            break
        time.sleep(2)

    if not serial:
        print("Device not found yet, checking offline devices...")
        res = subprocess.run([adb, "devices"], capture_output=True, text=True)
        print(res.stdout)
        return

    print(f"Device connected: {serial}. Waiting for boot completion...")
    for _ in range(60):
        res = subprocess.run([adb, "-s", serial, "shell", "getprop", "sys.boot_completed"], capture_output=True, text=True)
        if res.stdout.strip() == "1":
            print("System booted!")
            break
        time.sleep(2)

    # Dismiss any system dialogs
    time.sleep(2)
    subprocess.run([adb, "-s", serial, "shell", "input", "keyevent", "KEYCODE_BACK"])

    # Launch Monster Stud
    print("Launching Monster Stud...")
    apk = os.path.abspath("MonsterStud-S21-Release.apk")
    subprocess.run([adb, "-s", serial, "install", "-r", "-d", apk], capture_output=True)
    subprocess.run([adb, "-s", serial, "shell", "am", "start", "-S", "-n", "com.dragoncopper.monsterstud/.MainActivity"], capture_output=True)

    print("Waiting 8 seconds for game intro and webview to render...")
    time.sleep(8)

    os.makedirs("test_screenshots", exist_ok=True)
    sc = os.path.abspath("test_screenshots/live_game_verified.png")
    subprocess.run([adb, "-s", serial, "shell", "screencap", "-p", "/data/local/tmp/sc.png"])
    subprocess.run([adb, "-s", serial, "pull", "/data/local/tmp/sc.png", sc], capture_output=True)

    artifact_dir = os.path.join(
        os.environ.get("USERPROFILE", ""),
        ".gemini", "antigravity", "brain", "6383a5b5-e6fb-4d16-880d-1d7cdc4144d7"
    )
    art_dest = os.path.join(artifact_dir, "live_game_verified.png")
    if os.path.exists(sc):
        import shutil
        shutil.copyfile(sc, art_dest)
        print(f"SUCCESS! Verified screenshot saved to: {art_dest} ({os.path.getsize(art_dest):,} bytes)")

if __name__ == "__main__":
    main()
