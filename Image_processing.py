#!/usr/bin/python

import commands
from PIL import Image

fileImg = Image.open('test.png')

# Converting the image to greyscale.
converted = fileImg.convert('L')

# Saving the image as tesseract can read.
converted.save('tmp.bmp')

# Invoking tesseract from python to extract characters
commands.getoutput('tesseract tmp.bmp TF')

# Reading the output generated in TF.txt
with open('TF.txt', 'r') as TF:
    print TF.readline().strip()
#Write the info in a file
