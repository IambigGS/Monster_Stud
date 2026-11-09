import os

localappdata = os.environ.get("LOCALAPPDATA", "")
sdk_dir = os.path.join(localappdata, "Android", "Sdk")
adb = os.path.join(sdk_dir, "platform-tools", "adb.exe")
emulator = os.path.join(sdk_dir, "emulator", "emulator.exe")

print("adb exists:", os.path.exists(adb))
print("emulator exists:", os.path.exists(emulator))

# Check for existing AVDs
userprofile = os.environ.get("USERPROFILE", "")
avd_dir = os.path.join(userprofile, ".android", "avd")
print(".android/avd exists:", os.path.exists(avd_dir))
if os.path.exists(avd_dir):
    print("AVDs found:", os.listdir(avd_dir))
