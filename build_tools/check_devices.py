import os, subprocess

localappdata = os.environ.get("LOCALAPPDATA", "")
sdk_dir = os.path.join(localappdata, "Android", "Sdk")
adb = os.path.join(sdk_dir, "platform-tools", "adb.exe")

res = subprocess.run([adb, "devices"], capture_output=True, text=True)
print(res.stdout)
