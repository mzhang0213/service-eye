import os
import shutil
import random

# open files
CWD = os.getcwd()
dimensions = ["images","labels"]
dimensions_types = [".jpg",".json"]
file_dimensions = ["train","test","val"]
RAW_DIR = "bdd"
DATA_DIR = "yolodata"

def make_copy(dimension,file_dimension,filename):
    from_file = os.path.join(CWD,"resources","bdd",dimension,file_dimension,filename)
    to_file = os.path.join(CWD,"resources",DATA_DIR,dimension,file_dimension)
    if not os.path.exists(to_file):
        os.makedirs(to_file)
    shutil.copy(from_file,to_file)

#given array choose rnd index
def choose_rnd(list):
    ind = random.randint(0,len(list))
    return ind if ind not in inds and list[ind][:1] != "." else choose_rnd(list)

for fd in file_dimensions:
    paths_train = (sorted(os.listdir(os.path.join(CWD,"resources",RAW_DIR,"images",fd))))

    inds = []

    rng = 5000
    if fd == "train":
        rng = 4000
    else:
        rng = 2000

    for i in range(rng):
        inds.append(choose_rnd(paths_train))

    sample_files = []
    for i in inds:
        file = paths_train[i]
        file = file[:-4] #remove extension
        sample_files.append(file)

    for i in range(len(sample_files)):
        for d in range(len(dimensions)):
            make_copy(dimensions[d],fd,sample_files[i]+dimensions_types[d])