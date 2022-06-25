import os
from dotenv import load_dotenv

load_dotenv()

#Hosted URL
HOST_PORT = "8080"
HOST_URL = "0.0.0.0"

#Time before starting server
SHORT_SLEEP = 2

#Polling Interval
LONG_SLEEP = 10

#Published After Time for latest Videos
PUBLISHED_AFTER_TIME = 1209600 #2 weeks in seconds

#Youtube API Keys
API_KEYS = os.getenv("GOOGLE_API_KEYS").split(",")
#Youtube Object
YOUTUBE_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

#PreDefined Query
QUERY = 'football'

#MongoDB Database
MONGODB_URI = "mongodb://mongo:27017/fampay_api_db"
MONGODB_DATABASE = "fampay_api_db"
MONGODB_COLLECTION = "fampay_api_colelction"


#Pagination
PAGINATION_LIMIT  = 10