import cv2
from cv2 import imwrite


for num in [6,7,9,11,15,17,24,27,77,82,88,89,92,93,111,113,121,125,160,164,357,436,441,451]:
    img2=(f'sabun_right/{num}.png')
    img3=cv2.imread(img2)
    img3=cv2.bitwise_not(img3)
    cv2.imwrite(f'sabun_right/{num}.jpg',img3)