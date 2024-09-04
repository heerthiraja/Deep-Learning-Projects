import streamlit as st
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image, ImageOps
import io

# Load the trained model
model = load_model('model2.h5')

# Class labels (Replace these with your actual class labels)
class_names = ['Apple Scab', 'Apple Black Rot', 'Apple Cedar Rust', 'Healthy Apple', 
               'Grape Black Rot', 'Grape Esca', 'Grape Leaf Blight', 'Healthy Grape', 
               'Potato Early Blight', 'Potato Late Blight', 'Healthy Potato', 
               'Tomato Bacterial Spot', 'Tomato Early Blight', 'Tomato Late Blight', 
               'Tomato Leaf Mold', 'Tomato Septoria Leaf Spot', 'Tomato Spider Mites', 
               'Tomato Target Spot', 'Tomato Yellow Leaf Curl Virus', 
               'Tomato Mosaic Virus', 'Healthy Tomato']

# Streamlit interface
st.title("🌿 Leaf Disease Detection")
st.write("Upload an image of a leaf, and the model will predict if it has a disease and identify it.")

# File uploader
uploaded_file = st.file_uploader("Choose a leaf image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display the uploaded image
    image_data = uploaded_file.read()
    st.image(image_data, caption='Uploaded Leaf Image', use_column_width=True)
    
    # Preprocess the image for prediction
    img = Image.open(io.BytesIO(image_data))
    img = img.resize((128, 128))  # Resize the image to match the input size expected by your model
    img = ImageOps.fit(img, (128, 128), Image.ANTIALIAS)
    img = np.array(img) / 255.0  # Normalize the image
    img = np.expand_dims(img, axis=0)  # Expand dimensions to match the model's input shape
    
    # Predict using the loaded model
    predictions = model.predict(img)
    score = tf.nn.softmax(predictions[0])
    predicted_class = class_names[np.argmax(score)]
    
    # Display the prediction
    st.subheader(f"Prediction: {predicted_class}")
    st.write(f"Confidence: {100 * np.max(score):.2f}%")
else:
    st.write("Please upload an image to get a prediction.")
