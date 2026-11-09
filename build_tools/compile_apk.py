import os
import sys
import subprocess
import shutil

userprofile = os.environ.get("USERPROFILE", "")
gradle_bat = os.path.join(userprofile, ".gradle", "wrapper", "dists", "gradle-8.13-bin", "5xuhj0ry160q40clulazy9h7d", "gradle-8.13", "bin", "gradle.bat")
java_home = r"C:\Program Files\Eclipse Adoptium\jdk-17.0.17.10-hotspot"
android_home = os.path.join(os.environ.get("LOCALAPPDATA", ""), "Android", "Sdk")

env = os.environ.copy()
env["JAVA_HOME"] = java_home
env["ANDROID_HOME"] = android_home
env["PATH"] = os.path.join(java_home, "bin") + ";" + env["PATH"]

android_dir = os.path.abspath("android")
print(f"Running gradle assembleRelease in {android_dir}...")

proc = subprocess.Popen(
    [gradle_bat, "assembleRelease", "--stacktrace"],
    cwd=android_dir,
    env=env,
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,
    text=True,
    bufsize=1
)

for line in iter(proc.stdout.readline, ''):
    print(line, end='', flush=True)

proc.stdout.close()
return_code = proc.wait()
print(f"\nGradle finished with return code: {return_code}")

if return_code == 0:
    apk_out = os.path.join(android_dir, "app", "build", "outputs", "apk", "release", "app-release.apk")
    if not os.path.exists(apk_out):
        apk_out = os.path.join(android_dir, "app", "build", "outputs", "apk", "release", "app-release-unsigned.apk")
    
    dest_dir = os.path.abspath(os.path.join("builds", "apk"))
    os.makedirs(dest_dir, exist_ok=True)
    
    dest_versioned = os.path.join(dest_dir, "MonsterStud-v1.0.1.apk")
    dest_alias = os.path.join(dest_dir, "MonsterStud-S21-Release.apk")
    
    if os.path.exists(apk_out):
        shutil.copyfile(apk_out, dest_versioned)
        shutil.copyfile(apk_out, dest_alias)
        print(f"SUCCESS! Versioned APK copied to: {dest_versioned}")
        print(f"File size: {os.path.getsize(dest_versioned):,} bytes")
    else:
        print("Build succeeded, but looking for output APK...")
        for r, d, f in os.walk(os.path.join(android_dir, "app", "build")):
            for file in f:
                if file.endswith(".apk"):
                    print("Found APK:", os.path.join(r, file))
else:
    sys.exit(return_code)
