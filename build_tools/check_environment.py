import os, sys, shutil

print("JAVA_HOME:", os.environ.get("JAVA_HOME"))
print("ANDROID_HOME:", os.environ.get("ANDROID_HOME"))
print("ANDROID_SDK_ROOT:", os.environ.get("ANDROID_SDK_ROOT"))

localappdata = os.environ.get("LOCALAPPDATA", "")
possible_sdk = os.path.join(localappdata, "Android", "Sdk")
print("Standard Sdk exists:", os.path.exists(possible_sdk))
if os.path.exists(possible_sdk):
    print("Sdk contents:", os.listdir(possible_sdk))
    platforms = os.path.join(possible_sdk, "platforms")
    if os.path.exists(platforms):
        print("Platforms:", os.listdir(platforms))
    build_tools = os.path.join(possible_sdk, "build-tools")
    if os.path.exists(build_tools):
        print("Build tools:", os.listdir(build_tools))
