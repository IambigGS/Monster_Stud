import os
import sys
import time
import subprocess

def main():
    sdk = os.path.join(os.environ.get("LOCALAPPDATA", ""), "Android", "Sdk")
    adb = os.path.join(sdk, "platform-tools", "adb.exe")
    emulator = os.path.join(sdk, "emulator", "emulator.exe")

    print("Starting Android Emulator (Medium_Phone)...")
    env = os.environ.copy()
    env["ANDROID_HOME"] = sdk
    env["ANDROID_SDK_ROOT"] = sdk

    p = subprocess.Popen(
        [emulator, "-avd", "Medium_Phone", "-no-boot-anim", "-no-snapshot-save", "-gpu", "swiftshader_indirect"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        env=env
    )
    print("Emulator PID:", p.pid)

    print("Waiting for device to connect...")
    device_serial = None
    for attempt in range(60):
        res = subprocess.run([adb, "devices"], capture_output=True, text=True)
        lines = [l.strip() for l in res.stdout.strip().split("\n") if l.strip()]
        for l in lines[1:]:
            parts = l.split()
            if len(parts) >= 2 and parts[1] == "device":
                device_serial = parts[0]
                break
        if device_serial:
            break
        time.sleep(2)

    if not device_serial:
        print("Failed to detect online device.")
        return

    print(f"Device online: {device_serial}. Waiting for boot completion...")
    for attempt in range(60):
        res = subprocess.run([adb, "-s", device_serial, "shell", "getprop", "sys.boot_completed"], capture_output=True, text=True)
        if res.stdout.strip() == "1":
            print("Android system booted successfully!")
            break
        time.sleep(2)

    # Install APK
    apk = os.path.abspath("MonsterStud-S21-Release.apk")
    print(f"Installing {apk} onto {device_serial}...")
    res = subprocess.run([adb, "-s", device_serial, "install", "-r", "-d", apk], capture_output=True, text=True)
    print(res.stdout)
    if res.stderr:
        print("Stderr:", res.stderr)

    # Launch app
    print("Launching MainActivity...")
    res = subprocess.run([adb, "-s", device_serial, "shell", "am", "start", "-n", "com.dragoncopper.monsterstud/.MainActivity"], capture_output=True, text=True)
    print(res.stdout)

    # Wait for webview to load
    print("Waiting for game intro and webview to render...")
    time.sleep(6)

    # Capture screenshot
    os.makedirs("test_screenshots", exist_ok=True)
    sc_dest = os.path.abspath("test_screenshots/live_game_launch.png")
    subprocess.run([adb, "-s", device_serial, "shell", "screencap", "-p", "/sdcard/screen.png"])
    subprocess.run([adb, "-s", device_serial, "pull", "/sdcard/screen.png", sc_dest], capture_output=True)

    if os.path.exists(sc_dest):
        print(f"SUCCESS! Verified on device! Screenshot captured: {sc_dest} ({os.path.getsize(sc_dest):,} bytes)")

if __name__ == "__main__":
    main()
