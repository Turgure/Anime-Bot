from datetime import datetime
from model.post_type import PostType

class AnimeData:
    def __init__(self, postType: PostType, id: str, title: str, startDateTime: datetime, watchUrl: str, pictureUrl: str):
        self.postType = postType
        self.id = id
        self.title = title
        self.startDateTime = startDateTime
        self.startDateTimeStr = datetime.strptime(startDateTime, '%Y-%m-%dT%H:%M')
        self.watchUrl = watchUrl
        self.pictureUrl = pictureUrl

    def to_dict(self) -> dict[str, str]:
        return {
            'PostType': self.postType.name,
            'ContentId': self.id,
            'Title': self.title,
            'StartDateTime': self.startDateTime,
            'WatchUrl': self.watchUrl,
            'PictureUrl': self.pictureUrl,
        }
