# HandGesture Recognition With Neural Networks

A Framework for training Neural Network with custom hand gestures.
Advantages - 
1) Trainability - NN can be trained with this framework in 10 lines of code
2) Scalability - New gestures can be added under 5 lines of code
3) Configurability
4) Reusability

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development.

### Prerequisites

Clone the project
```
git clone 'https://github.com/shubhamg2404/Handgesture-Recognition.git'
```

### Installing
A step by step series of examples that tell you how to get a development env running

Inside the project folder run the following command to install the prerequisit packages
```sh
python setup.py
```
## Architecture Diagram
![diagram](https://github.com/shubhamg2404/Handgesture-Recognition/blob/master/docs/diagrams/Architecture_1.0.jpg)

## How to use
### 1) Data collection:
The framework comes prebuild with a library to collect hand gestures for training
```python
from image_collector import ImageCollector
collector = ImageCollector()
collector.setDebugTrue()
collector.add_classes(['class_one','class_two'])
collector.start()
```
Above code snipit will ignite your webcam and ask you to place your hand in from of it to grab 500 images for each gesture. The library will remove all the noise from the image and resize it to 50x50 pixels

### 2) Transformation: 
After the data has been collected (images) it is time to tranform the images so that it can be used as an input for Neural Networks
```python
from transformer import input_output_vector_constuctor
X, y = input_output_vector_constructor(FOLDER_PATH_OF_IMAGES,save= True)
```
above code will create an input and output vectors and same the numpy array if save parameter is true.
Note:  You can also specify 3rd parameter file_name="somefilename" to save the numpy array with that filename

### 3)Training
Prebuild module gesture_recognizer  handles model training and recognition

```python
from gesture_recognizer import Recognizer
recognizer = Recognizer(debug=True)
recognizer.train()
```

And that is it! The Neural Network is trained and can be used to recognize your gestures

#### 4) Recognition
Use the recognize method of Recognizer() object to test your results

```python
recognizer = Recognizer()
recognizer.recognize()
```

## Built With

* [OpenCV](https://docs.opencv.org/3.0-beta/modules/core/doc/intro.html) - Computer Vision Library
* [Scikit-Learn](https://scikit-learn.org/stable/documentation.html) - Machine Learning Library

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Authors

* **Shubham Gupta** - *Initial work* - [shubhamg2404](https://github.com/shubhamg2404)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details


