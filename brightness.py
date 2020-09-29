# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 17:05:26 2019

@author: Meena
"""

from PIL import Image

from PIL import ImageEnhance


def adjust_brightness(input_image, output_image, factor):

    image = Image.open(input_image)

    enhancer_object = ImageEnhance.Brightness(image)

    out = enhancer_object.enhance(factor)

    out.save(output_image)

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

if __name__ == '__main__':

    adjust_contrast('bee_brightness.jpg',

                    'bee_br_cont.jpg',

                    1.05)


def adjust_sharpness(input_image, output_image, factor):

    image = Image.open(input_image)

    enhancer_object = ImageEnhance.Sharpness(image)

    out = enhancer_object.enhance(factor)

    out.save(output_image)

if __name__ == '__main__':

    adjust_sharpness('bee_br_cont.jpg',

                     'bee_br_cont_sharp.jpg',

                     1.75)

'''