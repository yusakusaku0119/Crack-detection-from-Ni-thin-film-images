import cv2
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

from PIL import Image

IMAGE_SIZE=1024
img=cv2.imread('200.bmp')
mask=cv2.imread('.result200.jpg')

img = cv2.resize(img, (IMAGE_SIZE, IMAGE_SIZE), interpolation=cv2.INTER_LANCZOS4)
mask = cv2.resize(mask, (IMAGE_SIZE, IMAGE_SIZE), interpolation=cv2.INTER_LANCZOS4)

fig = plt.figure(figsize=(12, 6))
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)
ax1.imshow(img)
ax2.imshow(mask, cmap='cool')

plt.show()