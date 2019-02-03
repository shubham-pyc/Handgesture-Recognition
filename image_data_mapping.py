import cv2 as cv
import numpy as np
import os

X = None
image_path = "gestures/otsu"
dir = os.listdir(image_path)
key_mapping = {
    "one":0,
    "two":1,
    "three":2,
    "four":3,
    "five":4,
    "okay":5,
    "cool":6
}
y = np.zeros([len(dir),len(key_mapping.keys())])


print(y.shape)


for i in xrange(len(dir)):

    array   = cv.imread(image_path+"/"+dir[i],cv.CV_LOAD_IMAGE_UNCHANGED)
    array = array.reshape(1,2500)



    if  type(X) == np.ndarray:
        X = np.vstack([X,array])
    else:
        X  = array

    #y[i][int(dir[i].split('_')[0])-1] = 1
    y[i][key_mapping[dir[i].split("_")[0]]] = 1

# np.save("X",X)
# np.save("y",y)
print(X.shape,y.shape)
# np.save("X_otsu",X)
# np.save("y_otsu",y)
np.save("X_otsu_50",X)
np.save("y_otsu_50",y)