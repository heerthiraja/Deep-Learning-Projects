Leaf Disease Detection using Deep Learning :-)

Overview:

This project focuses on utilizing deep learning techniques for leaf disease detection. It includes two major components: the training code and the test code.

Training Code:

The training code is responsible for creating a convolutional neural network (CNN) model for leaf disease detection.

Here's a brief overview of the training code:

The code imports necessary libraries such as Keras for building the neural network.

A CNN model is defined and trained with various layers for feature extraction, including convolutional layers, max-pooling layers, batch normalization, and dropout layers.

ImageDataGenerator is used to augment and preprocess training data.

The model is compiled with an optimizer, loss function, and evaluation metrics.

Training data is loaded and the model is trained, and the trained model is saved in JSON and HDF5 formats.

Test Code:

The test code provides a graphical user interface (GUI) for users to upload images and predict leaf disease. 

Key features of the test code include:

It uses Tkinter for creating the GUI.
Users can browse and select an image for disease prediction.

The saved CNN model is loaded, and the selected image is preprocessed.

The model predicts the disease class, and the result is displayed to the user.
Usage:

Clone the repository.

Train the model by running the training code, which includes the creation of the dataset, model training, and model saving.

Run the test code to predict leaf disease using the trained model.

Dataset:
A labeled dataset was collected for various leaf diseases, with each image categorized by disease type. The dataset was split into training, validation, and test sets.
