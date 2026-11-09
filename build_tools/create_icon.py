import os
from PIL import Image

src_img = os.path.join('media_assets', 'extracted_art', 'special_genes', 'primal_apex.webp')
out_dir = os.path.join('build_tools', 'windows_app')
os.makedirs(out_dir, exist_ok=True)
out_ico = os.path.join(out_dir, 'app_icon.ico')

im = Image.open(src_img).convert('RGBA')

w, h = im.size
min_dim = min(w, h)
left = (w - min_dim) // 2
top = (h - min_dim) // 2
im_cropped = im.crop((left, top, left + min_dim, top + min_dim))

sizes = [(256, 256), (128, 128), (64, 64), (48, 48), (32, 32), (16, 16)]
im_cropped.save(out_ico, format='ICO', sizes=sizes)
print(f"Generated icon: {out_ico} ({os.path.getsize(out_ico)} bytes)")
