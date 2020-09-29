# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 21:05:55 2019

@author: Meena
"""

from PIL import Image, ImageOps

def add_border(input_image, output_image, border, color=0):

    img = Image.open(input_image)

    if isinstance(border, int) or isinstance(border, tuple):

        bimg = ImageOps.expand(img, border=border, fill=color)

    else:

        raise RuntimeError('Border is not an integer or tuple!')

    bimg.save(output_image)

if __name__ == '__main__':

    in_img = 'bee.jpg'

    add_border(in_img,

               output_image='bee_b2.jpg',

               border=20,
#start with left and move clockwise
               color='yellow')
#border=int specifies thickness in pixels
