# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 08:25:25 2019

@author: Meena
"""
'''
import cv2
import matplotlib.pyplot as plt 

# load the image
image = cv2.imread("vase.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

(h, w) = image.shape[:2]
center = (w / 2, h / 2)

# rotate the image by x degrees
M = cv2.getRotationMatrix2D(center,180, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
plt.imshow(rotated)
plt.show()
plt.axis('off')

'''
#crop using ROI
import cv2
import numpy as np
import matplotlib.pyplot as plt 
 
if __name__ == '__main__' :
 
    # Read image
    im = cv2.imread("home.jpg")
    im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)

     
    # Select ROI
    fromCenter = False
    r = cv2.selectROI("Image", im, fromCenter)
     
    # Crop image
    imCrop = im[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]
 
    # Display cropped image
    #cv2.imshow("Image", imCrop)
    #cv2.waitKey(0)
    plt.imshow(imCrop)
    plt.show()
    plt.axis('off')

