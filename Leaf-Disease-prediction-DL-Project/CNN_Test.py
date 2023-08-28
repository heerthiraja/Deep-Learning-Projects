import tkinter as tk
from tkinter import filedialog
import numpy as np
from keras.preprocessing import image
from keras.models import model_from_json
from tkinter import *

win=tk.Tk()

def b1_click():
    global path2
    try:
        json_file = open('model1.json', 'r')
        loaded_model_json = json_file.read()
        json_file.close()
        loaded_model = model_from_json(loaded_model_json)
        # load weights into new model
        loaded_model.load_weights("model1.h5")
        print("Loaded model from disk")
        label=["Apple___Apple_scab","Apple___Black_rot","Apple___Cedar_apple_rust","Apple___Healthy",
               "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot","Corn_(maize)___Common_rust_",
               "Corn_(maize)___Healthy","Corn_(maize)___Northern_Leaf_Blight","Grape___Black_rot",
               "Grape___Esca_(Black_Measles)","Grape___Healthy","Grape___Leaf_blight_(Isariopsis_Leaf_Spot)",
               "Potato___Early_blight","Potato___Healthy","Potato___Late_blight","Tomato___Bacterial_spot",
               "Tomato___Early_blight","Tomato___Healthy","Tomato___Late_blight","Tomato___Leaf_Mold",
               "Tomato___Septoria_leaf_spot","Tomato___Spider_mites Two-spotted_spider_mite","Tomato___Target_Spot",
               "Tomato___Tomato_Yellow_Leaf_Curl_Virus","Tomato___Tomato_mosaic_virus"]

        path2=filedialog.askopenfilename()
        print(path2)

        test_image = image.load_img(path2, target_size = (128, 128))        
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis = 0)
        result = loaded_model.predict(test_image)
        print(result)
        label2=label[result.argmax()]
        print(label2)
        lbl.configure(text=label2)
        win.mainloop()
        

    except IOError:
        pass

label1 = Label(win, text="GUI For Leaf Disease Detection using OPENCV", fg ='blue')
label1.pack()
    
b1=tk.Button(win, text= 'browse image',width=25, height=3,fg ='red', command=b1_click)
b1.pack()
lbl = Label(win, text="Result", fg ='blue')
lbl.pack()

win.geometry("550x250")
win.title("Leaf Disease Detection using OPENCV")
win.bind("<Return>", b1_click)
win.mainloop() 
