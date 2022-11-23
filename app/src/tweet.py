import json
import sys
from model.anime_data import AnimeData

sys.path.append('lib')
import tweepy

# https://qiita.com/r_saiki/items/8ae6df4c808b74bd824e
# https://qiita.com/charon/items/19ab5087f7036dafce4b
def tweet(animeDatas: list[AnimeData]) -> None:
    # 設定ファイル読み込み
    config = json.load(open('config.json', 'r'))

    auth = tweepy.OAuthHandler(config['consumer_key'], config['consumer_secret'])
    auth.set_access_token(config['access_token'], config['access_token_secret'])
    api = tweepy.API(auth)

    contents = []
    content = ''
    for data in animeDatas:
        line = '{}: {} / {} / {}\n'.format(data.id, data.title, data.startDateTime, data.watchUrl)
        # twitter文字数制限を超えたら分ける
        if (len(content + line) >= 280):
            contents.append(content)
            content = ''
        else:
            content += line
    contents.append(content)

    print('----- tweet message -----')
    for i, c in enumerate(contents):
        print(i)
        print(c)


    for c in contents:
        api.update_status(c)
