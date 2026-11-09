import os
import sys
import time
import subprocess

DETACHED_PROCESS = 0x00000008
CREATE_NEW_PROCESS_GROUP = 0x00000200

def main():
    sdk = os.path.join(os.environ.get("LOCALAPPDATA", ""), "Android", "Sdk")
    adb = os.path.join(sdk, "platform-tools", "adb.exe")
    emulator = os.path.join(sdk, "emulator", "emulator.exe")

    print("Checking if emulator is already running...")
    res = subprocess.run([adb, "devices"], capture_output=True, text=True)
    running_devs = [l.split()[0] for l in res.stdout.strip().split("\n")[1:] if "\tdevice" in l]

    if running_devs:
        serial = running_devs[0]
        print(f"Reusing running emulator: {serial}")
    else:
        print("Launching emulator in detached mode...")
        env = os.environ.copy()
        env["ANDROID_HOME"] = sdk
        env["ANDROID_SDK_ROOT"] = sdk

        subprocess.Popen(
            [emulator, "-avd", "Medium_Phone", "-no-boot-anim", "-no-snapshot-save", "-gpu", "swiftshader_indirect"],
            creationflags=DETACHED_PROCESS | CREATE_NEW_PROCESS_GROUP,
            close_fds=True,
            env=env
        )
        print("Waiting for device connection...")
        serial = None
        for _ in range(60):
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
        print("Error: Could not connect to emulator.")
        return

    print(f"Waiting for {serial} boot completed...")
    for _ in range(60):
        res = subprocess.run([adb, "-s", serial, "shell", "getprop", "sys.boot_completed"], capture_output=True, text=True)
        if res.stdout.strip() == "1":
            print("System booted!")
            break
        time.sleep(2)

    apk = os.path.abspath("MonsterStud-S21-Release.apk")
    print(f"Installing {apk}...")
    res = subprocess.run([adb, "-s", serial, "install", "-r", "-d", apk], capture_output=True, text=True)
    print("Install result:", res.stdout.strip())

    print("Launching Monster Stud...")
    res = subprocess.run([adb, "-s", serial, "shell", "am", "start", "-n", "com.dragoncopper.monsterstud/.MainActivity"], capture_output=True, text=True)
    print("Launch result:", res.stdout.strip())

    print("Waiting 6 seconds for intro to load...")
    time.sleep(6)

    os.makedirs("test_screenshots", exist_ok=True)
    sc1 = os.path.abspath("test_screenshots/01_game_intro_video.png")
    subprocess.run([adb, "-s", serial, "shell", "screencap", "-p", "/data/local/tmp/sc1.png"])
    subprocess.run([adb, "-s", serial, "pull", "/data/local/tmp/sc1.png", sc1], capture_output=True)
    if os.path.exists(sc1):
        print(f"Screenshot 1 saved: {sc1} ({os.path.getsize(sc1):,} bytes)")

    # Tap on screen to skip/advance past intro video to title screen
    print("Simulating tap to advance past intro video...")
    subprocess.run([adb, "-s", serial, "shell", "input", "tap", "500", "1000"])
    time.sleep(2)

    sc2 = os.path.abspath("test_screenshots/02_title_screen.png")
    subprocess.run([adb, "-s", serial, "shell", "screencap", "-p", "/data/local/tmp/sc2.png"])
    subprocess.run([adb, "-s", serial, "pull", "/data/local/tmp/sc2.png", sc2], capture_output=True)
    if os.path.exists(sc2):
        print(f"Screenshot 2 saved: {sc2} ({os.path.getsize(sc2):,} bytes)")

    # Tap again on Title Screen ("Click to start") to enter main game stable
    print("Simulating tap on Title Screen to enter main game...")
    subprocess.run([adb, "-s", serial, "shell", "input", "tap", "500", "1000"])
    time.sleep(3)

    sc3 = os.path.abspath("test_screenshots/03_main_stable_view.png")
    subprocess.run([adb, "-s", serial, "shell", "screencap", "-p", "/data/local/tmp/sc3.png"])
    subprocess.run([adb, "-s", serial, "pull", "/data/local/tmp/sc3.png", sc3], capture_output=True)
    if os.path.exists(sc3):
        print(f"Screenshot 3 saved: {sc3} ({os.path.getsize(sc3):,} bytes)")

    print("ALL EMULATOR TESTS COMPLETED!")

if __name__ == "__main__":
    main()
