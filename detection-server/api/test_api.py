import os

from PIL import Image
from PIL import Image
import PIL.ImageOps

from io import BytesIO
import base64

import numpy as np
from keras.models import load_model


model = load_model('../models/detect_model.h5')
def classify_cell(img):
    img = np.asarray(img.resize((128,128)))
    x = np.expand_dims(img, axis=0)
    Y_pred = model.predict(x)
    
    return Y_pred[0][0]

img = Image.open("../../test/sam1.jpg")
ccc="result: "+str(classify_cell(img))
print(ccc)