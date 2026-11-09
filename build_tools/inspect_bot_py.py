import os

bot_py = r"C:\bgs\all myAssets\Telegram\Absolute Waste of Time\AWOTvibeCode\bot-V2.py"
if os.path.exists(bot_py):
    with open(bot_py, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    print(f"Read {len(lines)} lines from bot-V2.py")
    for i, line in enumerate(lines):
        l_lower = line.lower()
        if 'webapp' in l_lower or 'game' in l_lower or 'fuimafly' in l_lower or 'mini' in l_lower:
            print(f"{i+1}: {line.strip()}")
