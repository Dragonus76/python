
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("computer.png")
tigre = parser.parse_args()
tigre.jpg = tigre.jpg


### on ouvre l'image
img = Image.open("computer.png").conert('RGBA')

### Fonction qui ajoute le texte
def Textes(img, texte, position,r,g,b):
	#on cree une nouvelle image vide de la meme taille que la premiere
	txt = Image.new ('RGBA', img.size,(255,255,255,0))
	# On choisit une police et sa taille 
	fnt = ImageFont.truetype('Jestho Fisher - Personal Use.otf',69)
	#pouvoir ecrire sur l'image "txt"
	d = ImageDraw.Draw(txt)
	# On defenit l'emplacement du texte , le texte, la police du texte et la couleur du texte
	d = texte(position,texte,font=fnt, fill=(r,g,b,128))
	image_finale = Image.alpha_composite(img,txt)
	return image_finale
	### On recupere les variables texte , position et RGB pour la couleur du texte + on les passe en in 
texte_choisi = input(" Quel texte ? ")

w=int(input("position -> x ? "))
h=int(input("position -> y ? "))
position = (w,h)
val_rouge = int(input("Valeur de rouge ?" ))
val_vert = int(input("Valeur de vert ?" ))
val_bleu = int(input("Valeur de bleu ?" ))
### On lance la fonction et on afffiche l'image qu"elle renvoie
img = Textes(img,texte_choisi,position,val_rouge,val_bleu,val_vert)
img.show()
### on sauvegarde 
sauvegarde = input("sauvegarde ? Oui ou Non. ")
if sauvegarde == "Oui":
	img.save("computer.png")