import requests
from PIL import Image

import base64
from io import BytesIO

import json

# some_fields.py
import sys
sys.path.insert(0, '../constants')
from fields import *

#load image
img = Image.open("sam2.jpg")

#pil to base64
buffered = BytesIO()
img.save(buffered, format="JPEG")
img_str = base64.b64encode(buffered.getvalue())

# defining the api-endpoint  
#URL = "http://"+main_server_ip+":"+main_server_port+"/receiver"
URL = "http://"+treatment_server_ip+":"+treatment_server_port+"/doctors"

# data to be sent to api 
data = {"lat":"23","lon":"88"}

# sending post request and saving response as response object 
r = requests.post(url = URL, data = data)

python_obj = json.loads(r.text)

print(python_obj[0])