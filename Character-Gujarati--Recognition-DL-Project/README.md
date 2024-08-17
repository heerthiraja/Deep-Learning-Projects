# Gujarati Character Recognition Using CNN and PyQt5

This project demonstrates the recognition of Gujarati characters using a Convolutional Neural Network (CNN). The model is trained to classify images of Gujarati characters into 45 different categories, enabling efficient and accurate character recognition.

## Table of Contents

1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Demo](#demo)
4. [Let's break down the code step by step](#Let's-break-down-the-code-step-by-step)
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

https://github.com/user-attachments/assets/69026880-7f16-4e08-8fe9-596b5797c17a

## Let's break down the code step by step:

1. **Importing Libraries**:
  - Import necessary libraries from TensorFlow, Keras, PyQt5, and other Python packages for building, training, and deploying the CNN model.

2. **Model Architecture**:
  - Define the Convolutional Neural Network (CNN) architecture with multiple convolutional, pooling, batch normalization, and dropout layers to extract features and prevent overfitting. The model is designed to classify images into 45 different Gujarati character classes.

3. **Compiling the Model**:
  - Compile the model using the Adam optimizer and categorical cross-entropy loss function to prepare it for training.

4. **Data Augmentation**:
  - Use ImageDataGenerator to augment the training data with techniques like rescaling, shearing, zooming, and horizontal flipping to improve model generalization.

5. **Loading Data**:
  - Load the training and validation datasets from directories, specifying the target image size (128x128) and batch size. Ensure that the data is organized into respective folders for each character class.

6. **Training the Model**:
  - Train the model using the training dataset and validate it using the validation dataset, specifying the number of epochs and steps per epoch. The model's performance is monitored and adjusted during training.

8. **Saving the Model**:
  - Save the trained model architecture and weights to disk (model.json and model.h5) for future use and deployment.

9. **Creating a GUI for Testing**:
  - Develop a graphical user interface (GUI) using PyQt5 to allow users to upload images and get predictions from the trained model. The GUI provides buttons for browsing images, classifying them, and viewing the recognized character.

10. **Loading the Model in GUI**:
  - Load the saved model architecture and weights in the GUI application. The model is loaded and prepared to make predictions on user-uploaded images.

11. **Image Prediction**:
  - Preprocess the uploaded image, make predictions using the loaded model, and display the predicted Gujarati character label on the GUI. The result is shown in the text box within the GUI.

12. **Cleanup**:
Ensure proper cleanup by releasing resources and closing any open windows after the GUI application is closed. This includes freeing up memory and closing any open file handles.


## Summary:
  - This project uses a Convolutional Neural Network (CNN) to detect and classify Gujarati characters, providing a user-friendly GUI for real-time predictions. The application is built with TensorFlow, Keras, and PyQt5, making it a comprehensive solution for character recognition tasks.

## Acknowledgments
We thank the developers of TensorFlow, Keras, and PyQt5 for their valuable resources, as well as the creators of the Gujarati character dataset used in this project.




