import os

# folder containing your photos
folder = "photos-26"

# get all files (ignore hidden files like .DS_Store)
files = [f for f in os.listdir(folder) if not f.startswith(".")]

# sort files so ordering is consistent
files.sort()

# rename files
for i, filename in enumerate(files, start=622):
    old_path = os.path.join(folder, filename)

    # keep original file extension
    ext = os.path.splitext(filename)[1]

    new_name = f"photo{i}{ext}"
    new_path = os.path.join(folder, new_name)

    os.rename(old_path, new_path)

    print(f"{filename} -> {new_name}")