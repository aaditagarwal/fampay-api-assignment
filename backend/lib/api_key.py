from lib.config import API_KEYS

#API KEY Index
api_key_idx = 0

#Retrive API KEY
def get_api_key():
    return API_KEYS[api_key_idx]

def generate_new_api_key():
    global api_key_idx
    api_key_idx = (api_key_idx+1)%(len(API_KEYS))
    return API_KEYS[api_key_idx]