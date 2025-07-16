import os
import shutil


CWD = os.getcwd()
base = os.path.join(CWD,"resources")
def get_folder(folder):
    print(folder)
    sub = os.listdir(folder)
    directories = []
    for item in sub:
        item_path = os.path.join(folder, item)
        if os.path.isdir(item_path):
            directories.append(item)
    print(" ".join(directories))
    inp = input("what folder or done\n")
    if inp=="done":
        return folder
    elif inp not in sub:
        print("bruh not a folder")
        return get_folder(folder)
    else:
        return get_folder(os.path.join(folder,inp))

res = get_folder(base)

for filename in os.listdir(res):
    file_path = os.path.join(res, filename)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    except Exception as e:
        print(f"Failed to delete {file_path}. Reason: {e}")

