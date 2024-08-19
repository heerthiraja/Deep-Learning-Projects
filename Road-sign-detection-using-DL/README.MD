# Road Sign Recognition Using Convolutional Neural Networks (CNN)

This project demonstrates the implementation of a Road Sign Recognition system using a Convolutional Neural Network (CNN) in Python. The system can classify various road signs, which is crucial for autonomous driving and advanced driver-assistance systems (ADAS). A graphical user interface (GUI) is provided using PyQt5 for ease of interaction.

## Table of Contents

1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Demo](#demo)
4. [How to Use](#how-to-use)
5. [Model Architecture](#model-architecture)
6. [Training the Model](#training-the-model)
7. [Testing and Classifying](#testing-and-classifying)
8. [GUI Interface](#gui-interface)
9. [Results](#results)
10. [Acknowledgments](#acknowledgments)

## Introduction

  The objective of this project is to accurately recognize road signs from images using deep learning techniques. The system leverages a CNN model trained on the German Traffic Sign Recognition Benchmark (GTSRB) dataset, which includes 43 classes of road signs. A PyQt5 GUI is built to facilitate model training, testing, and real-time classification of road signs.

1. Clone this repository:

    ```bash
    git clone https://github.com/your-username/road-sign-detection.git
    ```

2. Install the necessary Python packages:

    ```bash
    pip install -r requirements.txt
    ```


## Demo

  https://github.com/user-attachments/assets/77578538-80e3-4930-9590-0ffdf6f50e61


## Dataset Preparation

To collect data for the Road Sign Recognition project, you can follow these steps:

### 1. **Use Existing Datasets**
   - **German Traffic Sign Recognition Benchmark (GTSRB):** A widely-used dataset containing 43 classes of road signs. You can download it from official sources or repositories like Kaggle.

### 2. **Capture Images Manually**
   - **Smartphone/Camera:** Use a smartphone or digital camera to capture images of road signs from different angles, lighting conditions, and distances.
   - **GPS Tagging:** Include GPS data with images to enhance location-specific model capabilities.

### 3. **Data Augmentation**
   - **Image Transformation:** Apply techniques like rotation, zooming, flipping, and color variations to existing images to artificially increase the dataset size and variety.

### 4. **Crowdsourcing**
   - **Public Contributions:** Create a platform where users can upload road sign images, ensuring diversity in image sources.

### 5. **Simulated Environments**
   - **Use Driving Simulators:** Capture road sign images from driving simulators that can replicate various traffic scenarios.

### 6. **Scrape Images Online**
   - **Web Scraping:** Use Python libraries like `BeautifulSoup` and `Selenium` to scrape road sign images from the internet, ensuring they are labeled correctly and sorted into categories.

Always ensure that your collected data is properly labeled and categorized according to the different types of road signs for effective model training.

## How to Use
  
### Run the Application
  ```bash
  python main.py
  ```
  
## GUI Interface

**Browse Image**: Load an image of a road sign for classification.
**Classify**: Classify the loaded image using the trained model.
**Training**: Train the model on the dataset. This will also save the trained model to disk.

## Model Architecture

### The CNN architecture consists of:

**Convolutional Layers**: For feature extraction using filters.
**Max-Pooling Layers**: For down-sampling and reducing the spatial dimensions.
**Dropout Layers**: To prevent overfitting by randomly dropping neurons during training.
**Fully Connected Layers**: For final classification into 43 road sign categories.

## Training the Model

  The model can be trained by clicking the Training button in the GUI. The model is compiled using the Adam optimizer and categorical cross-entropy loss function. Training accuracy and validation accuracy, as well as loss, are plotted and saved as images.

## Testing and Classifying

  You can test the model by loading an image via the GUI and clicking on Classify. The model will predict the class of the road sign and display the recognized class in the GUI.


## GUI Interface

  The GUI is built using PyQt5, providing a simple and user-friendly interface to interact with the model.

**Browse Image**: Allows the user to load a road sign image.
**Classify**: Classifies the loaded image and displays the recognized road sign.
**Training**: Trains the model with the dataset and saves it for future use.

## Results

  The model achieves satisfactory accuracy on the test set, with performance metrics plotted and saved during the training process.

## Model Accuracy

  ![Accuracy](https://github.com/user-attachments/assets/9efed679-e82a-41df-8d05-dc19a0feeb64)

## Model Loss

  ![Loss](https://github.com/user-attachments/assets/09833742-a0c3-42ef-b895-ca943b0096c4)
  
##Acknowledgments

  This project utilizes the GTSRB dataset and various Python libraries including TensorFlow, Keras, and PyQt5. Special thanks to the open-source community for providing these valuable resources.
