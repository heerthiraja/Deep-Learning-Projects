# Object Recognition using MobileNet SSD

This project demonstrates real-time object recognition using the MobileNet Single Shot MultiBox Detector (SSD). The MobileNet architecture is lightweight and well-suited for real-time applications on resource-constrained devices.

## Table of Contents

1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Results and Examples](#results-and-examples)
5. [Contributing](#contributing)
6. [License](#license)
7. [Acknowledgments](#acknowledgments)

## Introduction

The goal of this project is to detect and label objects in a live webcam feed. We use the MobileNet SSD model, which is pre-trained on the COCO dataset and capable of detecting 20 different object classes.

## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/your-username/your-repo.git
    ```

2. Install the necessary Python packages:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the object recognition script:

    ```bash
    python object_recognition.py
    ```

2. The webcam feed will open, and detected objects will be highlighted with bounding boxes and labels.

## Results and Examples

![Object Recognition Example](example.gif)

## Demo

https://github.com/heerthiraja/Deep-Learning-Projects/assets/109062130/56a249a4-6971-4ed5-87e5-145000318eda


Let's break down the code step by step:

1. **Importing Libraries**:
    - We start by importing the necessary Python libraries:
        - `numpy`: For mathematical operations.
        - `imutils`: To resize images.
        - `cv2` (OpenCV): For image acquisition and manipulation.
        - `time`: To introduce a delay (used later).

2. **Model and Configuration Files**:
    - We define the paths to the MobileNet SSD model and its corresponding prototxt file:
        - `prototxt`: Path to the prototxt file.
        - `model`: Path to the pre-trained MobileNet SSD model.

3. **Threshold and Class Labels**:
    - We set a confidence threshold (`confThresh`) to filter out low-confidence detections.
    - The `CLASSES` list contains the names of the 20 object classes that the MobileNet SSD model can detect.

4. **Loading the Model**:
    - We load the MobileNet SSD model using OpenCV's `dnn` module.
    - The model is based on a deep neural network architecture and has been trained to recognize objects.

5. **Initializing the Camera Feed**:
    - We initialize the webcam feed using `cv2.VideoCapture(0)`.
    - A delay of 2 seconds (`time.sleep(2.0)`) allows the camera to stabilize.

6. **Main Loop**:
    - We continuously read frames from the camera (`vs.read()`).
    - Each frame is resized to a width of 500 pixels (`imutils.resize(frame, width=500)`).
    - We preprocess the resized frame by creating a blob (binary large object) using `cv2.dnn.blobFromImage`.
    - The blob is set as input to the MobileNet SSD model (`net.setInput(blob)`).
    - The model predicts detections, and we iterate through them:
        - If the confidence of a detection is above the threshold, we extract the class index, bounding box coordinates, and label.
        - We draw bounding boxes around detected objects and display their labels on the frame.
    - The processed frame is displayed in a window (`cv2.imshow("Frame", frame)`).
    - Pressing the 'q' key quits the loop.

7. **Cleanup**:
    - After exiting the loop, we release the camera (`vs.release()`) and close the OpenCV windows (`cv2.destroyAllWindows()`).

8. **Summary**:
    - This code captures webcam frames, processes them using the MobileNet SSD model, and displays detected objects with bounding boxes and labels.


## Acknowledgments

- We thank the authors of the MobileNet SSD model and the COCO dataset for their valuable contributions.


#Thank You!



