import os, sys, time, subprocess

sdk = os.path.join(os.environ.get("LOCALAPPDATA", ""), "Android", "Sdk")
adb = os.path.join(sdk, "platform-tools", "adb.exe")
emulator = os.path.join(sdk, "emulator", "emulator.exe")

env = os.environ.copy()
env["ANDROID_HOME"] = sdk
env["ANDROID_SDK_ROOT"] = sdk

print("Starting headless emulator...")
p = subprocess.Popen(
    [emulator, "-avd", "Medium_Phone", "-no-window", "-no-audio", "-no-boot-anim", "-gpu", "swiftshader_indirect"],
    stdout=subprocess.DEVNULL,
    stderr=subprocess.DEVNULL,
    env=env
)

print(f"Emulator launched with PID {p.pid}. Waiting for adb device...")
serial = None
for i in range(30):
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
    print("Device not ready in 60s.")
    p.terminate()
    sys.exit(1)

print(f"Device ready: {serial}. Waiting for boot completion...")
for _ in range(40):
    res = subprocess.run([adb, "-s", serial, "shell", "getprop", "sys.boot_completed"], capture_output=True, text=True)
    if res.stdout.strip() == "1":
        print("Boot complete!")
        break
    time.sleep(2)

# Launch app
print("Launching Monster Stud...")
subprocess.run([adb, "-s", serial, "shell", "am", "start", "-S", "-n", "com.dragoncopper.monsterstud/.MainActivity"], capture_output=True)

# Wait 6 seconds
time.sleep(6)

# Take screenshot
os.makedirs("test_screenshots", exist_ok=True)
dest = os.path.abspath("test_screenshots/headless_verified.png")
subprocess.run([adb, "-s", serial, "shell", "screencap", "-p", "/data/local/tmp/headless.png"])
subprocess.run([adb, "-s", serial, "pull", "/data/local/tmp/headless.png", dest], capture_output=True)

if os.path.exists(dest):
    print(f"Screenshot successfully captured: {dest} ({os.path.getsize(dest):,} bytes)")
    artifact_dir = os.path.join(os.environ.get("USERPROFILE", ""), ".gemini", "antigravity", "brain", "6383a5b5-e6fb-4d16-880d-1d7cdc4144d7")
    art_dest = os.path.join(artifact_dir, "headless_verified.png")
    import shutil
    shutil.copyfile(dest, art_dest)
    print(f"Copied to artifact dir: {art_dest}")

p.terminate()
print("Test completed cleanly!")
