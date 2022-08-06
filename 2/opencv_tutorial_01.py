# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 17:04:09 2019

@author: jain
"""

import imutils
import cv2

image = cv2.imread("jp.png")
(h,w,d) = image.shape
print("width={}, height={},depth={}".format(w,h,d))

cv2.imshow("Image", image)
cv2.waitKey(0)

(B,G,R) = image[100,50]
print("R={},G={},B={}".format(R,G,B))

# slicing and cropping
roi = image[60:160,320:420]
cv2.imshow("ROI", roi)
cv2.waitKey(0)

######## resizing #########
# resizing images ignoring the aspect ratio
resized = cv2.resize(image,(200,200))
cv2.imshow("Resized", resized)
cv2.waitKey(0)

# resizing the image wrt the aspect ratio cv2.resize(image, (w,h))
r = 300.0/w
dim = (300,int(h*r))
resized = cv2.resize(image,dim)
cv2.imshow("Resized with aspect ratio",resized)
cv2.waitKey(0)

# resizing with imutils with aspect ratio preserved
resized_1 = imutils.resize(image,width=300)
cv2.imshow("Resized using imutils",resized_1)
cv2.waitKey(0)

######## rotating ##########
# using cv
center = (w//2,h//2)
M = cv2.getRotationMatrix2D(center,-45,1.0)
rotated = cv2.warpAffine(image, M, (w,h))
cv2.imshow("Rotated", rotated)
cv2.waitKey(0)

# using inutils
rotated_1 = imutils.rotate(image, -45)
cv2.imshow("Rotated using imutils", rotated_1)
cv2.waitKey(0)

# bounded rotation using imutils
rotate_bounded = imutils.rotate_bound(image, -45)
cv2.imshow("Bounded rotation using imutils", rotate_bounded)
cv2.waitKey(0)

#####################
# blurring or smoothing
blurred = cv2.GaussianBlur(image,(11,11),0)
cv2.imshow("Blurred", blurred)
cv2.waitKey(0)

######## drawing on an image ##########
# Rectangle
output = image.copy()
cv2.rectangle(output, (320,60),(420,160),(0,0,255),2)
cv2.imshow("Rectangle", output)
cv2.waitKey(0)

# solid circle
output_1 = image.copy()
cv2.circle(output_1, (300,150),20,(255,0,0),-1)
cv2.imshow("Circel", output_1)
cv2.waitKey(0)

# line
output_2 = image.copy()
line = cv2.line(output_2, (60,20),(400,200),(0,0,255),5)
cv2.imshow("Line",line)
cv2.waitKey(0)

# text on the image
output_3 = image.copy()
cv2.putText(output_3, "OpenCV + Jurassic Park!!", (0,0),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,0),2)
cv2.imshow("Text", output_3)
cv2.waitKey(0)


























