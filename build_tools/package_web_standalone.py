import os
import zipfile

src_dir = 'web'
dest_zip = os.path.join('builds', 'web-standalone', 'MonsterStud-Web-v1.0.0.zip')

os.makedirs(os.path.dirname(dest_zip), exist_ok=True)

with zipfile.ZipFile(dest_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(src_dir):
        for file in files:
            full_path = os.path.join(root, file)
            rel_path = os.path.relpath(full_path, src_dir)
            zipf.write(full_path, rel_path)

size_mb = os.path.getsize(dest_zip) / (1024 * 1024)
print(f"Created {dest_zip} ({size_mb:.2f} MB)")
