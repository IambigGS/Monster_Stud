import os

paths_to_check = [
    r"C:\bgs\all myAssets\0myApps-All\AWOTBOT dependances",
    r"C:\bgs\all myAssets\Telegram\Absolute Waste of Time",
    r"C:\bgs\all myAssets\0myApps-All\DanDan's Dinner - P2\telegram_minigame"
]

for p in paths_to_check:
    print(f"\nChecking: {p}")
    if os.path.exists(p):
        for root, dirs, files in os.walk(p):
            for f in files:
                if f.endswith(('.py', '.js', '.mjs', '.ts', '.json', '.env', '.txt', '.md')):
                    print("  File:", os.path.join(root, f))
