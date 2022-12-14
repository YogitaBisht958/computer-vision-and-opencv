# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 09:29:45 2019

@author: jain
"""

from pyimagesearch.transform import four_point_transform
from skimage.filters import threshold_local
import numpy as np
import argparse
import cv2
import imutils

ap = argparse.ArgumentParser()

ap.add_argument("-i","--image", required = True, help = "path to the image to be scanned")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
ratio = image.shape[0]/500.0
orig = image.copy()
image = imutils.resize(image, height=500)
#cv2.imshow("original",orig)
#cv2.waitKey(0)
#cv2.imshow("resized", image)
#cv2.waitKey(0)

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

gray = cv2.GaussianBlur(gray,(5,5),0)
edged = cv2.Canny(gray,50,150)
#cv2.imshow("Image", image)
#cv2.imshow("Canny", edged)
#cv2.waitKey(0)

cnts = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
cnts = sorted(cnts, key= cv2.contourArea, reverse=True)[:5]

for c in cnts:
    peri = cv2.arcLength(c,True)
    approx = cv2.approxPolyDP(c, 0.02 * peri, True)
    
    if len(approx)==4:
        screenCnt  = approx
        break

print("Find contours of the paper")
cv2.drawContours(image, [screenCnt], -1, [0,255,0], 2)

warped = four_point_transform(orig, screenCnt.reshape(4,2)*ratio)

warped = cv2.cvtColor(warped, cv2.COLOR_BGR2GRAY)
T = threshold_local(warped, 11, offset = 10, method = "gaussian")
warped = (warped > T).astype("uint8") * 255
 
# show the original and scanned images
print("STEP 3: Apply perspective transform")
cv2.imshow("Original", imutils.resize(orig, height = 650))
cv2.imshow("Scanned", imutils.resize(warped, height = 650))
cv2.waitKey(0)













