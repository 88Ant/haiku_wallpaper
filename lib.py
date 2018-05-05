#importing modules that are necessary
import os, random
from PIL import Image, ImageFont, ImageDraw

#getting screen resolution from os command
screen_resolution = str(os.system("xdpyinfo | grep dimensions"))

#taking little poems to array
with open('haikus.txt') as f:
	lines = f.read().split('\n\n')	

#randomly choosing poem
rand = random.choice(lines)


#drawing an image
img = Image.new('RGB', (1400,900), ('white'))
draw = ImageDraw.Draw(img)
#w,h = draw.textsize(rand)
font = ImageFont.truetype("/home/saito/Templates/Haiku/haiku_wallpaper/Monaco.ttf", 23)
draw.text(((1400)/2.8, (900)/2), rand, (0,0,0), font=font)
img.save("haiku_wallpaper.png", "PNG")	



