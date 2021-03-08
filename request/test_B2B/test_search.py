import json

import requests

from request.test_ydy.ydy_test import tip, headers

KEYWORD = "络活喜"


class TestSearch:
    url = tip + "/b2bmalldrugstore/qywpurchasedrugs/suggest"
    hearder = headers

    # 联想词
    def test_suggest(self):
        url = self.url
        params = {
            "key": KEYWORD
        }
        res = requests.get(url=url, params=params, headers=headers, verify=False)
        print(json.dumps(res.json(), indent=2, ensure_ascii=False))
        global keyword
        keyword = res.json()['data'][0]
        print(f"关键词: {keyword}")

    # 联想词搜索
    def test_search_by_suggest(self):
        url = tip + "/b2bmalldrugstore/qywpurchasedrugs/search"

        data = {
            "current": 1,
            "keyword": keyword,
            "platform": "wxapp",
            "searchType": 0,
            "size": 20,
            "sortType": 2,
            "tag": ""
        }
        res = requests.post(url=url, headers=headers, data=json.dumps(data), verify=False)
        print(json.dumps(res.json(), indent=2, ensure_ascii=False))
