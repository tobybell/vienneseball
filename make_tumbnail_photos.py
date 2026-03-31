from PIL import Image
import os

full_folder = "photos-26"
thumb_folder = "photos-26-thumbs"

os.makedirs(thumb_folder, exist_ok=True)

for i in range(1, 622):
    filename = f"photo{i}.jpg"
    src_path = os.path.join(full_folder, filename)
    dst_path = os.path.join(thumb_folder, filename)

    if not os.path.exists(src_path):
        print(f"Skipping missing file: {src_path}")
        continue

    try:
        with Image.open(src_path) as img:
            img = img.convert("RGB")
            img.thumbnail((320, 320))
            img.save(dst_path, "JPEG", quality=70, optimize=True)
            print(f"Created thumbnail: {dst_path}")
    except Exception as e:
        print(f"Error with {src_path}: {e}")