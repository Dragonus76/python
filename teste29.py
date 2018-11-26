from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
image = Image.open("tigre.jpg")


police = ImageFont.truetype('Jestho Fisher - Personal Use.otf',69)

drawObj = ImageDraw.Draw(image)

drawObj.text((0,0),"coucou !",font=police, fill=(255,0,0))
image.show()