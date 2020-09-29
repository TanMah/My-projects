# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 08:24:26 2019

@author: Meena
"""
import numpy as np
import cv2
from matplotlib import pyplot as plt

#IT WORKS!!!!

#img = cv2.imread('guy_comp.jpeg')
#img = cv2.imread('blonde_comp.jpg')
#img = cv2.imread('portrait_1.jpg')
#img = cv2.imread('lamp.jpg')
#img = cv2.imread('yoga.jpeg')
#img = cv2.imread('housemd.jpg')
img = cv2.imread()

img=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
mask = np.zeros(img.shape[:2],np.uint8)

bgdModel = np.zeros((1,65),np.float64)
fgdModel = np.zeros((1,65),np.float64)

#for guy_comp
#rect = (109,113,623,903)

#for guy comp(only head)
#rect = (291,393,315,233)

#for blonde
#rect = (945,25,2329,2449)

#for portrait 1
#rect=(69,45,323,288)

#for lamp
#rect=(195,7,244,418)

#for lamp
#rect=(118,305,95,97)

#for yoga
#rect=(55,99,128,180)

#for house MD
#rect=(161,11,419,599)


cv2.grabCut(img,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)
mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
img = img*mask2[:,:,np.newaxis]

plt.imshow(img)
#plt.colorbar()
plt.show()
plt.axis('off')

