from Database.queries import search_videos

class DatabaseService:
    def __init__(self):
        pass

    @staticmethod
    def search_videos_db(query, page):
        results = search_videos(query, page)
        
        service_response = []
        for video in results:
            service_response.append(video)
        
        return service_response