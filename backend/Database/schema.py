class DbSchema:
    #Schema for each fetched video

    def __init__(
        self,
        id,
        title,
        description,
        published_at,
        thumbnail_default_res,
        thumbnail_high_res
    ):
        schema_object = {
            "id": id,
            "title": title,
            "description": description,
            "published_at": published_at,
            "thumbnail": {
                "default_res": thumbnail_default_res,
                "high_res": thumbnail_high_res
            }
        }
        return schema_object