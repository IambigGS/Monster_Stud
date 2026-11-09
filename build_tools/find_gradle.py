import os, glob

userprofile = os.environ.get("USERPROFILE", "")
gradle_home = os.path.join(userprofile, ".gradle")
for root, dirs, files in os.walk(gradle_home):
    if "gradle.bat" in files:
        print("Found gradle.bat at:", os.path.join(root, "gradle.bat"))
    if "gradle-wrapper.jar" in files:
        print("Found gradle-wrapper.jar at:", os.path.join(root, "gradle-wrapper.jar"))
        break
