'''
   1. Number of times pregnant
   2. Plasma glucose concentration a 2 hours in an oral glucose tolerance test
   3. Diastolic blood pressure (mm Hg)
   4. Triceps skin fold thickness (mm)
   5. 2-Hour serum insulin (mu U/ml)
   6. Body mass index (weight in kg/(height in m)^2)
   7. Diabetes pedigree function
   8. Age (years)
   9. Class variable (0 or 1)
'''


from numpy import loadtxt #load the dataset
from keras.models import Sequential #adding the layers in sequential order
from keras.layers import Dense #mathematical 

#load the data into the dataset variable
dataset = loadtxt('pima-indians-diabetes.csv', delimiter=',') #read/load the dataset

#segregate dataset into input and output
x = dataset[:,0:8] #input/feature/x
y = dataset[:,8] #output/classes/y
print(x)

#designing neural neural network
model = Sequential()
model.add(Dense(12, input_dim=8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

#compile
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

#train
model.fit(x, y, epochs=50, batch_size=10)

#evaluate the model
_, accuracy = model.evaluate(x, y)
print('Accuracy: %.2f' % (accuracy*100))

model_json = model.to_json()
with open("model.json", "w") as json_file:
    json_file.write(model_json)
model.save_weights("model.h5")
print("Saved model to disk")
