from __future__ import absolute_import
import json
from . import token
import requests


def searchCode(query, index = 1):
    HEADERS = {'Host': 'xueqiu.com',
               'Accept': 'application/json',
               'Cookie': token.get_token(),
               'User-Agent': 'Xueqiu iPhone 11.8',
               'Accept-Language': 'zh-Hans-CN;q=1, ja-JP;q=0.9',
               'Accept-Encoding': 'br, gzip, deflate',
               'Connection': 'keep-alive'}
    url = "https://xueqiu.com/stock/search.json?code={}&size={}".format(query, index)
    return json.loads(requests.get(url,headers=HEADERS).text)

