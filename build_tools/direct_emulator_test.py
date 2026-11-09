import os
import sys
import time
import subprocess

def main():
    sdk = os.path.join(os.environ.get("LOCALAPPDATA", ""), "Android", "Sdk")
    adb = os.path.join(sdk, "platform-tools", "adb.exe")
    serial = "emulator-5554"
    apk = os.path.abspath("MonsterStud-S21-Release.apk")

    print(f"Connecting to {serial}...")
    print(f"Installing {apk}...")
    res = subprocess.run([adb, "-s", serial, "install", "-r", "-d", apk], capture_output=True, text=True)
    print("Install output:\n", res.stdout)
    if res.stderr:
        print("Install error:\n", res.stderr)

    print("Launching com.dragoncopper.monsterstud/.MainActivity...")
    res = subprocess.run([adb, "-s", serial, "shell", "am", "start", "-n", "com.dragoncopper.monsterstud/.MainActivity"], capture_output=True, text=True)
    print("Launch output:\n", res.stdout)

    print("Waiting 5 seconds for opening scene to render...")
    time.sleep(5)

    os.makedirs("test_screenshots", exist_ok=True)
    out_png = os.path.abspath("test_screenshots/emulator_running.png")
    subprocess.run([adb, "-s", serial, "shell", "screencap", "-p", "/sdcard/screen.png"])
    subprocess.run([adb, "-s", serial, "pull", "/sdcard/screen.png", out_png], capture_output=True)

    if os.path.exists(out_png):
        print(f"SUCCESS! Screenshot pulled: {out_png} ({os.path.getsize(out_png):,} bytes)")

if __name__ == "__main__":
    main()
