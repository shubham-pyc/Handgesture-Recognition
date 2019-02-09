import os
import cv2 as cv
import numpy as np
import constants
import os
def input_output_vector_constructor(folder_path,save=False,file_name="X"):
    """
    Utility function to flatten the images into (1,N) vector for all images
    creates corrospoinding output vector for labels
    :param folder_path:  Path of the folder from which images has
    to be mapped
    :return: X input vector y output vector
    """
    X = None
    key_mapping = get_class_keys(folder_path)
    dir = os.listdir(folder_path)

    y = np.zeros([len(dir), len(key_mapping.keys())])
    for i in xrange(len(dir)):
        array = cv.imread(folder_path + "/" + dir[i], cv.CV_LOAD_IMAGE_UNCHANGED)
        array = array.reshape(1, array.shape[0] *array.shape[1])
        if type(X) == np.ndarray:
            X = np.vstack([X, array])
        else:
            X = array
        y[i][key_mapping[dir[i].split(constants.DEFAULT_DELIMITER)[0]]] = 1
    if save:
        if not os.path.exists(constants.NUMPY_FOLDER_PATH):
            os.makedirs(constants.NUMPY_FOLDER_PATH)
        np.save("{}{}".format(constants.NUMPY_FOLDER_PATH,file_name),X)
        np.save("{}{}".format(constants.NUMPY_FOLDER_PATH,"y"),y)
    return X,y

def get_class_keys(folder_path,inverse=False):
    '''
    utility function to create key_value pair according to unique classes in image folder
    '''

    dir = os.listdir(folder_path)
    classes = dict()
    key_counter = 0
    for _image in dir:
        key_name = _image.split(constants.DEFAULT_DELIMITER)[0]
        if key_name not in classes:
            classes[key_name] = key_counter
            key_counter+=1
    if inverse:
        return inverse_dict(classes)
    return classes

def inverse_dict(directory):
    """
    Inverses directory: keys becomes value and values becomes keys
    """
    return dict((v,k) for k,v in directory.iteritems())

