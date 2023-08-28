from keras.preprocessing import image
import numpy as np
from keras.models import model_from_json

json_file = open('model2.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
model = model_from_json(loaded_model_json)
model.load_weights("model2.h5")
print("Model Loaded Successfully")

def classify(img_file):
    img_name = img_file
    test_image = image.load_img(img_name, target_size = (128, 128))
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis=0)
    result = model.predict(test_image)
    print(result)
    classes=["A","B","C","D","E","F"]
    label2 = classes[result.argmax()]
    print(label2,img_name)
    
import os
path = 'test'
files = []
for r, d, f in os.walk(path):
   for file in f:
     if '.jpg' in file:
        print(files)
        files.append(os.path.join(r, file))
for f in files:
   classify(f)
   print('\n')
