
"""
Created on Thu Jun 27 20:00:32 2019

@author: Meena
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt


#reading an image
img = cv2.imread('bee.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#cv2.imshow('image',img)
#plt.imshow(img)
#plt.show()
plt.axis("off")
#cv2.waitKey(0)
#cv2.destroyAllWindows()


from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib import colors


#RGB coloured scatter plot

r, g, b = cv2.split(img)
fig = plt.figure()
axis = fig.add_subplot(1, 1, 1, projection="3d")
pixel_colors = img.reshape((np.shape(img)[0]*np.shape(img)[1], 3))
norm = colors.Normalize(vmin=-1.,vmax=1.)
norm.autoscale(pixel_colors)
pixel_colors = norm(pixel_colors).tolist()
axis.scatter(r.flatten(), g.flatten(), b.flatten(), facecolors=pixel_colors, marker=".")
axis.set_xlabel("Red")
axis.set_ylabel("Green")
axis.set_zlabel("Blue")
plt.show()

'''
#HSV 3D scatter plot
hsv_img = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
h, s, v = cv2.split(hsv_img)
fig = plt.figure()
axis = fig.add_subplot(1, 1, 1, projection="3d")

axis.scatter(h.flatten(), s.flatten(), v.flatten(), facecolors=pixel_colors, marker=".")
axis.set_xlabel("Hue")
axis.set_ylabel("Saturation")
axis.set_zlabel("Value")
plt.show()



#rgb histogram
img = cv2.imread('girl_comp.jpeg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
color = ('b','g','r')
for i,col in enumerate(color):
    histr = cv2.calcHist([img],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])
    plt.show()
   
'''