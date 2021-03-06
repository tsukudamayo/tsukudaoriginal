import numpy as np
import matplotlib.pyplot as plt

import cv2


img1 = cv2.imread('messi5.jpg')
img2 = cv2.imread('opencv-logo.png')

# img1 = cv2.resize(img1, (256,256))
img2 = cv2.resize(img2, (64,64))

print('img1.shape ', img1.shape)
print('img2.shape ', img2.shape)

# I want to put logo on top-lerft corner, So I create a ROI
rows, cols, channels = img2.shape
print('row, cols, channels', rows, cols, channels)
roi = img1[0:rows, 0:cols]
print('roi ', roi)

# Now create a mask of logo and create its inverse mask also
img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

# Now black-out the area of logo in ROI
img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)

# Take only region of lofo in ROI
img2_fg = cv2.bitwise_and(img2, img2, mask=mask)

# Put logo in ROI and modify the main image
dst = cv2.add(img1_bg, img2_fg)
img1[0:rows, 0:cols] = dst

cv2.imshow('res', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()

