import requests

import os
from flask import Flask, request, redirect, url_for

from PIL import Image
import numpy as np
import PIL.ImageOps

from io import BytesIO
import base64

# some_fields.py
import sys
sys.path.insert(0, '../constants')
from fields import *

app = Flask(__name__)

@app.route('/receiver', methods=['POST'])
def predict_digit():
    encoded = request.form['sample_image']
    
    im = Image.open(BytesIO(base64.b64decode(encoded)))

    #im.show()
    
    # defining the api-endpoint  
    URL = "http://"+detection_server_ip+":"+detection_server_port+"/predict"
    
    # data to be sent to api 
    data = {'sample_image':encoded}

    # sending post request and saving response as response object 
    r = requests.post(url = URL, data = data)

    print(r.text)

    #return str(predict(im))
    return "sample: normal"