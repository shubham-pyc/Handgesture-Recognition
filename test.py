import os
import cv2 as cv
def rename_images(path):
    dir = os.listdir(path)
    for image_path in dir:
        #image = cv.imread(image_path,cv.CV_LOAD_IMAGE_UNCHANGED)
        print(image_path)



video = cv.VideoCapture(0)
while True:
    ret,frame = video.read()
    cv.imshow('frame',frame)
    gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    gray = cv.flip(gray,1)
    ret2,thresh = cv.threshold(gray,220,255,cv.THRESH_BINARY_INV)
    cv.imshow('gray', gray)
    cv.imshow('thresh',thresh)
    gray = cv.medianBlur(gray,5)
    canny = cv.Canny(gray,150,150)
    gauss = cv.adaptiveThreshold(gray,500,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,115,1)
    _,otsu = cv.threshold(gray,220,255,cv.THRESH_BINARY_INV+cv.THRESH_OTSU)
    cv.imshow('gauss',gauss)
    cv.imshow('otsu',otsu)
    print(gray.shape)
    cv.imshow('edge',canny)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv.destroyAllWindows()
