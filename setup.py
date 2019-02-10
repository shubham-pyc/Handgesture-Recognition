import importlib
import pip
import constants

def install_packages(package,lib_name):
    try:
        importlib.import_module(package)
        print(constants.DM_MODULE_ALREADY_INSTALLED.format(package))
    except:
        print(constants.DM_INSTALLING_MODULE.format(package))
        pip.main(['install',lib_name])

def main():
    required_modules = ['sklearn','numpy','cv2','scipy']
    lib_name = ['scikit-learn','numpy','opencv-python','scipy']

    for i in range(len(required_modules)):
        install_packages(required_modules[i],lib_name[i])



main()