import os

fuimafly_dir = r"C:\bgs\all myAssets\0myApps-All\steve_arena\FUimAfly"

for root, dirs, files in os.walk(fuimafly_dir):
    # skip node_modules and .git
    if 'node_modules' in root or '.git' in root or 'dist' in root:
        continue
    for f in files:
        if f.endswith(('.md', '.json', '.ts', '.js', '.html', '.yml')):
            fp = os.path.join(root, f)
            try:
                with open(fp, 'r', encoding='utf-8', errors='ignore') as file:
                    content = file.read()
                    if 'github.io' in content.lower() or 'telegram' in content.lower():
                        print(f"Match in {f} ({fp}):")
                        for line in content.splitlines():
                            if 'github.io' in line.lower() or 'telegram' in line.lower():
                                print("  ", line.strip()[:120])
            except Exception:
                pass
