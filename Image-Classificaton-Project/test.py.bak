from keras.models import model_from_json
import numpy as np
from keras.preprocessing import image

json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
model = model_from_json(loaded_model_json)
model.load_weights("model.h5")
print("Loaded model from disk")

def classify(img_file):
    img_name = img_file
    test_image = image.load_img(img_name, target_size = (64, 64))

    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis=0)
    result = model.predict(test_image)

    if result[0][0] == 1:
        prediction = 'Thanos'
    else:
        prediction = 'Joker'
    print(prediction,img_name)


import os
path = 'D:/MasterClass/Artificial_Intelligence/Day12/Code/Dataset/test'
files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
   for file in f:
     if '.jpeg' in file:
       files.append(os.path.join(r, file))

for f in files:
   classify(f)
   print('\n')