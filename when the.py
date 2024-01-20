
# Modification date: Sat Feb 19 20:38:16 2022

# Production date: Sun Sep  3 15:44:14 2023

from PIL import Image
import os
from clear_screen import clear
from time import sleep
from random import sample

print(os.getcwd())


path = os.getcwd()

img = Image.open(path + "\\sky.jpg")

width, height = img.size

#print(img.size)
#img = img.resize((height//2, width//2))
width, height = img.size
print(img.size)
#img.rotate(90)



for x in range(width):
    for y in range(height):
        rgb = img.getpixel((x, y))
        r, g, b = rgb[0], rgb[1], rgb[2]
        rgbt = rgb[0] + rgb[1] + rgb[2]
        diff = 100 - rgbt
        rgb2 = []
        add = diff // 3
        
        for i in range(3):
            try:
                rgb2.append(rgb[i] + add)
            except:
                if diff > 0:
                    rgb2.append(255)
                else:
                    rgb2.append(0)
        rgb2 = tuple(rgb2)
        img.putpixel((x, y), rgb2)
        
            
img.save("sky006.jpg")
            








