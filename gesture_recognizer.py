from sklearn.neural_network import MLPClassifier
import numpy as np
import constants
import os
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle
class Recognizer:
    def __init__(self,debug=False):
        self.neural_network = None
        self.is_trained = False
        self.input_vector_path = "{}{}{}".format(constants.NUMPY_FOLDER_PATH,constants.DEFAULT_INPUT_VECTOR_NAME,".npy")
        self.output_vector_path = "{}{}{}".format(constants.NUMPY_FOLDER_PATH,constants.DEFAULT_OUTPUT_VECTOR_NAME,".npy")
        if not os.path.isfile(self.input_vector_path):
            raise OSError(constants.FILE_NOT_FOUND_ERROR_MESSAGE.format(self.input_vector_path))
        if not os.path.isfile(self.output_vector_path):
            raise OSError(constants.FILE_NOT_FOUND_ERROR_MESSAGE.format(self.output_vector_path))
        self.hidden_layers = [constants.DEFAULT_HIDDEN_LAYER]
        self.trained_modal = None
        self.debug = debug

    def toggle_debug(self):
        self.debug = not self.debug

    def train(self,force_train=False):
        if not self.is_trained or force_train:
            X = np.load(self.input_vector_path)
            y = np.load(self.output_vector_path)
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
            if self.debug:
                print(constants.DM_TRAIN_TEST_SPLIT_DONE)
            for layer in self.hidden_layers:
                modal = MLPClassifier(hidden_layer_sizes=layer, solver='adam',max_iter=500, alpha=0.003, verbose=self.debug,
                          random_state=42,tol=0.000000001)
                if self.debug:
                    print (constants.DM_LEARNING_STARTED.format(layer))
                self.trained_modal = modal.fit(X_train,y_train)
                y_pred = self.trained_modal.predict(X_test)
                score = accuracy_score(y_test,y_pred)
                print(constants.IM_DONE_TRAINING.format(score))
                self.is_trained = True

                choice = raw_input(constants.IM_SAVE_MODAL)
                print(choice)


                if(str(choice) == 'y'):
                    file_name = "Modal_{}-{:0.4f}".format("_".join(str(i) for i in layer),0.9998)
                    if(self.debug == True):
                        print(constants.DM_SAVE_MODAL.format(file_name))
                    pickle.dump(self.trained_modal,open(constants.NEURAL_NETWORKS_FOLDER_PATH+file_name,'wb'))

            return

        else:
            if self.debug:
                print(constants.DM_MODAL_ALREADY_TRAINED)
            return
    def recognize(self):
        pass

recognizer = Recognizer(debug=True)
recognizer.train()