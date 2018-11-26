from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
image = Image.open("tigre.jpg")
# On ouvre l'image
# On charge la police de caractère présente dans le méme dossier , avec les taille qu'on veut 

police = ImageFont.truetype('Jestho Fisher - Personal Use.otf',69)
#Ici on crée l'objet nous permettant d'ecrire le texte sur l'image
drawObj = ImageDraw.Draw(image)
#On defénit l'emplacement du texte sur l'image,le texte, la police et la couleur !
drawObj.text((0,0),"coucou !",font=police, fill=(255,0,0))
image.show()