import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('427.bmp',0)
edges = cv2.Canny(img,50,100)

plt.subplot(121),plt.imshow(img,cmap = 'Greens')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'summer')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

plt.show()

cv2.imwrite('427.jpg',edges)

print('aaa')