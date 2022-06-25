from flask import Flask, Response, request
from flask_cors import CORS, cross_origin

import threading
import requests
import datetime
import time
import json

from lib.config import (
    HOST_PORT,
    HOST_URL,
    SHORT_SLEEP,
    LONG_SLEEP,
    YOUTUBE_SERVICE_NAME,
    YOUTUBE_API_VERSION
)
from Service.youtube_service import YoutubeService 
from Service.database_service import DatabaseService

app = Flask(__name__)
cors = CORS(app)
SERVER_START_TIME = datetime.datetime.utcnow()

youtube_fetcher = YoutubeService(YOUTUBE_SERVICE_NAME, YOUTUBE_API_VERSION)
#initialize page token
page_token = None
#Save Videos is Bulk
bulk_save = False

database_fetcher = DatabaseService()

@app.before_first_request
def activate_job():
    def poll_youtube_videos():
        while True:
            print("[Youtube Service] fetching new videos...", flush=True)
            global page_token
            next_token = youtube_fetcher.fetch_latest_videos(
                page_token, bulk_save
            )
            
             # next_token is None when API limit exceeds
            if(next_token):
                page_token = next_token
            else:
                page_token = page_token
            time.sleep(LONG_SLEEP)

    thread = threading.Thread(target=poll_youtube_videos)
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

@app.route("/search", methods=["GET"])
@cross_origin
def search():
    query = request.args.get('query')
    page = int(request.args.get('page'))
    print("[Database Service] query: {",query,"}, page: {",page,"}", flush=True)
    return Response(
        json.dumps(DatabaseService.search_videos(query, page)),
        status=200,
        mimetype='application/json'
    )

def start_runner():
    #Loop for initializing Youtube Fetch without wait for First Query
    def start_loop():
        not_started = True
        while not_started:
            print('In start loop', flush=True)
            try:
                #Checking if Server started
                r = requests.get(f"http://{HOST_URL}:{HOST_PORT}")
                if r.status_code == 200:
                    print('Server started, quiting start_loop', flush=True)
                    not_started = False
                print(r.status_code, flush=True)
            except:
                print('Server not yet started', flush=True)
            time.sleep(SHORT_SLEEP)

    print('Started runner', flush=True)
    thread = threading.Thread(target=start_loop)
    thread.start()


if( __name__ == "__main__"):
    start_runner()
    app.run(port=HOST_PORT, host=HOST_URL)