import os, sys, time, subprocess

sdk = os.path.join(os.environ.get("LOCALAPPDATA", ""), "Android", "Sdk")
adb = os.path.join(sdk, "platform-tools", "adb.exe")
emulator = os.path.join(sdk, "emulator", "emulator.exe")

env = os.environ.copy()
env["ANDROID_HOME"] = sdk
env["ANDROID_SDK_ROOT"] = sdk

print("Launching emulator...")
p = subprocess.Popen(
    [emulator, "-avd", "Medium_Phone", "-no-boot-anim", "-no-audio", "-gpu", "swiftshader_indirect"],
    stdout=subprocess.DEVNULL,
    stderr=subprocess.DEVNULL,
    env=env
)

time.sleep(15)
serial = "emulator-5554"
print(f"Waiting for {serial}...")
subprocess.run([adb, "-s", serial, "wait-for-device"])

for _ in range(30):
    res = subprocess.run([adb, "-s", serial, "shell", "getprop", "sys.boot_completed"], capture_output=True, text=True)
    if res.stdout.strip() == "1":
        print("Boot complete!")
        break
    time.sleep(2)

print("Starting app...")
subprocess.run([adb, "-s", serial, "shell", "am", "start", "-S", "-n", "com.dragoncopper.monsterstud/.MainActivity"])
time.sleep(4)

# Tap to advance past video intro to Title Screen
print("Tapping to advance to Title Screen...")
subprocess.run([adb, "-s", serial, "shell", "input", "tap", "540", "1200"])
time.sleep(2)

# Screenshot of Title Screen
sc_title = os.path.abspath("test_screenshots/verified_title_screen.png")
subprocess.run([adb, "-s", serial, "shell", "screencap", "-p", "/data/local/tmp/sc_title.png"])
subprocess.run([adb, "-s", serial, "pull", "/data/local/tmp/sc_title.png", sc_title], capture_output=True)

# Tap again to enter Main Stable
print("Tapping to enter Main Game Stable...")
subprocess.run([adb, "-s", serial, "shell", "input", "tap", "540", "1200"])
time.sleep(3)

# Screenshot of Main Stable
sc_stable = os.path.abspath("test_screenshots/verified_stable_screen.png")
subprocess.run([adb, "-s", serial, "shell", "screencap", "-p", "/data/local/tmp/sc_stable.png"])
subprocess.run([adb, "-s", serial, "pull", "/data/local/tmp/sc_stable.png", sc_stable], capture_output=True)

artifact_dir = os.path.join(os.environ.get("USERPROFILE", ""), ".gemini", "antigravity", "brain", "6383a5b5-e6fb-4d16-880d-1d7cdc4144d7")
import shutil
if os.path.exists(sc_title):
    shutil.copyfile(sc_title, os.path.join(artifact_dir, "verified_title_screen.png"))
    print("Copied title screen to artifact dir!")
if os.path.exists(sc_stable):
    shutil.copyfile(sc_stable, os.path.join(artifact_dir, "verified_stable_screen.png"))
    print("Copied stable screen to artifact dir!")

p.terminate()
print("All done!")
