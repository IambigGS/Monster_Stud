import os

search_terms = ['fuimafly', 'awhatvibe', 'awotbot', 'telegram']

def scan_dir(base_path, depth=2):
    if depth < 0 or not os.path.exists(base_path):
        return
    try:
        entries = os.listdir(base_path)
    except Exception:
        return
    for e in entries:
        full = os.path.join(base_path, e)
        e_lower = e.lower()
        if any(term in e_lower for term in search_terms):
            print(f"MATCH: {full}")
        if os.path.isdir(full) and depth > 0:
            scan_dir(full, depth - 1)

print("Scanning C:\\bgs...")
scan_dir("C:\\bgs", depth=3)
