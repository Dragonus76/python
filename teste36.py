from PIL import ImageFilter
from PIL import Image
import cv2


############################
# UTILISATION DE LA WEBCAM #
############################

cam = cv2.VideoCapture(0) 
ret, image = cam.read() # prend une photo


##########################
# MANIPULATION DE L'IMAGE #
###########################

image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # convertit la photo dans un format OK pour PIL

image = Image.fromarray(image) # charge l'image convertie dans PIL avec la methode "fromarray"

image = image.filter(ImageFilter.EDGE_ENHANCE)
image = image.filter(ImageFilter.ModeFilter(15))


######################################
# SAUVEGARDE DE L'IMAGE ET AFFICHAGE #
######################################

image.show()
image.save("customSelfie.png")