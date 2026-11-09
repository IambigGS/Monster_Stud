import os, subprocess

sdk = os.path.join(os.environ.get("LOCALAPPDATA", ""), "Android", "Sdk")
adb = os.path.join(sdk, "platform-tools", "adb.exe")
serial = "emulator-5554"

res = subprocess.run([adb, "-s", serial, "logcat", "-d"], capture_output=True, text=True, errors="ignore")
lines = res.stdout.split("\n")
print(f"Total logcat lines: {len(lines)}")
for l in lines:
    if "dragoncopper" in l.lower() or "monsterstud" in l.lower() or "fatal" in l.lower() or "exception" in l.lower():
        print(l.strip())
