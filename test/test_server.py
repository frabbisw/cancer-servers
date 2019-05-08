import requests
from PIL import Image

import base64
from io import BytesIO

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
URL = "http://"+main_server_ip+":"+main_server_port+"/receiver"

# data to be sent to api 
data = {'sample_image':img_str}

# sending post request and saving response as response object 
r = requests.post(url = URL, data = data)

print(r.text)
