import os
import random

random.seed(777)

for root, dirs, files in os.walk("../out/"):
    for filename in files:
        # print("~/work/out/{}\t{}".format(filename, filename.split('_')[0]))
        pass

print(len(files))

random.shuffle(files)

n_train = int(len(files) * 0.8)
n_validation = int(len(files) * 0.1)
n_test = int(len(files) * 0.1)

print(n_train, n_validation, n_test)

train_files = files[:n_train]
validation_files = files[n_train:(n_train+n_validation)]
test_files = files[-n_test:]

train_f = open("gt_train.txt", "w")
i = 0
for filename in train_files:
    src_file = "../out/"+filename
    dst_file = "../data/train/"+filename
    os.rename(src_file, dst_file)
    print('../data/train/{0}\t{1}\n'.format(filename, filename.split('_')[0]))
    train_f.write('../data/train/{0}\t{1}\n'.format(filename, filename.split('_')[0]))
    i += 1

train_f.close()
print(i)

validation_f = open("gt_validation.txt", "w")
i = 0
for filename in train_files:
    src_file = "../out/"+filename
    dst_file = "../data/valid/"+filename
    os.rename(src_file, dst_file)
    print('../data/valid/{0}\t{1}\n'.format(filename, filename.split('_')[0]))
    validation_f.write('../data/valid/{0}\t{1}\n'.format(filename, filename.split('_')[0]))
    i += 1

validation_f.close()
print(i)

test_f = open("gt_test.txt", "w")
i = 0
for filename in train_files:
    src_file = "../out/"+filename
    dst_file = "../data/test/"+filename
    os.rename(src_file, dst_file)
    print('../data/test/{0}\t{1}\n'.format(filename, filename.split('_')[0]))
    test_f.write('../data/test/{0}\t{1}\n'.format(filename, filename.split('_')[0]))
    i += 1

test_f.close()
print(i)

