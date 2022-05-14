from platform import release
import cv2


#importing some preexsiting algorithm 
trained_face_data=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


class Video(object):
    def __init__(self):
        self.video=cv2.VideoCapture(0)
    def __del__(self):
        self.video.release()
    def get_frame(self):
        ret,frame=self.video.read()

        grayscaled_img= cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)


        #Detect faces
        face_coordinates=trained_face_data.detectMultiScale(grayscaled_img)


        #Draw rectange around the faces
        for (x,y,w,h) in face_coordinates:
         cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)
        ret,jpg=cv2.imencode('.jpg',frame)
        return jpg.tobytes()