with open('web/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(7160, min(7230, len(lines))):
    ascii_line = lines[i].encode('ascii', errors='replace').decode('ascii')
    print(f"{i+1}: {ascii_line}", end='')
