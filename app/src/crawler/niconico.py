from datetime import datetime
import os
import re
import sys

from model.anime_data import AnimeData
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'lib'))
import requests
from bs4 import BeautifulSoup

class Niconico:
    @staticmethod
    def __get_content() -> BeautifulSoup:
        # ニコニコ一挙リストのURL
        url = 'https://anime.nicovideo.jp/live/reserved-ikkyo.html?from=live_watch_anime'
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')

        return soup

    @classmethod
    def create_data(cls) -> list[AnimeData]:
        conetnt = cls.__get_content()
        # <script id="tktk-module"> 以下のスクリプトタグを取得
        tag = conetnt.find('script', id='tktk-module')

        animeDatas = []
        # スクリプトの中身を1行ずつ調べる
        for line in tag.string.splitlines():
            # window.TKTK['live_reserved_ikkyo'] から始まるデータが一挙放送のリスト
            keyword = "window.TKTK['live_reserved_ikkyo']"
            if not line.startswith(keyword): continue

            # keywordの文字を消す
            titleList = line[line.index((keyword)) + len(keyword):]
            # []の中の文字列を取得
            titleList = titleList[titleList.find('{') + 1:titleList.rfind('}')]

            for data in titleList.split('},{'):
                print(data)

                contentId = re.search(r'contentId:s\("(.*?)"\)', data).group(1).strip()
                title = re.search(r'title:s\("(.*?)"\)', data).group(1).strip()
                startTime = re.search(r'startTime:d_s\(\'(.*?)\'\)', data).group(1).strip()
                watchUrl = re.search(r'watchUrl:s\("(.*?)"\)', data).group(1).strip()
                pictureUrl = re.search(r'pictureUrl:s\("(.*?)"\)', data).group(1).strip()

                print("\"", contentId, "\"", sep='')
                print("\"", title, "\"", sep='')
                print("\"", datetime.strptime(startTime, '%Y-%m-%dT%H:%M'), "\"", sep='')
                print("\"", watchUrl, "\"", sep='')
                print("\"", pictureUrl, "\"", sep='')
                print("---")

                animeDatas.append(AnimeData(contentId, title, datetime.strptime(startTime, '%Y-%m-%dT%H:%M'), watchUrl, pictureUrl))

        return animeDatas
