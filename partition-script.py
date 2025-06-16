import os
import shutil
import random

# open files
CWD = os.getcwd()
dimensions = ["images","labels"]
dimensions_types = [".jpg",".json"]
file_dimensions = ["train","test","val"]


def make_copy(dimension,file_dimension,filename):
    from_file = os.path.join(CWD,"resources","bdd",dimension,file_dimension,filename)
    to_file = os.path.join(CWD,"resources","bdd-sample",dimension,file_dimension,filename)
    shutil.copy(from_file,to_file)

#given array choose rnd index
def choose_rnd(list):
    ind = random.randint(0,len(list))
    return ind if ind not in inds else choose_rnd(list)

for fd in file_dimensions:
    paths_train = sorted(os.listdir(os.path.join(CWD,"resources","bdd","images",fd)))

    inds = []

    rng = 5000
    if fd == "test":
        rng = 2000
    else:
        rng = 1000

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