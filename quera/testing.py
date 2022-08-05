import cv2 as cv
import time
import numpy as np
import matplotlib.pyplot as plt


image_path = '.\Desktop\IMG.jpg'
image_path2 = '.\Desktop/text.png'
img = cv.imread(image_path)
img_r = cv.resize(img, (img.shape[1] // 4, img.shape[0] // 4))
pos1 = img_r.shape[1] // 2
pos2 =  img_r.shape[0] // 2

def translate(img, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

def rotate(img, angle, axis = None):
    (height, width) = img.shape[:2]
    
    if axis is None:
        axis = (width // 2, height // 2)

    rotated = cv.getRotationMatrix2D(axis, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotated, dimensions) 
blur = cv.GaussianBlur(img_r, (5,5), 0)
converted = cv.cvtColor(img_r, cv.COLOR_BGR2RGB)
plt.imshow(converted)
#plt.show()
canny1 = cv.Canny(blur, 135, 175)
canny2 = cv.Canny(img_r, 135, 175)
rotated = rotate(img_r, 50)
translated = translate(img_r, 100, 100)
cv.imshow('blurred', blur)
#cv.imshow('rotate', rotated)
#cv.imshow('shift', translated)
cv.imshow('canny1', canny1)
cv.imshow('canny2', canny2)
cv.imshow('org', img_r)
cv.waitKey(0)
"""
cv.rectangle(img_r, (pos2 - 50, pos1 - 50), (pos2 + 50, pos1 + 50), (0,255,0), thickness = 2)
cv.line(img_r , (pos2 - 100, pos1 + 10), (pos2 + 10, pos2 + 30), (255,0,0), thickness = 4)
cv.imshow('show', img_r)
cv.waitKey(0)

#capture = cv.VideoCapture('.\Desktop\ink_blots.mov')
capture = cv.VideoCapture(0)
time.sleep(1.000)
while True:
    isTrue, frame = capture.read()
    canny = cv.Canny(frame, 115, 185)
    cv.imshow('vid', canny)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
"""