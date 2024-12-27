import cv2
from mtcnn import MTCNN
from mtcnn.utils.images import load_image
class FaceCap:
    

    def __init__(self):
        #Creating a Video Capture fe
        self.cap = cv2.VideoCapture(0)
        #Creating a MTCNN detector object
        self.detector = MTCNN(device="CPU:0")
        self.count=0
        while True:
            self.ret, self.frame = self.cap.read()
            if self.ret == True:
                self.a=self.frame.copy()
                self.location=self.detector.detect_faces(self.frame)
                if len(self.location)>0:
                    for self.face in self.location:
                        self.score = self.face["confidence"]
                        if self.score >= 0.90:
                            self.x1,self.y1,self.width,self.height=self.face['box']
                            self.x2=self.x1+self.width
                            self.y2=self.y1+self.width
                            cv2.rectangle(self.a, (int(self.x1), int(self.y1)), (int(self.x2), int(self.y2)), (0, 0, 255), 2)
                            #cv2.imwrite("captured_image.jpg",self.frame[int(self.y1):int(self.y1+self.height), int(self.x1):int(self.x1+self.width)]) #The cropped output image
                cv2.imshow("capture",self.a)
                if self.count>=1:
                    break
                self.key=cv2.waitKey(1)
        
                if self.key==ord('s'):
                    cv2.imwrite("captured_image.jpg",self.frame[int(self.y1):int(self.y1+self.height), int(self.x1):int(self.x1+self.width)]) #The cropped output image
                    break
        
                if self.key==ord('q'):
                    break 
            else:
                break
        self.cap.release()
        cv2.destroyAllWindows()
