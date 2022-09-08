import cv2
def det_hum(image_path):
    # define hog algorithm
    hog=cv2.HOGDescriptor()
    # use petrained model to detect humen
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
    image=cv2.imread(image_path)
    # detect bound of rectangle
    bound,wights=hog.detectMultiScale(image,winStride=(4,4), padding=(4,4), scale=1.05)
    for (x,y,w,h) in bound:
        cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,255),4)
    # get path size
    size=len(image_path)
    # modify image path
    new_path=image_path[:size-4]
    new_path=new_path+'_detct.jpg'
    # save detect image in new path
    cv2.imwrite(new_path,image)
    return new_path