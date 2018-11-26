from PIL import Image
from PIL import ImageDraw
image = Image.open("tigre.jpg")

drawObj = ImageDraw.Draw(image)
#ensuite,on utilise la fonction "line" pour dessiner une ligne 
drawObj.line(xy=(0,0,100,100), fill=(255,0,0), width=40)

#Pour finir,on montre l'image !
image.show()