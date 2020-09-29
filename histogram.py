# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 06:20:00 2019

@author: Meena
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

#histogram
img = cv2.imread('girl_comp.jpeg')
color = ('b','g','r')
for i,col in enumerate(color):
    histr = cv2.calcHist([img],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])
    plt.show()
    
