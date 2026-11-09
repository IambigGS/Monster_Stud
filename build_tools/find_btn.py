import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('web/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if 'videoIntroSoundBtn' in l:
        print(f"{i+1}: {repr(l.strip())}")
