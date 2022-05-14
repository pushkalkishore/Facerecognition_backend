import cv2

#importing some preexsiting algorithm 
trained_face_data=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#Chose image to detect
#img=cv2.imread('rdj.jpeg')

webcam=cv2.VideoCapture(0)


while True:

    #frame read
    successful_frame_read, frame=webcam.read()


    #Converting image to grayscale
    grayscaled_img= cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)


    #Detect faces
    face_coordinates=trained_face_data.detectMultiScale(grayscaled_img)


    #Draw rectange around the faces
    for (x,y,w,h) in face_coordinates:
      cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)

    cv2.imshow('RDJ',frame)
    cv2.waitKey(1)



















""""
#Converting image to grayscale
grayscaled_img= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


#Detect faces
face_coordinates=trained_face_data.detectMultiScale(grayscaled_img)


#Draw rectange around the faces
for (x,y,w,h) in face_coordinates:
 cv2.rectangle(img, (x, y), (x+w, y+h), (0,255,0), 2)


# print(face_coordinates)


cv2.imshow('RDJ',img)
cv2.waitKey()

print ("Code completed")
"""