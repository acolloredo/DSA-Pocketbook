from flask import Flask
from flask_cors import CORS
import time

app = Flask(__name__)
CORS(app, supports_credentials=True)


@app.route('/time')
def get_current_time():
    return {'time': time.time()}
