import cv2
from mtcnn import MTCNN
from mtcnn.utils.images import load_image

#Creating a Video Capture feed
cap = cv2.VideoCapture(0)
#Creating a MTCNN detector object
detector = MTCNN(device="CPU:0")

while True:
    ret, frame = cap.read()
    if ret == True:
        a=frame.copy()
        location=detector.detect_faces(frame)
        if len(location)>0:
            for face in location:
                score = face["confidence"]
                if score >= 0.90:
                    x1,y1,width,height=face['box']
                    x2=x1+width
                    y2=y1+width
                    cv2.rectangle(a, (int(x1), int(y1)), (int(x2), int(y2)), (0, 0, 255), 2)
        cv2.imshow("capture",a)
        key=cv2.waitKey(1)
        
        if key==ord('s'):
            cv2.imwrite("captured_image.jpg",frame[int(y1):int(y1+height), int(x1):int(x1+width)]) #The cropped output image
            break
        
        if key==ord('q'):
            break 
    else:
        break
cap.release()
cv2.destroyAllWindows()

