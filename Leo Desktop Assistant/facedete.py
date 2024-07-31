import cv2

face_cap=cv2.CascadeClassifier("C:\Users\Dnyaneshwar\AppData\Local\Programs\Python\Python311\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml")
video_cap=cv2.VideoCapture(0)
while True:
    ret,frame=video_cap.read()
    col=cv2.cvtColor(video_cap,cv2.COLOR_BAYER_BGGR2GRAY)
    faces=face_cap.detectMultiScale(
        col,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30,30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    for(x,y,w,h) in faces:
        cv2.rectangle(video_cap(x,y),(x+w,y+h),(0,255,0),2)
    cv2.imshow("Video Live",frame)
    if cv2.waitKey(10)== ord("a"):
        break
video_cap.release()
    
