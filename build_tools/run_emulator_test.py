import os
import sys
import time
import subprocess

def main():
    localappdata = os.environ.get("LOCALAPPDATA", "")
    sdk_dir = os.path.join(localappdata, "Android", "Sdk")
    adb = os.path.join(sdk_dir, "platform-tools", "adb.exe")
    emulator = os.path.join(sdk_dir, "emulator", "emulator.exe")

    apk_path = os.path.abspath("MonsterStud-S21-Release.apk")
    if not os.path.exists(apk_path):
        print(f"Error: {apk_path} not found.")
        return

    print(f"Target APK: {apk_path} ({os.path.getsize(apk_path):,} bytes)")

    # 1. Check if an emulator or device is running
    res = subprocess.run([adb, "devices"], capture_output=True, text=True)
    lines = [line.strip() for line in res.stdout.strip().split("\n") if line.strip()]
    devices = [l.split()[0] for l in lines[1:] if "device" in l and not "offline" in l]

    target_device = None
    if devices:
        target_device = devices[0]
        print(f"Using already running device: {target_device}")
    else:
        print("Starting emulator: Medium_Phone...")
        # Start emulator non-blocking
        subprocess.Popen(
            [emulator, "-avd", "Medium_Phone", "-no-boot-anim"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        print("Waiting for emulator to come online...")
        # Wait up to 60s for device to show up
        for _ in range(60):
            res = subprocess.run([adb, "devices"], capture_output=True, text=True)
            cur_lines = [l.strip() for l in res.stdout.strip().split("\n") if l.strip()]
            cur_devs = [l.split()[0] for l in cur_lines[1:] if "device" in l and not "offline" in l]
            if cur_devs:
                target_device = cur_devs[0]
                break
            time.sleep(2)

    if not target_device:
        print("Timeout waiting for emulator device.")
        return

    print(f"Device ready: {target_device}. Waiting for system boot completion...")
    for _ in range(60):
        res = subprocess.run([adb, "-s", target_device, "shell", "getprop", "sys.boot_completed"], capture_output=True, text=True)
        if res.stdout.strip() == "1":
            print("System boot completed!")
            break
        time.sleep(2)

    # 2. Install APK
    print("Installing MonsterStud-S21-Release.apk...")
    install_res = subprocess.run([adb, "-s", target_device, "install", "-r", "-d", apk_path], capture_output=True, text=True)
    print(install_res.stdout)
    if "Success" not in install_res.stdout:
        print(install_res.stderr)

    # 3. Launch the App
    print("Launching com.dragoncopper.monsterstud/.MainActivity...")
    launch_res = subprocess.run([adb, "-s", target_device, "shell", "am", "start", "-n", "com.dragoncopper.monsterstud/.MainActivity"], capture_output=True, text=True)
    print(launch_res.stdout)

    # 4. Wait 3 seconds and capture screenshot
    time.sleep(4)
    print("Capturing live emulator screen...")
    os.makedirs("test_screenshots", exist_ok=True)
    screenshot_path = os.path.abspath("test_screenshots/emulator_launch.png")
    subprocess.run([adb, "-s", target_device, "shell", "screencap", "-p", "/sdcard/screen.png"])
    subprocess.run([adb, "-s", target_device, "pull", "/sdcard/screen.png", screenshot_path], capture_output=True)
    if os.path.exists(screenshot_path):
        print(f"Screenshot saved to: {screenshot_path} ({os.path.getsize(screenshot_path):,} bytes)")

if __name__ == "__main__":
    main()
