import cv2

cam = cv2.VideoCapture(0)# accede a la webcam
ret, image = cam.read() # prend une photo
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) #convertit l'image pour le format PILL
image = Image.fromarray(image) # charge l'image convertie dans PIL avec la methode "fromarray"
