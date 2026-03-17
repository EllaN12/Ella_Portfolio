"""
Run this once profile.jpg is saved in this folder:
  python process_photo.py
"""
from PIL import Image, ImageEnhance, ImageFilter
import os

INPUT  = "profile.jpg"
OUTPUT = "profile_processed.jpg"

img = Image.open(INPUT).convert("RGB")
w, h = img.size

# --- Crop: keep top 72% (head + torso) and center horizontally ---
crop_h = int(h * 0.72)
left   = int(w * 0.05)
right  = int(w * 0.95)
img    = img.crop((left, 0, right, crop_h))

# --- Resize to portrait card dimensions ---
img = img.resize((600, 720), Image.LANCZOS)

# --- Professional filters ---
img = ImageEnhance.Contrast(img).enhance(1.08)
img = ImageEnhance.Brightness(img).enhance(0.96)
img = ImageEnhance.Color(img).enhance(0.88)       # slight desaturation
img = ImageEnhance.Sharpness(img).enhance(1.15)

img.save(OUTPUT, "JPEG", quality=92)
print(f"Saved → {OUTPUT}")
