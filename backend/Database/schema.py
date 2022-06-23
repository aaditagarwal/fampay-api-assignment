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
        self.id = id,
        self.title = title,
        self.description = description,
        self.published_at = published_at,
        self.thumbnail_default_res = thumbnail_default_res,
        self.thumbnail_high_res = thumbnail_high_res