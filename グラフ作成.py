import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
  
  
pil_image_color = Image.open('237.bmp')

plt.figure()

plt.imshow(pil_image_color)    

#plt.axvline(x=310)
plt.axvline(x=525,linestyle='dashed')

plt.savefig(f'si.jpg')