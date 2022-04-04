import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import glob

for num in [250]:
  img1=(f'.result{num}.jpg')
  img2=(f'{num}.jpg')
  img = cv2.imread(img1, cv2.IMREAD_GRAYSCALE)
  img3=cv2.imread(img2,cv2.IMREAD_GRAYSCALE)

  #print(np.unique(img))  # [  0 255]

  points = np.column_stack(np.where(img == 0))
  points3 = np.column_stack(np.where(img3==0))
  #print(points)
  #print(len(points))
  new_list=[i for i in points[:,1] if (i<900) and (i>200)]
  new_list3=[i for i in points3[:,1] if (i>0)]
  print(new_list)
  print(f'検出結果{num}')
  print(min(new_list))
  print('正解')
  print(min(new_list3))
  print('差')
  print(min(new_list)-min(new_list3))



  pil_image_color = Image.open(img1)

  plt.figure()

  plt.imshow(pil_image_color)    

  plt.axvline(x=min(new_list))

  plt.savefig(f'kekka1_{num}'+'.jpg')

