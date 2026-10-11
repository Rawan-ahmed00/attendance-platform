from PIL import Image, ImageDraw
import os

os.makedirs("school/static/school/icons", exist_ok=True)
for size in (192, 512):
    img = Image.new("RGB", (size, size), "#1e3a8a")
    d = ImageDraw.Draw(img)
    m = size // 5
    d.rounded_rectangle([m, m, size - m, size - m], radius=size // 10, fill="white")
    d.line([size // 2, m, size // 2, size - m], fill="#1e3a8a", width=max(2, size // 40))
    img.save(f"school/static/school/icons/icon-{size}.png")
print("done")
