#ERROR MESSAGES
ARGUMENTS_TYPE_LIST_OR_STRING_ERROR_MESSAGE= "Arguments should be of type List or String"
ARGUMENTS_TYPE_STRING_ERROR_MESSAGE = "Arguments should be of type String"
LABEL_ALREADY_PRESENT_ERROR_MESSAGE = "Class/Label: {} already present."
NO_LABEL_PRESENT_ERROR_MESSAGE = "Please add Class/Labels to the object first using add_classes method"
FILE_NOT_FOUND_ERROR_MESSAGE = "No such file names {} found\n Please call transformer.input_output_vector_constructor with save=True parameter"

# FOLDERS PATHS
MODALS_PATH = "modals/"
NUMPY_FOLDER_PATH = "{}numpy/".format(MODALS_PATH)
NEURAL_NETWORKS_FOLDER_PATH = "{}neural_network/".format(MODALS_PATH)
DEFAULT_FOLDER_PATH = "gestures/"
DEFAULT_COLOUR_IMAGE_FOLDER_PATH = "{}rgb/".format(DEFAULT_FOLDER_PATH)
DEFAULT_GRAY_IMAGE_FOLDER_PATH = "{}gray/".format(DEFAULT_FOLDER_PATH)
DEFAULT_OTSU_IMAGE_FOLDER_PATH = "{}otsu/".format(DEFAULT_FOLDER_PATH)

#INSTRUCTION_MESSAGES (IM)
IM_SHOW_GESTURE_FOR_CLASS = "show gesture for {} class and press c to start capturing"
IM_PRESS_C = "press c to start capturing"
IM_DONE_TRAINING = "Finished Traning!\n Accurecy score: {}"
IM_SAVE_MODAL = "Happy with the result?\nSave modal? (y/n): "

#DEBUG MESSAGES(DM)
DM_IMAGE_SAVE = "Saving file: {}"
DM_DATA_CAPTURING_INITIATED = "Started capturing data"
DM_MODAL_ALREADY_TRAINED = "The Modal is already trained.\nRecall this method with 'force_train=True' parameter to retrain"
DM_TRAIN_TEST_SPLIT_DONE = "Train test split done."
DM_LEARNING_STARTED = "Learning Started with hidden layer: {}"
DM_SAVE_MODAL = "Saving modal: {}"


#MISCELANIOUS
DEFAULT_SAMPLE_SIZE = 500
DEFAULT_DELIMITER ="-"
DEFAULT_HIDDEN_LAYER = (500,200)
DEFAULT_INPUT_VECTOR_NAME = "X"
DEFAULT_OUTPUT_VECTOR_NAME = "y"
