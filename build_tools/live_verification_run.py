import os
import sys
import time
import subprocess
import shutil

def main():
    sdk = os.path.join(os.environ.get("LOCALAPPDATA", ""), "Android", "Sdk")
    adb = os.path.join(sdk, "platform-tools", "adb.exe")
    emulator = os.path.join(sdk, "emulator", "emulator.exe")

    env = os.environ.copy()
    env["ANDROID_HOME"] = sdk
    env["ANDROID_SDK_ROOT"] = sdk

    print("Checking if emulator is running...")
    res = subprocess.run([adb, "devices"], capture_output=True, text=True)
    lines = [l.strip() for l in res.stdout.strip().split("\n")[1:] if l.strip()]
    running = [l.split()[0] for l in lines if "\tdevice" in l]

    if running:
        serial = running[0]
        print(f"Using already running emulator: {serial}")
        proc = None
    else:
        print("Starting emulator: Medium_Phone...")
        proc = subprocess.Popen(
            [emulator, "-avd", "Medium_Phone", "-no-boot-anim", "-no-audio", "-gpu", "swiftshader_indirect"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            env=env
        )
        serial = None
        for _ in range(40):
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
        print("Device not ready.")
        return

    print(f"Waiting for {serial} to complete boot...")
    for _ in range(60):
        res = subprocess.run([adb, "-s", serial, "shell", "getprop", "sys.boot_completed"], capture_output=True, text=True)
        if res.stdout.strip() == "1":
            print("System boot completed!")
            break
        time.sleep(2)

    # Let CPU settle for 5 seconds after boot
    time.sleep(5)

    # Dismiss any keyguard / lockscreen / dialog
    subprocess.run([adb, "-s", serial, "shell", "input", "keyevent", "82"]) # MENU/UNLOCK
    subprocess.run([adb, "-s", serial, "shell", "input", "keyevent", "4"])  # BACK

    # Clear logcat buffer
    subprocess.run([adb, "-s", serial, "logcat", "-c"])

    # Launch Monster Stud
    print("Launching Monster Stud...")
    subprocess.run([adb, "-s", serial, "shell", "am", "start", "-S", "-W", "-n", "com.dragoncopper.monsterstud/.MainActivity"])

    # Wait 8 seconds for WebView and assets to load
    print("Waiting for game interface to render...")
    time.sleep(8)

    # Inspect logcat for chromium / WebConsole logs
    log_res = subprocess.run([adb, "-s", serial, "logcat", "-d", "-s", "chromium:I", "MainActivity:I"], capture_output=True, text=True)
    print("Browser logcat output:")
    for line in log_res.stdout.split("\n"):
        if "console" in line.lower() or "monster" in line.lower() or "error" in line.lower():
            print("  ", line)

    # Take screenshot 1: Video Intro or Title Screen
    os.makedirs("test_screenshots", exist_ok=True)
    sc1 = os.path.abspath("test_screenshots/01_game_running.png")
    subprocess.run([adb, "-s", serial, "shell", "screencap", "-p", "/data/local/tmp/sc1.png"])
    subprocess.run([adb, "-s", serial, "pull", "/data/local/tmp/sc1.png", sc1], capture_output=True)

    # Tap on center of screen to advance past intro/title
    print("Tapping to advance screen...")
    subprocess.run([adb, "-s", serial, "shell", "input", "tap", "540", "1200"])
    time.sleep(3)

    sc2 = os.path.abspath("test_screenshots/02_game_advanced.png")
    subprocess.run([adb, "-s", serial, "shell", "screencap", "-p", "/data/local/tmp/sc2.png"])
    subprocess.run([adb, "-s", serial, "pull", "/data/local/tmp/sc2.png", sc2], capture_output=True)

    # Tap once more to ensure reaching main stable
    print("Tapping again to enter stable...")
    subprocess.run([adb, "-s", serial, "shell", "input", "tap", "540", "1200"])
    time.sleep(3)

    sc3 = os.path.abspath("test_screenshots/03_game_stable.png")
    subprocess.run([adb, "-s", serial, "shell", "screencap", "-p", "/data/local/tmp/sc3.png"])
    subprocess.run([adb, "-s", serial, "pull", "/data/local/tmp/sc3.png", sc3], capture_output=True)

    artifact_dir = os.path.join(
        os.environ.get("USERPROFILE", ""),
        ".gemini", "antigravity", "brain", "6383a5b5-e6fb-4d16-880d-1d7cdc4144d7"
    )
    for name in ["01_game_running.png", "02_game_advanced.png", "03_game_stable.png"]:
        p = os.path.join("test_screenshots", name)
        if os.path.exists(p):
            shutil.copyfile(p, os.path.join(artifact_dir, name))
            print(f"Copied {name} to artifact directory ({os.path.getsize(p):,} bytes)")

    if proc:
        proc.terminate()
    print("Verification run completed successfully!")

if __name__ == "__main__":
    main()
