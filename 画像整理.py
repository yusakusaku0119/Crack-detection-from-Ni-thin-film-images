import json
import os
import glob
import shutil

import numpy as np
import cv2
from PIL import Image
import matplotlib.pyplot as plt
import re

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    return [ atoi(c) for c in re.split(r'(\d+)', text) ]

json_list= sorted(glob.glob('i/*.png'), key=natural_keys)

train_dir = 'train'
val_dir = 'val'
if not os.path.exists(train_dir):
    os.mkdir(train_dir)
    os.mkdir(train_dir + '/images')
    os.mkdir(train_dir + '/masks')
if not os.path.exists(val_dir):
    os.mkdir(val_dir)
    os.mkdir(val_dir + '/images')
    os.mkdir(val_dir + '/masks')

for ind, file in enumerate(json_list):
             
        # 保存
        file_name = file_name.replace('png', 'png')
        if ind<(len(json_list)-20):
            cv2.imwrite(f'train/images/{file_name}', img)
        else:
            cv2.imwrite(f'val/images/{file_name}', img)