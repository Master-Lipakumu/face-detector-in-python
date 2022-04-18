import cv2
#import open cv / cv2


#recuperation du fichier frontalface
face = cv2.CascadeClassifier('frontalface.xml')

#lancement de la capture video depuis la webcam
cap = cv2.VideoCapture(0)

#lancement de la capture video depuis le fichider mp4
#cap = cv2.VideoCapture('file.mp4')


#lancement de la boucle infini 
while True:
#lire le cadre 
    _, img = cap.read()
#convertir en grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#detecter le visage
    faces = face.detectMultiScale(gray, 1.1, 4)
# tracer un rectangle autour de chaque face
    for (x,y,w,h) in faces:

        cv2.rectangle(img, (x,y), (x + w , y + h ), (255,0,0), 2)
#affichage
    cv2.imshow('img', img)
#stoper si la touche d'échappement est enfoncée
    k=cv2.waitKey(30) & 0xff

    if k == 27:

        break
#libere la videocapture
cap.release()