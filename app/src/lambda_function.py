from crawler.niconico import Niconico
from tweet import tweet

def lambda_handler(event, context):
    tweet(Niconico.create_data())
