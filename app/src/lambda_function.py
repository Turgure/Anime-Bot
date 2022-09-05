import os
import sys
import tweepy

# tweepyをインストールしたディレクトリ相対パスを指定する
sys.path.append('python_package')

def lambda_handler(event, context):
    auth = tweepy.OAuthHandler(os.getenv('CONSUMER_KEY'), os.getenv('CONSUMER_SECRET'))
    auth.set_access_token(os.getenv('ACCESS_TOKEN'), os.getenv('ACCESS_TOKEN_SECRET'))

    api = tweepy.API(auth)

    api.update_status("test tweet")


lambda_handler(None, None)
#https://qiita.com/r_saiki/items/8ae6df4c808b74bd824e
