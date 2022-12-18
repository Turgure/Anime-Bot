from model.anime_data import AnimeData
from model.dynamodb import DynamoDB

def write_items(animeDatas: list[AnimeData]) -> None:
    DynamoDB.get_instance().write_items(map(lambda x: x.to_dict(), animeDatas))

def get_all_items() -> None:
    DynamoDB.get_instance().get_all_items()

