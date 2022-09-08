import cv2
from matplotlib import image
import numpy as np
def det_hum(image_path):
    hog=cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
    image=cv2.imread(image_path)
    bound,wights=hog.detectMultiScale(image,winStride=(4,4), padding=(4,4), scale=1.05)
    for (x,y,w,h) in bound:
        cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,255),4)
    size=len(image_path)
    new_path=image_path[:size-4]
    new_path=new_path+'_detct.jpg'
    cv2.imwrite(new_path,image)
    return new_path