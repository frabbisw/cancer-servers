import os
from flask import Flask, request, redirect, url_for

from PIL import Image
import numpy as np
import PIL.ImageOps

from io import BytesIO
import base64

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict_digit():
    encoded = request.form['encoded']
    
    im = Image.open(BytesIO(base64.b64decode(encoded)))

    im.show()
    
    #return str(predict(im))
    return "sample: normal"