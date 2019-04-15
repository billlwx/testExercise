#! /usr/bin/env python
# _*_ coding: utf-8 _*_
# __author__ = 'bill'
# create on 2019/4/15

import pytesseract
from PIL import Image

# open image
image = Image.open('1555300573216.jpg')
code = pytesseract.image_to_string(image, lang='chi_sim')
print(code)