
import pickle
import cv2 as cv
import numpy as np
video = cv.VideoCapture(0)
fileName = "model_ostu_50"
clf = pickle.load(open(fileName,'rb'))
message_keys = {
    0:"1 Fingure",
    1:"2 Fingures",
    2:"3 Fingure",
    3:"4 Fingures",
    4:"5 Fingures",
    5:"Okay",
    6:"Cool"
}


while True:
    ret,frame = video.read()
    cv.rectangle(frame,(300, 300), (100, 100), (255, 0, 0), 0)

    crop_image = frame[100:300,100:300]
    conver_gray = cv.cvtColor(crop_image ,cv.COLOR_BGR2GRAY)
    _, otsu = cv.threshold(conver_gray, 220, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)
    otsu = cv.resize(otsu,(50,50),interpolation=cv.INTER_AREA)
    cv.imshow('otsu', otsu)
    # otsu = otsu.reshape(1,40000)
    otsu = otsu.reshape(1, 2500)
    result = clf.predict(otsu)[0]

    maximum = max(result)
    index = [i for i,j in enumerate(result) if j==maximum]
    print(index[0])
    message = message_keys[index[0]]
    print(message)
    cv.putText(frame,message,(0,50),cv.FONT_HERSHEY_COMPLEX,2,(255,255,255),2)

    cv.imshow('frame', frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv.destroyAllWindows()