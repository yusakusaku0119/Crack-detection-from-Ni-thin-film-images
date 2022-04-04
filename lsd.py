import cv2
import time
from pylsd.lsd import lsd

import numpy as np

img = cv2.imread('166_sen.png')
img = cv2.resize(img,(int(img.shape[1]/5),int(img.shape[0]/5)))
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray,(5,5),5)

t1 = time.time()
edges = cv2.Canny(gray,50,150,apertureSize = 3)
linesH = cv2.HoughLinesP(edges, rho=1, theta=np.pi/360, threshold=50, minLineLength=50, maxLineGap=7)
t2 = time.time()

linesL = lsd(gray)
t3 = time.time()

img2 = img.copy()

for line in linesH:
    x1, y1, x2, y2 = line[0]

    # 赤線を引く
    img2 = cv2.line(img2, (x1,y1), (x2,y2), (0,0,255), 2)

cv2.imwrite('edges.jpg',img2)

