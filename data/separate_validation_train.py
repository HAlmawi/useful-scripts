#python separate_validation_train.py full_list train_name validation_name ratio
import sys
import random
import math
from file_functions import get_num_lines

full_list = open(sys.argv[1]).readlines()
save_train = sys.argv[2]
save_val = sys.argv[3]
split = float(sys.argv[4])

num_files = int(get_num_lines(sys.argv[1]))

divider = math.ceil(float (split * num_files))

array_files = [[i] for i in range(num_files)]
random.shuffle(array_files)

f_t = open(save_train,'w')
f_v = open(save_val,'w')

for i in range(num_files):
    if i < divider:
        f_v.write(full_list[int(array_files[i][0])])
    else:
        f_t.write(full_list[int(array_files[i][0])])

f_t.close()
f_v.close()
