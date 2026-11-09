import os, subprocess

sdk = os.path.join(os.environ.get("LOCALAPPDATA", ""), "Android", "Sdk")
emulator = os.path.join(sdk, "emulator", "emulator.exe")

env = os.environ.copy()
env["ANDROID_HOME"] = sdk
env["ANDROID_SDK_ROOT"] = sdk

res = subprocess.run([emulator, "-avd", "Medium_Phone", "-gpu", "swiftshader_indirect", "-no-boot-anim", "-verbose"], capture_output=True, text=True, timeout=10, env=env)
print("Return code:", res.returncode)
print("STDOUT:\n", res.stdout[:500])
print("STDERR:\n", res.stderr[:500])
