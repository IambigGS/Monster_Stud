import sys

with open('web/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'setupMonsterStudVideoIntro' in line or 'bgmManager =' in line or 'bgmToggleBtn' in line:
        start = max(0, i - 10)
        end = min(len(lines), i + 60)
        sys.stdout.write(f"\n=== Block around line {i+1} ===\n")
        for j in range(start, end):
            ascii_line = lines[j].encode('ascii', errors='replace').decode('ascii')
            sys.stdout.write(f"{j+1}: {ascii_line}")
