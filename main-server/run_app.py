import os

from api.image_receiver import app
# some_fields.py
import sys
sys.path.insert(0, '../constants')
from fields import *

if __name__ == '__main__':
    app.debug = True
    #app.config['DATABASE_NAME'] = 'library.db'
    host = os.environ.get('IP', '0.0.0.0')
    port = int(os.environ.get('PORT', main_server_port))
    app.run(host=host, port=port)
