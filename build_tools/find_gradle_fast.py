import os, glob

userprofile = os.environ.get("USERPROFILE", "")
dists = os.path.join(userprofile, ".gradle", "wrapper", "dists")
for root, dirs, files in os.walk(dists):
    if "gradle.bat" in files:
        print("GRADLE_BAT:", os.path.join(root, "gradle.bat"))
        break
