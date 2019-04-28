import requests
from PIL import Image

import base64
from io import BytesIO

#load image
img = Image.open("sam2.jpg")

#pil to base64
buffered = BytesIO()
img.save(buffered, format="JPEG")
img_str = base64.b64encode(buffered.getvalue())


# defining the api-endpoint  
URL = "http://192.168.0.101:5001/detect"

# data to be sent to api 
data = {'sample_image':img_str}

# sending post request and saving response as response object 
r = requests.post(url = URL, data = data)

print(r.text)