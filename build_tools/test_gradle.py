import os, subprocess

userprofile = os.environ.get("USERPROFILE", "")
gradle_bat = os.path.join(userprofile, ".gradle", "wrapper", "dists", "gradle-8.13-bin", "5xuhj0ry160q40clulazy9h7d", "gradle-8.13", "bin", "gradle.bat")
java_home = r"C:\Program Files\Eclipse Adoptium\jdk-17.0.17.10-hotspot"
android_home = os.path.join(os.environ.get("LOCALAPPDATA", ""), "Android", "Sdk")

env = os.environ.copy()
env["JAVA_HOME"] = java_home
env["ANDROID_HOME"] = android_home
env["PATH"] = os.path.join(java_home, "bin") + ";" + env["PATH"]

res = subprocess.run([gradle_bat, "--version"], capture_output=True, text=True, env=env)
print("Exit code:", res.returncode)
print(res.stdout[:500])
