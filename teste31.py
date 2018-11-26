from PIL import Image
from PIL import ImageDraw
image = Image.open("tigre.jpg")
drawobj = ImageDraw.Draw(image)
drawobj.ellipse(xy=(0,0,200,200), outline=(0,0,255), fill=(255,0,0))

image.show()