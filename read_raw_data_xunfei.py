# -*- coding: utf-8 -*-
# author: xieyuqiang
# email: xieyuqiang@iie.ac.cn
# 2021.11.30
# read raw_data from Xun Fei open platform, Yuyin Zhuanxie

import numpy as np
import json
import ast

# Demonstration
input_path = './raw_data.txt'
output_path = './result.txt'

f1= open(input_path)
lines = f1.readlines()
all_data_so = []
for line in lines:
    item = line.replace("\n", "").split("/getResult success:")[1]
    item = item.split("'[")[1]
    item = item.split("]'")[0]
    user_dicts = ast.literal_eval(item)
    for user_dict in user_dicts:
        all_data_so.append(user_dict['onebest'])

with open(output_path, 'w') as f2:
    f2.writelines(all_data_so)

f1.close()
f2.close()
