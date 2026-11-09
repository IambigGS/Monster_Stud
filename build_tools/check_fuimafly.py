import os

p = r"C:\bgs\all myAssets\0myApps-All\steve_arena\FUimAfly"
print("Exists:", os.path.exists(p))
if os.path.exists(p):
    for f in os.listdir(p):
        print(" ", f)

# Also check git config in that folder
git_config = os.path.join(p, ".git", "config")
if os.path.exists(git_config):
    print("\n--- .git/config ---")
    with open(git_config, 'r') as gf:
        print(gf.read())
