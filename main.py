from ultralytics import YOLO
import cv2
import cvzone
import math


#cap=cv2.VideoCapture(0) #Use 0 for webcam or replace with video path
cap=cv2.VideoCapture('../Videos/ppe2.mp4')
model=YOLO('ppe.pt')
classNames=['Hardhat', 'Mask', 'NO-Hardhat', 'NO-Mask', 'NO-Safety Vest', 'Person', 'Safety Cone',
              'Safety Vest', 'machinery', 'vehicle']

myColor=(0,255,0)
while True:
    success,img=cap.read()
    results=model(img,stream=True)

    for r in results:
        boxes=r.boxes
        for box in boxes:
            x1,y1,x2,y2=box.xyxy[0]
            w,h=int(x2-x1),int(y2-y1)
            x1,y1=int(x1),int(y1)

            conf=math.ceil((box.conf[0]*100))/100
            cls=int(box.cls[0])

            if conf>0.5:
                if classNames[cls] =='NO-Hardhat' or classNames[cls] =='NO-Safety Vest' or classNames[cls] == "NO-Mask":
                    myColor = (0, 0,255)
                elif classNames[cls] =='Hardhat' or classNames[cls] =='Safety Vest' or classNames[cls] == "Mask":
                    myColor =(0,255,0)
                else:
                    myColor = (255, 0, 0)

            #cv2.putText(img,f'{className} {conf}',(max(0,x1),max(0,y1-10)),cv2.FONT_HERSHEY_SIMPLEX,0.6,(255,255,255),2)
            cvzone.cornerRect(img,(x1,y1,w,h),t=3,rt=2,l=15,colorR=myColor,colorC=myColor) #Bounding box
            cvzone.putTextRect(img,f'{classNames[cls]} {conf}',(max(0,x1),max(35,y1-10)),scale=1.4,thickness=1,offset=3,colorB=myColor,colorT=(255,255,255))

    cv2.imshow("Image",img)
    cv2.waitKey(1)
