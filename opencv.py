import cv2

# import the data from the openCv2 path
face_cap=cv2.CascadeClassifier("C:/Users/anjali kashyap/AppData/Roaming/Python/Python312/site-packages/cv2/data/haarcascade_frontalface_default.xml")

# capture the video
video_cap=cv2.VideoCapture(0)

# loop is continue
while True :
    # read and return the video data
    ret,video_data = video_cap.read()

    # detect the color
    col=cv2.cvtColor(video_data,cv2.COLOR_BGR2GRAY)

    # face object define
    faces=face_cap.detectMultiScale(
        col,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(5,5),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    # dimension
    for(x,y,w,h) in faces:
        cv2.rectangle(video_data,(x,y),(x+w,y+w),(0,255,0),2)
    cv2.imshow("video_live",video_data)
    if cv2.waitKey(10) == ord("a"):
        break 
video_cap.release()

# video_cap=cv2.VideoCapture(0)
# while True :

#     ret,video_data = video_cap.read()
#     cv2.imshow("video_live",video_data)
#     if cv2.waitKey(10) == ord("a"):
#         break 
# video_cap.release()


