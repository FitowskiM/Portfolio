import os

def batch_rename(folder_path, prefix):
    for count, filename in enumerate(os.listdir(folder_path)):
        file_extension = os.path.splitext(filename)[1]
        new_name = f"{prefix}_{count}{file_extension}"
        src = os.path.join(folder_path, filename)
        dst = os.path.join(folder_path, new_name)
        os.rename(src, dst)
    print(f"Renamed {count + 1} files successfully.")

# Example usage
# batch_rename("path/to/your/folder", "newfile")