import json
import sys
# tweepyをインストールしたディレクトリ相対パスを指定する
sys.path.append('lib')
import tweepy

# https://qiita.com/r_saiki/items/8ae6df4c808b74bd824e
# https://qiita.com/charon/items/19ab5087f7036dafce4b
def lambda_handler(event, context):
    # 設定ファイル読み込み
    config = json.load(open('config.json', 'r'))

    auth = tweepy.OAuthHandler(config['consumer_key'], config['consumer_secret'])
    auth.set_access_token(config['access_token'], config['access_token_secret'])
    api = tweepy.API(auth)

    api.update_status("test tweet")
