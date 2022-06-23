from flask import Flask, Response, request, jsonify
from flask_cors import CORS, cross_origin

import threading
import requests
import datetime
import time
import json

from setting import (
    HOST_PORT,
    HOST_URL,
    SHORT_SLEEP,
    LONG_SLEEP
)

app = Flask(__name__)
cors = CORS(app)
SERVER_START_TIME = datetime.datetime.utcnow()

@app.before_first_request
def activate_job():
    def poll_youtube_videos():
        while True:
            print("[Youtube API] fetching new videos...")
            
            time.sleep(LONG_SLEEP)

    thread = threading.Thread(target=run_job)
    thread.start()

@app.route("/", methods=["GET"])
@cross_origin()
def root():
    istTime = str(SERVER_START_TIME + datetime.timedelta(hours=5.5)) + 'IST'
    CURRENT_TIME = datetime.datetime.utcnow()
    res =  Response(
        json.dumps({"uptime": str(CURRENT_TIME - SERVER_START_TIME), "started" : istTime}),
        status=200,
        mimetype='application/json'
    )
    return res

def start_runner():
    def start_loop():
        not_started = True
        while not_started:
            print('In start loop')
            try:
                r = requests.get(f"http://{HOST_URL}:{HOST_PORT}")
                if r.status_code == 200:
                    print('Server started, quiting start_loop')
                    not_started = False
                print(r.status_code)
            except:
                print('Server not yet started')
            time.sleep(SHORT_SLEEP)

    print('Started runner')
    thread = threading.Thread(target=start_loop)
    thread.start()


if( __name__ == "__main__"):
    start_runner()
    app.run(port=HOST_PORT, host=HOST_URL)