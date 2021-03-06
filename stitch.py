# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 21:15:33 2019

@author: prans
"""

# import the necessary packages
from panorama import Stitcher
import imutils
import cv2
 

# load the two images and resize them to have a width of 400 pixels
# (for faster processing)
imageA = cv2.imread('download.png',0)
imageB = cv2.imread('download2.png',0)
imageA = imutils.resize(imageA, width=400)
imageB = imutils.resize(imageB, width=400)
 
# stitch the images together to create a panorama
stitcher = Stitcher()
(result, vis) = stitcher.stitch([imageA, imageB], showMatches=True)
 
# show the images
cv2.imshow("Image A", imageA)
cv2.imshow("Image B", imageB)
cv2.imshow("Keypoint Matches", vis)
cv2.imshow("Result", result)
cv2.waitKey(0)