import os
import shutil

def organize_files(folder_path):
    for filename in os.listdir(folder_path):
        src_path = os.path.join(folder_path, filename)
        if os.path.isfile(src_path):
            file_ext = filename.split('.')[-1]
            dest_dir = os.path.join(folder_path, file_ext.upper())
            os.makedirs(dest_dir, exist_ok=True)
            shutil.move(src_path, os.path.join(dest_dir, filename))
    print("Files organized successfully.")

# Example usage
# organize_files("path/to/your/folder")