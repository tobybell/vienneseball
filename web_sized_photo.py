from PIL import Image
import os

# === SETTINGS ===
INPUT_FOLDER = "photos-26"
OUTPUT_FOLDER = "photos-26-web"
MAX_SIZE = 1600        # max width or height (px)
QUALITY = 80           # 70–85 is a good range
START_INDEX = 622
END_INDEX = 1515        # change if needed

# =================

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def process_image(input_path, output_path):
    try:
        with Image.open(input_path) as img:
            img = img.convert("RGB")

            # Resize while maintaining aspect ratio
            img.thumbnail((MAX_SIZE, MAX_SIZE))

            # Save optimized
            img.save(
                output_path,
                "JPEG",
                quality=QUALITY,
                optimize=True,
                progressive=True
            )

    except Exception as e:
        print(f"❌ Error processing {input_path}: {e}")


print("🚀 Creating web-sized images...\n")

for i in range(START_INDEX, END_INDEX + 1):
    filename = f"photo{i}.jpg"

    input_path = os.path.join(INPUT_FOLDER, filename)
    output_path = os.path.join(OUTPUT_FOLDER, filename)

    if not os.path.exists(input_path):
        print(f"⚠️ Missing: {input_path}")
        continue

    process_image(input_path, output_path)
    print(f"✅ {filename}")

print("\n🎉 Done! Web images saved to:", OUTPUT_FOLDER)