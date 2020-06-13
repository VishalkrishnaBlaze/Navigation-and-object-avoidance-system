# Navigation-and-object-avoidance-system
## A pre-final year mini-project

### Description
----
This Project is a Pre-final year mini-project for MS Ramaiah University of Applied Sciences. Tae aim of this project is to take a step towards helping the blind to better navigate and see the world around them which they struggle to see. 

The project is divided into following modules:
1. Object Detection, A YOLOv3 based object detection system with upto 80 classes.
2. Traffic Light Detection, A OpenCV and numpy based traffic light detection system.

### Directory Structure
----
```
.
├── _object-detection
|   ├── _Model
│   |   ├── coco.names
|   |   ├── yolov3.cfg
|   |   └── yolov3.weights
|   └── _src
|       ├── main.py
|       ├── sound.py      
|       └── speak.mp3   
|
├── _traffic-light-detection
|   ├── _light               
|   |   ├── _extra
|   |   |   ├── _day
|   |   |   |   └── (set of tesing images in day)
|   |   |   ├── _night
|   |   |   |   └── (set of tesing images in night)
|   |   |   ├── _test
|   |   |   |   └── set of default tesing images
|   |   ├── _result
|   |   |   └── (set of labeled images saved)
|   |   └── (set of default testing images)                      
|   └── _src                      
|       ├── main.py
|       ├── sound.py
|       └── speak.mp3
|
└── README.md
```
### Getting Started
----
#### Dependencies
* Python 3.5+
* Python libraries
  * NumPy
  * opencv-python
  * gTTS
  * playsound
* YOLOv3 weights

#### Installing
Clone this Git repository using the following command `git clone https://github.com/VishalkrishnaBlaze/Navigation-and-object-avoidance-system.git`

Download the yolov3 weights from this [link](https://pjreddie.com/media/files/yolov3.weights) and move the downloaded weight to object-detection/model directory.

The object-detection/model directory should look somthing like this:
```
└── _Model
    ├── coco.names
    ├── yolov3.cfg
    └── yolov3.weights
```

#### Execution

1. To start the object detection module run the following command in the src directory of the module: `python main.py`
2. To start the traffic light detection module run the following command in the src directory of the module: `python main.py`

### Contributing Members
----
1. Vishalkrishna Bhosle
2. Vivek Badani
3. Yohann Jacob
4. Rohit Tiwari
