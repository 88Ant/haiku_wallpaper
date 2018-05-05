import os
import random
import sys
from PIL import Image, ImageFont, ImageDraw


#screen_resolution = str(os.system("xdpyinfo | grep dimensions"))

with open('haikus.txt') as f:
	lines = f.read().split('\n\n')	





rand = random.choice(lines)
#for x in lines:
#	print x,'\n'
#print str(lines).split('\n\n')
print rand















img = Image.new('RGB', (1400,900), (255, 255, 255))
txt = rand
draw = ImageDraw.Draw(img)
font = ImageFont.truetype("/home/saito/Templates/Haiku/haiku_wallpaper/Monaco.ttf", 25)
draw.text((100, 50), txt, (0,0,0), font=font)
img_resized = img.resize((188,45), Image.ANTIALIAS)
img.save("haiku_wallpaper.png", "PNG")	



