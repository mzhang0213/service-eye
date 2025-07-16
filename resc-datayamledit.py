# use this script to generate the first 3 rows for windows
import os

CWD = os.getcwd()
DATA_DIR = "yolodata" # or wherever data for training is stored

print(f"path: {os.path.join(CWD, "resources", DATA_DIR)}")
print(f"train: {os.path.join(CWD, "resources", DATA_DIR, "train")}")
print(f"val: {os.path.join(CWD, "resources", DATA_DIR, "val")}")

# take console output and copy to data.yaml