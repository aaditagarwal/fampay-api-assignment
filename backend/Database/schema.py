class DbSchema:
    #Schema for each fetched video

    def __init__(self):
        pass

    @staticmethod
    def create_schema_object(
        youtube_id,
        title,
        description,
        published_at,
        thumbnail_default_res,
        thumbnail_high_res
    ):
        schema_object = {
            "youtube_id": youtube_id,
            "title": title,
            "description": description,
            "published_at": published_at,
            "thumbnail": {
                "default_res": thumbnail_default_res,
                "high_res": thumbnail_high_res
            }
        }
        return schema_object