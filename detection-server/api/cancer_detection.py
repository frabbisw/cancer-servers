import os
from flask import Flask, request, redirect, url_for

from PIL import Image
from PIL import Image
import PIL.ImageOps

from io import BytesIO
import base64

import numpy as np
from keras.models import model_from_json
import tensorflow as tf

from keras import backend as K

# load json and create model
json_file = open('models/resnet50.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
loaded_model.summary()
#load weights
loaded_model.load_weights('models/resnet50.h5')

graph = tf.get_default_graph()

app = Flask(__name__)

def classify_cell(img):
    global graph
    with graph.as_default():
        img = np.asarray(img.resize((224,224)))
        x = np.expand_dims(img, axis=0)

        Y_pred = loaded_model.predict(x)

    return Y_pred

@app.route('/detect', methods=['POST'])
def predict_cancer():
    img = request.form['sample_image']
    
    img = Image.open(BytesIO(base64.b64decode(img)))

    #img.show()
    v = "result: "+str(classify_cell(img))
    #classify_cell(img)
    
    return v