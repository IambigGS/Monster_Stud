import os, sys, time, subprocess, shutil

sdk = os.path.join(os.environ.get("LOCALAPPDATA", ""), "Android", "Sdk")
adb = os.path.join(sdk, "platform-tools", "adb.exe")
emulator = os.path.join(sdk, "emulator", "emulator.exe")

env = os.environ.copy()
env["ANDROID_HOME"] = sdk
env["ANDROID_SDK_ROOT"] = sdk

print("Checking emulator connection...")
res = subprocess.run([adb, "devices"], capture_output=True, text=True)
running = [l.split()[0] for l in res.stdout.strip().split("\n")[1:] if "\tdevice" in l]

proc = None
if running:
    serial = running[0]
    print(f"Connecting to running emulator {serial}...")
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
    print("Device offline.")
    sys.exit(1)

print("Waiting for boot completion...")
for _ in range(50):
    res = subprocess.run([adb, "-s", serial, "shell", "getprop", "sys.boot_completed"], capture_output=True, text=True)
    if res.stdout.strip() == "1":
        print("Boot complete!")
        break
    time.sleep(2)

# Ensure screen is ON and lockscreen dismissed
print("Waking screen and dismissing keyguard...")
subprocess.run([adb, "-s", serial, "shell", "input", "keyevent", "KEYCODE_WAKEUP"])
subprocess.run([adb, "-s", serial, "shell", "wm", "dismiss-keyguard"])
time.sleep(1)

apk = os.path.abspath("MonsterStud-S21-Release.apk")
print(f"Installing {apk}...")
subprocess.run([adb, "-s", serial, "install", "-r", "-d", apk], capture_output=True)

print("Starting Monster Stud Activity...")
subprocess.run([adb, "-s", serial, "shell", "am", "start", "-S", "-W", "-n", "com.dragoncopper.monsterstud/.MainActivity"])

print("Waiting 6 seconds...")
time.sleep(6)

focus = subprocess.run([adb, "-s", serial, "shell", "dumpsys", "window"], capture_output=True, text=True)
for line in focus.stdout.split("\n"):
    if "mCurrentFocus" in line or "mFocusedApp" in line:
        print("Focus:", line.strip())

os.makedirs("test_screenshots", exist_ok=True)
sc1 = os.path.abspath("test_screenshots/verified_ingame_1.png")
subprocess.run([adb, "-s", serial, "shell", "screencap", "-p", "/data/local/tmp/v1.png"])
subprocess.run([adb, "-s", serial, "pull", "/data/local/tmp/v1.png", sc1], capture_output=True)

# Tap to advance
print("Tapping screen to advance...")
subprocess.run([adb, "-s", serial, "shell", "input", "tap", "540", "1200"])
time.sleep(2)

sc2 = os.path.abspath("test_screenshots/verified_ingame_2.png")
subprocess.run([adb, "-s", serial, "shell", "screencap", "-p", "/data/local/tmp/v2.png"])
subprocess.run([adb, "-s", serial, "pull", "/data/local/tmp/v2.png", sc2], capture_output=True)

# Tap again
print("Tapping screen into main stable...")
subprocess.run([adb, "-s", serial, "shell", "input", "tap", "540", "1200"])
time.sleep(2)

sc3 = os.path.abspath("test_screenshots/verified_ingame_3.png")
subprocess.run([adb, "-s", serial, "shell", "screencap", "-p", "/data/local/tmp/v3.png"])
subprocess.run([adb, "-s", serial, "pull", "/data/local/tmp/v3.png", sc3], capture_output=True)

artifact_dir = os.path.join(
    os.environ.get("USERPROFILE", ""),
    ".gemini", "antigravity", "brain", "6383a5b5-e6fb-4d16-880d-1d7cdc4144d7"
)
for f in ["verified_ingame_1.png", "verified_ingame_2.png", "verified_ingame_3.png"]:
    p = os.path.join("test_screenshots", f)
    if os.path.exists(p):
        shutil.copyfile(p, os.path.join(artifact_dir, f))
        print(f"Copied {f} to artifacts ({os.path.getsize(p):,} bytes)")

if proc:
    proc.terminate()
print("Verification finished!")
