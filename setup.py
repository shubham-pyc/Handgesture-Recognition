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
    required_modules = {'sklearn':'scikit-learn','numpy':'numpy','cv2':'opencv-python','scipy':'scipy'}

    for package,lib_name in required_modules.items():
        install_packages(required_modules,lib_name)

main()
