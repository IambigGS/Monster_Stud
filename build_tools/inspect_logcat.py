import os, subprocess

sdk = os.path.join(os.environ.get("LOCALAPPDATA", ""), "Android", "Sdk")
adb = os.path.join(sdk, "platform-tools", "adb.exe")
serial = "emulator-5554"

res = subprocess.run([adb, "-s", serial, "logcat", "-d", "-s", "MonsterStud:V", "chromium:V", "ActivityTaskManager:I"], capture_output=True, text=True)
print("LOGCAT:\n", res.stdout[-2000:])
