
# Thanos vs. Joker Image Classification

### Introduction
This project aims to build an image classification model capable of distinguishing between two iconic characters: Thanos and Joker. Whether you're a Marvel or DC fan, this model will help you identify these characters in images.

### Data Collection
To create a robust dataset, I used the `simple_image_download` Python library. It allowed me to download images related to both Thanos and Joker. The dataset includes various poses, lighting conditions, and backgrounds, ensuring diversity for effective training.

### Model Architecture
I designed a Convolutional Neural Network (CNN) with the following architecture:

```python
model = Sequential()
model.add(Conv2D(32, (3, 3), input_shape=(64, 64, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Flatten())
model.add(Dense(units=128, activation='relu'))
model.add(Dense(units=1, activation='sigmoid'))
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
```

- The first layer is a 2D convolutional layer with 32 filters and a 3x3 kernel size, using ReLU activation.
- Max-pooling reduces spatial dimensions.
- The flattened layer prepares data for fully connected layers.
- Two dense layers follow: one with 128 units (ReLU activation) and the final output layer with a single unit (sigmoid activation).

### Data Split
I split the dataset into three subsets:
- **Training set**: Used for model training.
- **Validation set**: Used for hyperparameter tuning.
- **Test set**: Remained unseen until model evaluation.
Data augmentation techniques (shear, zoom, and horizontal flip) were applied to enhance model generalization.

### Model Training
The model was trained using the training set:

```python
training_set = train_datagen.flow_from_directory('Dataset/train',
                                                 target_size=(64, 64),
                                                 batch_size=8,
                                                 class_mode='binary')
model.fit_generator(training_set,
                    steps_per_epoch=10,
                    epochs=50,
                    validation_data=val_set,
                    validation_steps=2)
```

### Model Evaluation
After training, I evaluated the model’s performance on the test set. The accuracy achieved is shown in the result section.



### Result
![joker](https://github.com/heerthiraja/Deep-Learning-Projects/assets/109062130/8e69f682-0acb-4abc-ae5b-4e563d0428b6)

The model successfully identified Thanos and Joker in unseen images. Feel free to explore further, fine-tune hyperparameters, and expand the dataset for even better results!


### Feel free to contribute, share feedback, and enjoy exploring the Marvel and DC universes through computer vision! 

# Thank You!

