import streamlit as st
import tensorflow as tf
from tensorflow.keras.preprocessing.image import img_to_array, load_img
import numpy as np
from PIL import Image

# Load the trained model
model = tf.keras.models.load_model('model2.h5')

# Define the class names
class_names = ['Apple Scab', 'Apple Black Rot', 'Apple Cedar Rust', 'Apple Healthy', 
               'Corn Cercospora Leaf Spot', 'Corn Common Rust', 'Corn Northern Leaf Blight', 'Corn Healthy',
               'Grape Black Rot', 'Grape Esca', 'Grape Leaf Blight', 'Grape Healthy',
               'Peach Bacterial Spot', 'Peach Healthy', 'Pepper Bell Bacterial Spot', 'Pepper Bell Healthy',
               'Potato Early Blight', 'Potato Late Blight', 'Potato Healthy', 'Strawberry Leaf Scorch',
               'Strawberry Healthy', 'Tomato Bacterial Spot', 'Tomato Early Blight', 'Tomato Late Blight',
               'Tomato Leaf Mold', 'Tomato Septoria Leaf Spot', 'Tomato Spider Mites', 'Tomato Target Spot',
               'Tomato Yellow Leaf Curl Virus', 'Tomato Mosaic Virus', 'Tomato Healthy']

# Function to make predictions
def predict_disease(image):
    img = image.resize((128, 128))
    img = img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img = img / 255.0

    predictions = model.predict(img)
    prediction_idx = np.argmax(predictions)
    confidence = np.max(predictions)

    return class_names[prediction_idx], confidence

# Streamlit app layout
st.title("Leaf Disease Detection")
st.write("Upload an image of a leaf to detect its disease.")

# File uploader
uploaded_file = st.file_uploader("Choose a leaf image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    st.write("")

    # Predict button
    if st.button('Predict'):
        st.write("Classifying...")
        label, confidence = predict_disease(image)
        st.write(f"Prediction: **{label}**")
        st.write(f"Confidence: **{confidence*100:.2f}%**")

