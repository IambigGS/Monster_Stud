import os, sys, shutil

userprofile = os.environ.get("USERPROFILE", "")
gradle_home = os.path.join(userprofile, ".gradle")
print(".gradle exists:", os.path.exists(gradle_home))
if os.path.exists(gradle_home):
    wrapper_dists = os.path.join(gradle_home, "wrapper", "dists")
    if os.path.exists(wrapper_dists):
        print("Gradle dists:", os.listdir(wrapper_dists))
