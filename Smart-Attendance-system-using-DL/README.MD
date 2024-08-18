# Smart Attendance System

The Smart Attendance System is a facial recognition-based attendance management system that automates the process of recording attendance. By capturing and recognizing faces, the system ensures that attendance records are accurate and tamper-proof. This system is ideal for educational institutions, corporate offices, and other organizations where attendance tracking is crucial.

## Table of Contents

1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Demo](#demo)
4. [Code](#Code)
5. [Acknowledgments](#acknowledgments)

## Introduction

The goal of this project is to detect and classify Gujarati characters using a CNN. The model is trained on a dataset of Gujarati characters and can identify 45 different character classes. The application also provides a user-friendly graphical user interface (GUI) built with PyQt5, allowing users to upload images and get real-time predictions.

## Introduction

1. Clone this repository:

    ```bash
    git clone https://github.com/your-username/gujarati-character-recognition.git
    ```

2. Install the necessary Python packages:

    ```bash
    pip install -r requirements.txt
    ```


## Demo

https://github.com/heerthiraja/Deep-Learning-Projects/assets/109062130/30226b2d-20a6-48a3-b37c-5e7ff058c072



## The project is organized into the following folders:


**data/**: This folder stores the labeled image datasets used for training the model.

**Embeddings/**: This folder contains the extracted facial embeddings generated during preprocessing.

**Model/**: This folder holds the trained facial recognition model.

**scripts/**: This folder contains Python scripts for:

**data_creation.py**: Captures user data and creates labeled image datasets.

**preprocessing.py**: Preprocesses images and extracts facial embeddings.

**train_model.py**: Trains the facial recognition model.

**real_time_recognition.py**: Implements live recognition and attendance marking.

**utils/**: This folder contains utility functions used throughout the project (optional).


## Dependencies

- Python 3.7 or Higher
- TensorFlow 2.4.0
- Keras 2.4.0
- OpenCV
- NumPy
- scikit-learn
- imutils (optional)
- pickle
- PyTorch
- Caffe


Install Dependencies: Use pip install <package_name> to install the required dependencies.


## Download Pre-trained Models:

Download a pre-trained deep learning model for facial feature extraction, compatible with TensorFlow (explore alternatives like VGGFace2).
Download a pre-trained face detection model (like "haarcascade_frontalface_default.xml") or train your own.

Create Datasets: Run scripts/data_creation.py to capture user data and create labeled image datasets.

## Process

Preprocess Data: Run scripts/preprocessing.py to preprocess images and generate embeddings.

Train Model: Run scripts/train_model.py to train the facial recognition model using TensorFlow and Keras.

Real-Time Recognition: Run scripts/real_time_recognition.py to experience live recognition and potentially integrate with your attendance management system.



## Code

### For Data Creation:

### Follow the Prompts:

- Enter the user's name.
- Enter the user's roll number.
- The system will capture 50 images from the webcam and store them in the dataset directory under the user's name.

### Verify the Dataset:

The images are stored in dataset/{Name}.

![Data-Creation](https://github.com/heerthiraja/Deep-Learning-Projects/assets/109062130/d66adcb1-5f4a-421e-9e9c-4464d0e9f3b5)

### Another way of Data creation from google

![Dataset-download-from-google](https://github.com/heerthiraja/Deep-Learning-Projects/assets/109062130/1f345fd2-f019-4059-ba44-e2f36337c980)

### Preprocessing the Embeddings - Facial Embeddings

The facial embedding process converts images into a numerical vector representation, making it easier to compare faces.

### Process:

- The script processes each image in the dataset directory.
- It detects faces using a deep learning model and extracts facial embeddings.
- The embeddings are stored in output/embeddings.pickle.


![Preprocessing-the-Embeddings](https://github.com/heerthiraja/Deep-Learning-Projects/assets/109062130/a830a8c3-a3ee-42e2-ab71-8312c9ee7724)

### Training FaceML
- Train the model using the facial embeddings to recognize faces.

### Process:

- The embeddings and corresponding labels are loaded.
- The SVM model is trained using these embeddings.
- The trained model and label encoder are saved as recognizer.pickle and le.pickle in the output directory.


![Training-faceML](https://github.com/heerthiraja/Deep-Learning-Projects/assets/109062130/857c949b-d054-440e-9ac5-61c310fae478)

### Recognizing Person

- Recognize individuals in real-time and record their attendance.

### Process:

- The system starts the webcam and detects faces.
- It matches the detected faces with the trained model.
- If a match is found, the user's name and roll number are displayed, and the attendance is recorded in student.csv.


![Recognizing-Person](https://github.com/heerthiraja/Deep-Learning-Projects/assets/109062130/9f8d0839-2d9c-4191-9803-37410b95fc7c)


## Summary

This Smart Attendance System project automates the attendance process using facial recognition technology, providing an efficient, error-free, and user-friendly solution for educational institutions and workplaces.

## Acknowledgments

We extend our gratitude to the developers of the facial recognition libraries and the authors of the datasets used in training. Special thanks to the open-source community for their contributions, making this project possible.


Further Enhancements

- Integrate the system with an existing attendance management platform.
- Implement security measures for user authentication.
- Enhance the user interface for a more user-friendly experience.
- Explore more advanced deep learning models for facial feature extraction.

# Thank You!


