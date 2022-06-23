import os

#Hosted URL
HOST_PORT = "8080"
HOST_URL = "0.0.0.0"

#Time before starting server
SHORT_SLEEP = 2,

#Polling Interval
LONG_SLEEP = 10

#Published After Time for latest Videos
PUBLISHED_AFTER_TIME = 1209600 #2 weeks in seconds

#Youtube API Keys
API_KEYS = os.getenv("GOOGLE_API_KEYS").split(',')

#PreDefined Query
QUERY = 'football'