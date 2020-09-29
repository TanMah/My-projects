# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 15:54:56 2019

@author: Tanisha
"""
'''
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('flower_comp.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
kernel = np.ones((5,5),np.float32)/25
dst = cv2.filter2D(img,-1,kernel)
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dst),plt.title('Averaging')
plt.xticks([]), plt.yticks([])
'''
import cv2
import numpy as np
from matplotlib import pyplot as plt
    
img = cv2.imread('flower_comp.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
blur = cv2.blur(img,(5,5))
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()
