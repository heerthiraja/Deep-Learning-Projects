# Leaf Disease Detection Using Computer Vision

This project demonstrates the detection of leaf diseases using a Convolutional Neural Network (CNN). The model is trained to classify images of leaves into different disease categories, helping farmers take timely actions to protect their crops.

## Table of Contents

1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Demo](#demo)
4. [Let's break down the code step by step](#Let's-break-down-the-code-step-by-step)
5. [Acknowledgments](#acknowledgments)

## Introduction

The goal of this project is to detect and classify leaf diseases using a CNN. The model is trained on a dataset of leaf images with various diseases and can identify 25 different disease categories.

## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/your-username/your-repo.git
    ```

2. Install the necessary Python packages:

    ```bash
    pip install -r requirements.txt
    ```


## Demo

https://github.com/user-attachments/assets/cee1cdad-9c91-423b-98b1-9cea3d702cb3

## Let's break down the code step by step:

1. **Importing Libraries**:
    - Import necessary libraries from TensorFlow, Keras, and other Python packages for building and training the CNN model.

2. **Model Architecture**:
    - Define the Convolutional Neural Network (CNN) architecture with multiple convolutional, pooling, batch normalization, and dropout layers to extract features and prevent overfitting.

3. **Compiling the Model**:
    - Compile the model using an optimizer (e.g., Adam) and a loss function (e.g., categorical cross-entropy) to prepare it for training.

4. **Data Augmentation**:
    - Use ImageDataGenerator to augment the training data with techniques like rescaling, shearing, zooming, and horizontal flipping to improve model generalization.

5. **Loading Data**:
    - Load the training and validation datasets from directories, specifying the target image size and batch size.

6. **Training the Model**:
    - Train the model using the training dataset and validate it using the validation dataset, specifying the number of epochs and steps per epoch.

7. **Saving the Model**:
    - Save the trained model architecture and weights to disk for future use.

8. **Creating a GUI for Testing**:
    - Develop a graphical user interface (GUI) using Tkinter to allow users to upload images and get predictions from the trained model.

9. **Loading the Model in GUI**:
   - Load the saved model architecture and weights in the GUI application.

10. **Image Prediction**:
    - Preprocess the uploaded image, make predictions using the loaded model, and display the predicted disease label on the GUI.

11. **Cleanup**:
    - Ensure proper cleanup by releasing resources and closing any open windows after the GUI application is closed.

**Summary**:
    
- This project uses a Convolutional Neural Network (CNN) to detect and classify leaf diseases, providing a user-friendly GUI for real-time predictions.

## Acknowledgments

 - We thank the authors of the dataset and the contributors to the TensorFlow and Keras libraries for their valuable resources.

# Thank you!
