# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 11:52:55 2019

@author: Meena
"""

import cv2
import numpy as np
import matplotlib as plt

 
if __name__ == '__main__' :
 
    # Read image
    im = cv2.imread("stock_flower.jpg")
     
    # Select ROI
    fromCenter = False
    r = cv2.selectROI(im, fromCenter)
     
    # Crop image
    imCrop = im[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]
 
    # Display cropped image
    #cv2.imshow("Image", imCrop)
    #cv2.waitKey(0)
    plt.imshow(imCrop)
    plt.show
    plt.axis('off')