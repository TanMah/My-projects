# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 11:45:30 2019

@author: Meena
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

originalImage = cv2.imread('clouds_comp.jpeg')
grayImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)
  
(thresh, blackAndWhiteImage) = cv2.threshold(grayImage, 127, 255, cv2.THRESH_BINARY)
 
#cv2.imshow('Black white image', blackAndWhiteImage)
#cv2.imshow('Original image',originalImage)
#cv2.imshow('Gray image', grayImage)
 
#cv2.waitKey(0)
#cv2.destroyAllWindows()
plt.imshow(grayImage, cmap='gray')
plt.show()
plt.axis('off')
