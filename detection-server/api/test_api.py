import os

from PIL import Image
from PIL import Image
import PIL.ImageOps

from io import BytesIO
import base64

import numpy as np
from keras.models import load_model
from keras.models import model_from_json

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 

# load json and create model
json_file = open('../models/resnet50.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
loaded_model.summary()
#load weights
loaded_model.load_weights('../models/resnet50.h5')

def classify_cell(img):
    img = np.asarray(img.resize((224,224)))
    x = np.expand_dims(img, axis=0)
    Y_pred = loaded_model.predict(x)
    
    return Y_pred

img = Image.open("../../test/norm.jpg")
ccc = classify_cell(img)

print(ccc)