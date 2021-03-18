import requests
import json
from request.test_ydy.db_drugstore import DB
import urllib3

urllib3.disable_warnings()  # 忽略警告

global tip
tip = "https://test.edianyao.com/micro"
global headers
headers = {"Content-Type": "application/json;charset=UTF-8"}


# 快捷登录
def login():
    login_url = tip + "/hwauthcenteruser/centeruser/superlogin"
    data = {
        "username": "18245284815",
        "code": "191628",
        "loginType": "qlogin",
        "loginWhere": "edianyao",
        "province": "广东省",
        "city": "深圳市",
        "platform": "wxapp"
    }

    # res = requests.post(url=login_url, json=data, verify=False)

    data = json.dumps(data, ensure_ascii=False).encode("utf-8")
    res = requests.post(url=login_url, data=data,
                        headers={"Content-Type": "application/json;charset=UTF-8"},
                        verify=False)

    # jres = json.loads(res.text)
    jres = res.json()

    # token_type = jres.get('data').get('token_type')
    token_type = jres['data']['token_type']
    access_token = jres['data']['access_token']
    global token
    token = token_type + " " + access_token

    global headers
    headers = {
        "Content-Type": "application/json;charset=UTF-8",
        "Authorization": token
    }

    assert res.status_code == 200
    print("快捷登录成功")


# 平台购物车
def public_card():
    url = tip + "/ydyorderh5/publicCart/v2/user/list?adcode=440305&latitude=22.54073676215278&longitude=113.9413815646701&platform=ios"
    params = {
        "adcode": "440305",
        "latitude": "22.540648",
        "longitude": "113.941597",
        "platform": "wxapp"
    }

    res = requests.get(url=url, params=params, headers=headers, verify=False)
    assert res.reason == 0


# 门店上架药品列表（数据库查询）
def store_drug_list():
    # db.py
    # res = query_drug('S988', 1)

    # db_drugstore.py
    db = DB()
    res = db.query_drug('S988', 1)
    print(res)


# 药品添加到预约清单
def add_drug():
    url = tip + "/ydyorderh5/shopCart/v2/user/add"
    data = {
        "adcode": 440305,
        "storeId": 37120,
        "businessType": 1,
        "bn": "118067934",
        "type": "incre",
        "platform": "wxapp"
    }
    res = requests.post(url=url, headers=headers, json=data, verify=False)
    assert res.status_code == 200
    # print(res.text)
    print(res.status_code, res.reason)
    print(json.dumps(res.json(), indent=2, ensure_ascii=False))


# 订单
# 订单列表
def order_list():
    url = tip + "/ydyorderh5/qyworders/v1/lists"
    params = {
        "current": 1,
        "status": "all",
        "platform": "wxapp"
    }
    res = requests.get(url=url, params=params, headers=headers, verify=False)
    assert res.json()['code'] == 0

# if __name__ == '__main__':
#     login()
#     # public_card()
#     # order_list()
#     # store_drug_list()
#     add_drug()
