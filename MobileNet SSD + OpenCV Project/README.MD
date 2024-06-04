# MobileNet SSD

## Facial Recognition Attendance System

This project implements a facial recognition system for attendance purposes, utilizing Python libraries like OpenCV, TensorFlow, and scikit-learn to achieve real-time recognition.

## Table of Contents

Project Structure
Dependencies
Getting Started
Usage
Further Enhancements
License
Project Structure

The project is organized into the following folders:

data/: This folder stores the labeled image datasets used for training the model.
embeddings/: This folder contains the extracted facial embeddings generated during preprocessing.
model/: This folder holds the trained facial recognition model.
scripts/: This folder contains Python scripts for:
data_creation.py: Captures user data and creates labeled image datasets.
preprocessing.py: Preprocesses images and extracts facial embeddings.
train_model.py: Trains the facial recognition model.
real_time_recognition.py: Implements live recognition and attendance marking.
utils/: This folder contains utility functions used throughout the project (optional).
README.md: This file (you are currently reading it!).
Dependencies

Python 3.7
TensorFlow 2.4.0
Keras 2.4.0
OpenCV
NumPy
scikit-learn
imutils (optional)
pickle
Getting Started

Install Dependencies: Use pip install <package_name> to install the required dependencies.

Download Pre-trained Models:

Download a pre-trained deep learning model for facial feature extraction, compatible with TensorFlow (explore alternatives like VGGFace2).
Download a pre-trained face detection model (like "haarcascade_frontalface_default.xml") or train your own.
Create Datasets: Run scripts/data_creation.py to capture user data and create labeled image datasets.

Usage

Preprocess Data: Run scripts/preprocessing.py to preprocess images and generate embeddings.

Train Model: Run scripts/train_model.py to train the facial recognition model using TensorFlow and Keras.

Real-Time Recognition: Run scripts/real_time_recognition.py to experience live recognition and potentially integrate with your attendance management system.

Further Enhancements

Integrate the system with an existing attendance management platform.
Implement security measures for user authentication.
Enhance the user interface for a more user-friendly experience.
Explore more advanced deep learning models for facial feature extraction.
License

This project is licensed under the MIT License (refer to LICENSE file for details).
