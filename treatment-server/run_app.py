import os

from api.doctors_info import app

if __name__ == '__main__':
    app.debug = True
    #app.config['DATABASE_NAME'] = 'library.db'
    host = os.environ.get('IP', '0.0.0.0')
    port = int(os.environ.get('PORT', 5002))
    app.run(host=host, port=port)