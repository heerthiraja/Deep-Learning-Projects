# Drowsiness Detection Using Computer Vision

This project implements a real-time drowsiness detection system using computer vision techniques. By analyzing the Eye Aspect Ratio (EAR) from a live video feed, the system can detect when a person is becoming drowsy and issue an alert, helping to prevent accidents caused by driver fatigue.


## Table of Contents

1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Demo](#demo)
4. [Project Overview](#project-overview)
5. [How It Works](#How-it-works)
6. [Key Features](#key-features)
7. [Conclusion](#conclusion)
8. [Acknowledgments](#acknowledgments)


## Introduction

Drowsiness while driving is a major cause of road accidents globally. This project aims to create a system that can detect drowsiness in real-time by analyzing eye movements using a webcam. The system triggers an alert if it detects that the driver is drowsy, thereby potentially preventing accidents.


## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/your-repo.git
    ```

2. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```



Demo
Check out the system in action:

https://github.com/user-attachments/assets/efa3b581-87f6-499f-8cd8-6c46912c0363



## Project Overview

This project leverages a combination of computer vision techniques and a well-known face landmarks detector provided by dlib to monitor the eye aspect ratio (EAR). The system continuously checks for signs of drowsiness and alerts the user with an audible beep if the eyes remain closed for a certain period.



## How It Works

1. **Eye Aspect Ratio (EAR) Calculation**:

  - EAR is calculated using the distances between specific facial landmarks around the eyes.

  - If the EAR falls below a certain threshold (earThresh) for a consecutive number of frames (earFrames), the system considers the user drowsy.

2. **Face and Eye Detection**:

  - The system uses dlib's pre-trained facial landmark detector to locate the face and the eyes in each frame of the video feed.

3. **Alert System**:

  - If drowsiness is detected, a visual warning is displayed on the screen, and an audible beep is sounded to alert the user.

4. **Continuous Monitoring**:

  - The system runs in real-time, continuously monitoring the user's eyes and updating the EAR calculation.



## Key Features

**Real-Time Monitoring**: The system processes video frames in real-time for instant detection.

**Non-Intrusive**: It only requires a standard webcam, making it easy to deploy.

**Customizable Parameters**: EAR threshold and frame count can be adjusted for different sensitivity levels.



## Conclusion

This drowsiness detection system is a practical tool for enhancing driver safety. By using computer vision to monitor signs of drowsiness, it provides an effective solution for preventing accidents caused by driver fatigue.



## Acknowledgments

  - dlib library for providing the face landmark detection model.
  - OpenCV and imutils libraries for handling image processing tasks.
  - Scipy library for calculating Euclidean distances used in EAR computation.

# Thank YOU!
