import os

userprofile = os.environ.get("USERPROFILE", "")
android_dir = os.path.join(userprofile, ".android")
for f in os.listdir(android_dir):
    if "log" in f.lower() or "err" in f.lower() or f.endswith(".txt"):
        print("Log file:", f)
        p = os.path.join(android_dir, f)
        if os.path.isfile(p):
            try:
                with open(p, "r", encoding="utf-8", errors="ignore") as lf:
                    lines = lf.readlines()
                    print(f"--- {f} (last 10 lines) ---")
                    for l in lines[-10:]:
                        print(l.strip())
            except Exception as e:
                print("Error reading:", e)
