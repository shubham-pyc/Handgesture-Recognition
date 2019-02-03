import cv2 as cv
from time import sleep
import numpy as np

video = cv.VideoCapture(0)
flag = False
number_of_fingers = 0
i = 500
folder_path = "images_edge/"

while True:
    ret,frame = video.read()
    cv.rectangle(frame,(300, 300), (100, 100), (255, 0, 0), 0)
    cv.imshow('frame',frame)
    crop_image = frame[100:300,100:300]
    conver_gray = cv.cvtColor(crop_image,cv.COLOR_BGR2GRAY)

    canny = cv.Canny(conver_gray,90,90)
    cv.imshow('crop image', canny)
    if(number_of_fingers<6):
        if(i<50):
            if flag:
                cv.imwrite(folder_path + str(number_of_fingers) + "_finger+" + str(i) + ".png", canny)
                print('took image')
                i += 1
                flag = False
        else:
            print("please show {} fingers".format(number_of_fingers))
            number_of_fingers += 1
            i = 1
    else:
        break
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
    if cv.waitKey(1) & 0xFF == ord('c'):
        flag = True


video.release()
cv.destroyAllWindows()