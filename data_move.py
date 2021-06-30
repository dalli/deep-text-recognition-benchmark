import os

for root, dirs, files in os.walk("../data/train/"):
    for filename in files:
        pass

for filename in files:
    src_file = '../data/train/'+filename
    dst_file = '../out/'+filename
    print("{}\t{}".format(src_file, dst_file))
    os.rename(src_file, dst_file)

