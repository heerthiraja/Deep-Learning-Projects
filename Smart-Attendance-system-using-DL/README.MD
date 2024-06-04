# Facial Recognition Attendance System

This project implements a facial recognition system for attendance purposes, utilizing Python libraries like OpenCV, TensorFlow, and scikit-learn to achieve real-time recognition.


## The project is organized into the following folders:

data/: This folder stores the labeled image datasets used for training the model.

embeddings/: This folder contains the extracted facial embeddings generated during preprocessing.

model/: This folder holds the trained facial recognition model.

scripts/: This folder contains Python scripts for:

data_creation.py: Captures user data and creates labeled image datasets.

preprocessing.py: Preprocesses images and extracts facial embeddings.

train_model.py: Trains the facial recognition model.

real_time_recognition.py: Implements live recognition and attendance marking.

utils/: This folder contains utility functions used throughout the project (optional).


## Dependencies

- Python 3.7
- TensorFlow 2.4.0
- Keras 2.4.0
- OpenCV
- NumPy
- scikit-learn
- imutils (optional)
- pickle


Install Dependencies: Use pip install <package_name> to install the required dependencies.

## Download Pre-trained Models:

Download a pre-trained deep learning model for facial feature extraction, compatible with TensorFlow (explore alternatives like VGGFace2).
Download a pre-trained face detection model (like "haarcascade_frontalface_default.xml") or train your own.

Create Datasets: Run scripts/data_creation.py to capture user data and create labeled image datasets.

## Process

Preprocess Data: Run scripts/preprocessing.py to preprocess images and generate embeddings.

Train Model: Run scripts/train_model.py to train the facial recognition model using TensorFlow and Keras.

Real-Time Recognition: Run scripts/real_time_recognition.py to experience live recognition and potentially integrate with your attendance management system.

## Demo
https://github.com/heerthiraja/Deep-Learning-Projects/assets/109062130/30226b2d-20a6-48a3-b37c-5e7ff058c072

## Code

### For Data Creation:
![Data-Creation](https://github.com/heerthiraja/Deep-Learning-Projects/assets/109062130/d66adcb1-5f4a-421e-9e9c-4464d0e9f3b5)

### Another way of Data creation from google
![Dataset-download-from-google](https://github.com/heerthiraja/Deep-Learning-Projects/assets/109062130/1f345fd2-f019-4059-ba44-e2f36337c980)

### Preprocessing the Embeddings
![Preprocessing-the-Embeddings](https://github.com/heerthiraja/Deep-Learning-Projects/assets/109062130/a830a8c3-a3ee-42e2-ab71-8312c9ee7724)

### Training FaceML
![Training-faceML](https://github.com/heerthiraja/Deep-Learning-Projects/assets/109062130/857c949b-d054-440e-9ac5-61c310fae478)

### Recognizing Person
![Recognizing-Person](https://github.com/heerthiraja/Deep-Learning-Projects/assets/109062130/9f8d0839-2d9c-4191-9803-37410b95fc7c)

Further Enhancements

Integrate the system with an existing attendance management platform.
Implement security measures for user authentication.
Enhance the user interface for a more user-friendly experience.
Explore more advanced deep learning models for facial feature extraction.

# Thank You!


