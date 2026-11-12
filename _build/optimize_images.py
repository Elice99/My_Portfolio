#!/usr/bin/env python3
"""
Convert portfolio images to WebP so the site ships far less data.

Run from anywhere:
    python _build/optimize_images.py

Originals are kept untouched. New files sit next to them with a .webp
extension. Both the build script and the browser image loader prefer WebP,
so the site picks them up automatically on the next build.

Re-run this after replacing a photo if you keep the same filename, because
an existing .webp will otherwise win over the newer .jpg/.png.
"""
import os
import sys

try:
    from PIL import Image, ImageOps
except ImportError:
    sys.exit("Pillow is required: python -m pip install Pillow")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMAGES = os.path.join(ROOT, "images")
SOURCE_EXTS = (".png", ".jpg", ".jpeg")
QUALITY = 84
SCREENSHOT_MAX_WIDTH = 1600
PROFILE_MAX_WIDTH = 1000


def max_width_for(name):
    # Profile photos are displayed at 180-400 CSS px; 1000 keeps them sharp
    # on 2x screens without shipping a multi-megapixel file.
    return PROFILE_MAX_WIDTH if name.startswith("Elice_") else SCREENSHOT_MAX_WIDTH


def convert(path):
    name = os.path.splitext(os.path.basename(path))[0]
    dst = os.path.join(IMAGES, name + ".webp")
    if os.path.isfile(dst) and os.path.getmtime(dst) >= os.path.getmtime(path):
        return None

    with Image.open(path) as img:
        img = ImageOps.exif_transpose(img)
        has_alpha = img.mode in ("RGBA", "LA") or (
            img.mode == "P" and "transparency" in img.info
        )
        img = img.convert("RGBA" if has_alpha else "RGB")

        max_w = max_width_for(name)
        if img.width > max_w:
            new_h = round(img.height * max_w / img.width)
            img = img.resize((max_w, new_h), Image.LANCZOS)

        img.save(dst, "WEBP", quality=QUALITY, method=6)

    old_size = os.path.getsize(path)
    new_size = os.path.getsize(dst)
    # Flat screenshots of tables sometimes compress better as PNG. If WebP
    # did not actually help, keep the original and remove the new file.
    if new_size >= old_size:
        os.remove(dst)
        return ("kept", path, old_size)
    return ("ok", path, old_size, new_size)


def main():
    if not os.path.isdir(IMAGES):
        sys.exit("No images/ folder found at " + IMAGES)

    before = after = 0
    converted = 0
    for entry in sorted(os.listdir(IMAGES)):
        if not entry.lower().endswith(SOURCE_EXTS):
            continue
        src = os.path.join(IMAGES, entry)
        result = convert(src)
        if not result:
            continue
        if result[0] == "kept":
            _, _, old_size = result
            before += old_size
            after += old_size
            print(f"{entry:44} {old_size/1024:8.0f} KB    kept original (WebP was not smaller)")
            continue
        _, _, old_size, new_size = result
        before += old_size
        after += new_size
        converted += 1
        saved = 100 - (new_size / old_size * 100)
        print(f"{entry:44} {old_size/1024:8.0f} KB -> {new_size/1024:7.0f} KB  ({saved:4.0f}% smaller)")

    if not converted:
        print("Nothing to do - every source image already has a newer .webp.")
        return

    print()
    print(f"Converted {converted} images")
    print(f"Total: {before/1024/1024:.1f} MB -> {after/1024/1024:.1f} MB "
          f"({100 - (after / before * 100):.0f}% smaller)")


if __name__ == "__main__":
    main()
