import datetime
from urllib import response
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from lib.api_key import (
    get_api_key,
    generate_new_api_key
)
from lib.config import (
    PUBLISHED_AFTER_TIME,
    QUERY
)

class YoutubeService:
    def __init__(self, service_name, api_version):
        self.service_name = service_name
        self.api_version = api_version
        self.api_key = get_api_key()
        self.published_after = datetime.datetime.strftime(
            datetime.datetime.now()-datetime.timedelta(seconds=PUBLISHED_AFTER_TIME),
            "%Y-%m-%dT%H:%M:%SZ"
        )
        self.youtube_object = self.build_youtube_object()

    def build_youtube_object(self):
        return build(
            self.service_name, self.api_version, developer_key=self.api_key
        )

    def update_api_key(self):
        self.api_key = generate_new_api_key()
        print("[Youtube Service] Updated API Key...")

    def fetch_latest_videos(self, page_token):
        try:
            api_response = (
                self.youtube_object.search()
                .list(
                    q=QUERY,
                    part="id,snippet",
                    order="date",
                    publishedAfter=self.published_after,
                    type="video",
                    pageToken=page_token
                )
                .execute()
            )
        except Exception as e:
            print(f"[Youtube Service] Error: {e}")
            #Youtube API limit reached
            if(
                isinstance(e, HttpError) and
                "exceeded" in e._get_reason()
                or isinstance(e, OverflowError)
            ):
                self.update_api_key()
                self.youtube_object = self.build_youtube_object()
            else:
                print(f"[Youtube Service] Uncaught Exception: {e}")
            return [], None

        results = []
        for item in api_response.get('items', []):
            #Iterating Videos
            if item["id"]["kind"] == "youtube#video":
                published_date = datetime.datetime.strptime(
                    item["snippet"]["publishedAt"],
                    "%Y-%m-%dT%H:%M:%SZ",
                ).strftime("%Y-%m-%d %H:%M:%S")

        next_page_token = response.get("nextPageToken", None)
        return results, next_page_token