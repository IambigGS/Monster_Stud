import os

userprofile = os.environ.get("USERPROFILE", "")
modules = os.path.join(userprofile, ".gradle", "caches", "modules-2", "files-2.1")
if os.path.exists(modules):
    agp_dir = os.path.join(modules, "com.android.tools.build", "gradle")
    if os.path.exists(agp_dir):
        print("Cached AGP versions:", os.listdir(agp_dir))
    else:
        print("No cached AGP found")
else:
    print("No modules-2 cache")
