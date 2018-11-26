from PIL import Image
from PIL import ImageDraw
image = Image.open("tigre.jpg")
drawobj = ImageDraw.Draw(image)
for position in range(10,100,5):
	drawobj.point(xy=(position,position),fill=(255,0,0))
image.show()