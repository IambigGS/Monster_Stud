import os, glob

userprofile = os.environ.get("USERPROFILE", "")
print("Userprofile:", userprofile)

# Check common locations for android CLI or sidecars
search_dirs = [
    os.path.join(userprofile, ".gemini"),
    os.path.join(userprofile, "AppData", "Local"),
    os.path.join(userprofile, "AppData", "Roaming"),
]

for d in search_dirs:
    if os.path.exists(d):
        for root, dirs, files in os.walk(d):
            for f in files:
                if f.lower() in ["android.exe", "android.cmd", "android.bat"]:
                    print("Found android cli:", os.path.join(root, f))
