import os
from flask import Flask, request, redirect, url_for

from PIL import Image
from PIL import Image
import PIL.ImageOps

from io import BytesIO
import base64

import numpy as np
from keras.models import load_model

app = Flask(__name__)


model = load_model('models/detect_model.h5')
def classify_cell(img):
    img = np.asarray(img.resize((128,128)))
    x = np.expand_dims(img, axis=0)
    Y_pred = model.predict(x)
    
    return Y_pred[0][0]

@app.route('/detect', methods=['POST'])
def predict_digit():
    img = request.form['sample_image']
    
    img = Image.open(BytesIO(base64.b64decode(img)))

    #img.show()
    #print(classify_cell(img))
    ccc = "result: "+str(classify_cell(img))
    print(ccc)
    
    #return str(predict(im))
    
    return ccc