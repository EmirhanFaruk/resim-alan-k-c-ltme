
# Modification date: Wed Feb  2 21:03:02 2022

# Production date: Sun Sep  3 15:44:14 2023

from PIL import Image
import os
from clear_screen import clear
from time import sleep

print(os.getcwd())


path = os.getcwd()

img = Image.open(path + "/p2.jpg")

width, height = img.size

#print(img.size)
#img = img.resize((height//2, width//2))
width, height = img.size
print(img.size)
img.rotate(90)


for y in range(height):
	clear()
	print(f"%{int(y/ height * 100) + 1}")
	print(f"{y} / {height}")
	streak = []
	sc = -1
	onst = False
	x = 0
	while x < width - 1:
		rgb = img.getpixel((x, y))
		rgb2 = img.getpixel((x + 1, y))
		cases = [abs(rgb[0] - rgb2[0]) < 3, abs(rgb[1] - rgb2[1]) < 3, abs(rgb[2] - rgb2[2]) < 3]
		passing = False
		for bruh in range(len(cases)):
			if cases[bruh]:
				passing = True
			else:
				onst = False
		if passing:
			if not onst:
				sc += 1
				streak.append([])
			onst = True
			if not ((x, y), rgb) in streak[sc]:
				streak[sc].append(((x, y), rgb))
			if not ((x + 1, y), rgb2) in streak[sc]:
				streak[sc].append(((x + 1, y), rgb2))
		x += 1
	if len(streak) > 0:
		#print(f"{len(streak)} > 0")
		for i in range(len(streak)):
			ct = len(streak[i])
			counter = 0
			r = 0
			g = 0
			b = 0
			while counter < ct:
				r += streak[i][counter][1][0]
				g += streak[i][counter][1][1]
				b += streak[i][counter][1][2]
				counter += 1
			mr = r // len(streak[i])
			mg = g // len(streak[i])
			mb = b // len(streak[i])
			for j in range(len(streak[i])):
				img.putpixel(streak[i][j][0], (mr, mg, mb))
	#print(len(streak))
	#print(len(streak[0]))
	#sleep(5)

		

img.save("p2t001.jpg")