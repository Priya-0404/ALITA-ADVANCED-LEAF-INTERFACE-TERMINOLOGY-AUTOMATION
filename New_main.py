                       #  ALITA - ADVANCED LEAF INTERFACE TERMINOLOGY ANALYSIS


#  'Ashok_tree': 0
#  'Chilbil_tree': 1
#  'Neem_tree': 2
#  'Pipal_tree': 3

#IMPORTING NECESSARY MODULES

from keras.models import load_model
import numpy as np
import os
from statistics import mode
from keras.preprocessing.image import img_to_array, load_img
from keras.applications.vgg19 import preprocess_input

# RENAMING CAPTURED IMAGES FROM ARDUINO

data = os.listdir("CapturedImages")
j=1
for i in range(0,len(data)):
    path = data[i]
    source = "CapturedImages/" + str(path)
    destination = "CapturedImages/" + str(j) + ".jpg"
    os.rename(source, destination)
    j += 1

#ANALYZING THE LEAF

model = load_model("e.h5")
capturedCount = len(os.listdir("CapturedImages"))

predict = []
for i in range(1,capturedCount+1):
    img = load_img(f"CapturedImages/{i}.jpg", target_size= (256, 256))
    i = img_to_array(img)
    im = preprocess_input(i)
    img = np.expand_dims(im, axis= 0)
    pred = np.argmax(model.predict(img))
    predict.append(pred)

tree = mode(predict)

if(tree == 0):
    print("Ashok Tree")
elif(tree == 1):
    print("Elm or Chilbil Tree")
elif(tree == 2):
    print("Neem Tree")
elif(tree == 3):
    print("Pipal Tree")
else:
    print("Please scan a defined leaf- Ashok,Elm or Chilbil, Mulberry, Neem, Pipal tree")

# DELETING IMAGES FROM ARDUINO CAPTURED FOLDER FOR NEW IMAGES

data = os.listdir("CapturedImages")
for file in data:
    os.remove(f"CapturedImages/{file}")

