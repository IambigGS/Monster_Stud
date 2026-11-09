with open('web/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
match = re.search(r'const bgmManager\s*=\s*\{[\s\S]*?\n\};\n', text)
if match:
    print(match.group(0))
else:
    print("bgmManager definition not found by regex")
