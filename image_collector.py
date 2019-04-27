import cv2 as cv
import constants
import os
from printer import Printer

class ImageCollector:
    def __init__(self):
        self.classes = []                                               # Gesture names
        self.sample_size = []                                           # Number of images to capture
        self.debug = False                                              # Debug flag
        self.collected = False
        self.DEFAULT_SAMPLE_SIZE = constants.DEFAULT_SAMPLE_SIZE
        self.video = cv.VideoCapture(0)                                 # webcam object
        self.pixels = 200
        self.save_rgb = True                                            # Flag for saving RGB colored image
        self.save_gray = True                                           # Flag to save in gray scaled image
        self.save_otsu = True
        self.printer = Printer()                                        # Custom printer object

        self.folder_list = [constants.DEFAULT_FOLDER_PATH,
                            constants.DEFAULT_COLOUR_IMAGE_FOLDER_PATH,
                            constants.DEFAULT_OTSU_IMAGE_FOLDER_PATH,
                            constants.DEFAULT_GRAY_IMAGE_FOLDER_PATH,
                            constants.MODALS_PATH,
                            constants.NEURAL_NETWORKS_FOLDER_PATH,
                            constants.NUMPY_FOLDER_PATH]                    # List of directory folders 

        '''
        Create Defined Folders if Not already present 
        '''
        for _path in self.folder_list:
            if not os.path.exists(_path):
                os.mkdir(_path)




    def setDebugTrue(self):
        self.debug = True

    def add_classes(self,arg):
        ''' use this method to add new Class or Lable for a gesture
            arg can be of type Set or String '''
        if isinstance(arg,list):
            for index,value in enumerate(arg):
                    self.__insert_class(value)
        elif isinstance(arg,str):
            self.__insert_class(arg)
        else:
            raise ValueError(constants.ARGUMENTS_TYPE_LIST_OR_STRING_ERROR_MESSAGE)

    def __insert_class(self,class_name):
        '''
            Method to add a new label to the image collecting data or name gesture name
            :Param class_name: name of the new gesture
        '''
        if not isinstance(class_name,str):
            print(type(class_name))
            raise ValueError(constants.ARGUMENTS_TYPE_STRING_ERROR_MESSAGE)

        if class_name not in self.classes:
            self.classes.append(class_name)
            self.sample_size.append(self.DEFAULT_SAMPLE_SIZE)
        else:
            if self.debug:
                print(constants.LABEL_ALREADY_PRESENT_ERROR_MESSAGE.format(class_name))
            else:
                raise ValueError(constants.LABEL_ALREADY_PRESENT_ERROR_MESSAGE.format(class_name))

    def get_classes(self):
         if self.debug:
             print self.classes,'\n',self.sample_size
         return self.classes,self.sample_size

    def __save_image(self,image,folder,class_name,counter):
        '''
            Method to save image to the file directory
            :Param image: numpy array of image
            :Param folder: directory path
            :Param class_name: name of the file
            :Param counter: Number to append with the image name
        '''
        file_name = "{}{}-{}.png".format(folder
                                      ,class_name
                                      ,counter)
        print(file_name)
        if self.debug:
            pass
        cv.imwrite(file_name,image)


    def close_windows(self):
        '''
        Method To close all the open frame windows
        '''
        cv.destroyWindow('RGB')
        cv.destroyWindow('OTSU')
        cv.destroyWindow('GRAY')

    def start(self):
        '''
        Method to start the image collection
        '''
        if len(self.classes) == 0:
            raise ValueError(constants.NO_LABEL_PRESENT_ERROR_MESSAGE)
        # Custom printer class is used so logging can be done on different thread
        self.printer.start()                      

        total_gestures = len(self.classes)          # Calculating total number of gestures
        current_gesture = 0
        counter = 0
        capture_flag = False
        if self.debug:
            print(constants.DM_DATA_CAPTURING_INITIATED)
        while True:
            ret, frame = self.video.read()                                  # Start webcame
            cv.rectangle(frame, (300, 300), (100, 100), (255, 0, 0), 0)     # Create Rectable for ROI
            cv.imshow('frame', frame)                                       # Show image on screen
            crop_image = frame[100:300, 100:300]                            # Crop ROI
            gray_image = cv.cvtColor(crop_image, cv.COLOR_BGR2GRAY)         # Convert the image to gray scale
            if current_gesture < total_gestures:
                if(counter < self.DEFAULT_SAMPLE_SIZE):
                    if capture_flag:
                        if self.debug:
                            file_name = self.classes[current_gesture]+"_"+str(counter)          # Save the image
                            self.printer.message = constants.DM_IMAGE_SAVE.format(file_name)    # Log the image name


                        if self.save_rgb:
                            cv.imshow('RGB',crop_image)                                         # Save image in RGB color
                            self.__save_image(crop_image,
                                              constants.DEFAULT_COLOUR_IMAGE_FOLDER_PATH,
                                              self.classes[current_gesture],
                                              counter)
                        if self.save_gray: 
                            cv.imshow('GRAY', gray_image)                                       # Save image in gray scale
                            self.__save_image(gray_image,   
                                              constants.DEFAULT_GRAY_IMAGE_FOLDER_PATH,
                                              self.classes[current_gesture],
                                              counter)
                        if self.save_otsu:

                            _, otsu = cv.threshold(gray_image, 220, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)
                            cv.imshow('OTSU', otsu)                                             # Save image with OTSU thresholding
                            otsu = cv.resize(otsu,(50,50),interpolation=cv.INTER_AREA)
                            self.__save_image(otsu,
                                              constants.DEFAULT_OTSU_IMAGE_FOLDER_PATH,
                                              self.classes[current_gesture],
                                              counter)
                        counter +=1
                    else:
                        self.close_windows()

                else:
                    current_gesture += 1
                    if current_gesture < total_gestures:
                        self.printer.message ="\n"+constants.IM_SHOW_GESTURE_FOR_CLASS.format(self.classes[current_gesture])+"\n"
                        counter = 0
                        capture_flag = False
                    else:
                        self.close_windows()
                        self.printer.message = "\nEND press q to quit"
            if cv.waitKey(1) & 0xFF == ord('q'):                                # Break if Q is Pressed
                self.printer.stop()
                break
            if cv.waitKey(1) & 0xFF == ord('c'):                                # Start capturing if C is pressed
                if capture_flag == False :
                    print('C pressed')
                capture_flag = True


def main():
    collector = ImageCollector()
    collector.setDebugTrue()
    collector.add_classes(['one_fingure','two_fingure','three_fingure','four_fingure','five_fingure'])
    collector.add_classes(['okay_gesture', 'cool_gesture'])
    #collector.start()

main()
