# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 15:12:48 2019

@author: Meena
"""

from PIL import Image

from PIL import ImageEnhance

print("1.brightness\t2.contrast\t3.sharpness")
i=input("\n enter your choice: ")
input_image=input("\n enter input image: ")
output_image=input("\n enter output image: ")
factor=float(input("\n enetr factor value: "))



def adjust_brightness(input_image, output_image, factor):

    image = Image.open(input_image)

    enhancer_object = ImageEnhance.Brightness(image)

    out = enhancer_object.enhance(factor)

    out.save(output_image)
    '''

if __name__ == '__main__':

    adjust_brightness('bee.jpg',

                      'bee_brightness.jpg',

                      2.0)

'''
def adjust_contrast(input_image, output_image, factor):

    image = Image.open(input_image)

    enhancer_object = ImageEnhance.Contrast(image)

    out = enhancer_object.enhance(factor)

    out.save(output_image)
    '''

if __name__ == '__main__':

    adjust_contrast('bee_brightness.jpg',

                    'bee_br_cont.jpg',

                    1.05)
'''

def adjust_sharpness(input_image, output_image, factor):

    image = Image.open(input_image)

    enhancer_object = ImageEnhance.Sharpness(image)

    

if i==1:
    adjust_brightness(input_image, output_image, factor)
    
if i==2:
    adjust_contrast(input_image, output_image, factor)
    

if i==3:
    adjust_sharpness(input_image, output_image, factor)