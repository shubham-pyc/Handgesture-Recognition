import os
import cv2 as cv
def rename_images(path):
    dir = os.listdir(path)
    print(dir)
    for image_path in dir:
        image = cv.imread("{}/{}".format(path,image_path),cv.CV_LOAD_IMAGE_UNCHANGED)
        os.remove("{}/{}".format(path,image_path))

        name = image_path.split("_")
        name = "{}_{}-{}".format(name[0],name[1],name[2])
        cv.imwrite("{}/{}".format(path,name),image)

def convert_gray_to_otsu(path,next_path):
    dir = os.listdir(path)
    print(dir)
    for image_path in dir:
        image = cv.imread("{}/{}".format(path, image_path), cv.CV_LOAD_IMAGE_UNCHANGED)
        _, otsu = cv.threshold(image, 220, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)

        otsu = cv.resize(otsu, (50, 50), interpolation=cv.INTER_AREA)
        cv.imwrite("{}/{}".format(next_path,image_path), otsu)


#convert_gray_otsu("gestures/gray","gestures/otsu")
