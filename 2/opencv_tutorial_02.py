# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 09:06:49 2019

@author: jain
"""

import argparse
import imutils
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i","--image",required = True, help = "Path to image file")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Image",image)
cv2.waitKey(0)

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray",gray)
cv2.waitKey(0)

edged = cv2.Canny(gray,30,150)
cv2.imshow("Canney edged", edged)
cv2.waitKey(0)

thresh = cv2.threshold(gray,225,255,cv2.THRESH_BINARY_INV)[1]
cv2.imshow("Threshold",thresh)
cv2.waitKey(0)

cnts = cv2.findContours(thresh.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
output = image.copy()

for c in cnts:
    cv2.drawContours(output,[c],-1,(240,0,159),3)
    cv2.imshow("Contours", output)
    cv2.waitKey(0)
    
text = "I found {} objects".format(len(cnts))
cv2.putText(output, text, (10,25),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (240,0,159),2)
cv2.imshow("Contours", output)
cv2.waitKey(0)

#erosion
mask = thresh.copy()
mask = cv2.erode(mask,None, iterations=5)
cv2.imshow("Eroded", mask)
cv2.waitKey(0)

#Dilation
mask = thresh.copy()
mask = cv2.dilate(mask, None, iterations=5)
#mask = cv2.erode(mask,None, iterations=15)
cv2.imshow("Dilate", mask)
cv2.waitKey(0)

# Masking
mask = thresh.copy()
output = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Output", output)
cv2.waitKey(0)