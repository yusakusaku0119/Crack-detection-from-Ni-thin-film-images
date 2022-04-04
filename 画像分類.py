import json
import os
import glob
import shutil

import numpy as np
import cv2
from PIL import Image
import matplotlib.pyplot as plt
import re
IMAGE_SIZE = 1024

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    return [ atoi(c) for c in re.split(r'(\d+)', text) ]

json_list= sorted(glob.glob('bright/*.json'), key=natural_keys)
img_list = [f.replace('.json', '.bmp') for f in json_list]
print(len(json_list))


no = 3
 
# アノテーションデータ読み込み
with open(json_list[no]) as f:
 data = json.loads(f.read())
    
# 1つだけ取り出す
shapes= data['shapes'][0]
label = shapes['label']
points = shapes['points']
shape_type = shapes['shape_type']
print('[label]', label)
print('[shape_type]', shape_type)
print('[points]', points)

img = cv2.imread(img_list[no])
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
 
# アノテーション部分
mask = np.zeros((img.shape[0], img.shape[1],img.shape[2]), np.uint8)
mask = cv2.fillPoly(mask, np.int32([points]), (255,0,0))
cv2.imwrite('sample.jpg',mask)


 
# 横並びに表示
fig = plt.figure(figsize=(12, 6))
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)
ax1.imshow(img)
ax2.imshow(mask, cmap='gray')


plt.show()

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
    points = []
    with open(file) as f:
        data = json.loads(f.read())
        for s in data['shapes']:
            points.append(s['points'])
           
    
    if points:
        # 画像データを読み込み画像サイズ取得
        img_path = file.replace('json', 'bmp')
        img = cv2.imread(img_path)
        
 
        # ファイル名
        file_name = os.path.basename(img_path)
 
        # jsonのアノテーションデータ
        # 犬：1
        # 背景：0
        mask = np.zeros((img.shape[0], img.shape[1]), dtype=np.uint8)
        for p in points:
            mask = cv2.fillPoly(mask, np.int32([p]),(255,255,255))
            
        
        
            
            
        
 
        # リサイズ
        img = cv2.resize(img, (IMAGE_SIZE, IMAGE_SIZE), interpolation=cv2.INTER_LANCZOS4)
        mask = cv2.resize(mask, (IMAGE_SIZE, IMAGE_SIZE), interpolation=cv2.INTER_LANCZOS4)
 
        # 保存
        file_name = file_name.replace('bmp', 'png')
        if ind<(len(json_list)-2):
            maskim = Image.fromarray(np.uint8(mask))
            maskim.save(f'train/masks/{file_name}')
            cv2.imwrite(f'train/images/{file_name}', img)
        else:
            maskim = Image.fromarray(np.uint8(mask))
            maskim.save(f'val/masks/{file_name}')
            cv2.imwrite(f'val/images/{file_name}', img)

