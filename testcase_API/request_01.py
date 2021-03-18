import requests
import json
# from requests.packages.urllib3.exceptions import InsecureRequestWarning
#
# # 关闭安全请求警告
# requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
import urllib3

urllib3.disable_warnings()  # 忽略警告

# get请求
# url = "https://test.edianyao.com/micro/ydymkth5/qywtab/tabList?platform=wxapp"
# res = requests.get(url=url, verify=False)

getUrl = "https://test.edianyao.com/micro/ydymkth5/qywtab/tabList"
params = {"platform": "wxapp"}
getRes = requests.get(url=getUrl, params=params, verify=False)

print(getRes.text)


# post请求
postUrl = "https://test.edianyao.com/micro/ydymkth5/qywbanner/V2/lists"


# data = '{"type": 1,"platform": "wxapp"}'
# headers = {"Content-Type": "application/json"}
# postRes = requests.post(url=postUrl, headers=headers, data=data, verify=False)


# 多行文本, 字符串格式，也可以单行（注意外层有引号，为字符串）
# data = '''{
#     "type": 1,
#     "platform": "wxapp"
# }'''
# headers = {"Content-Type": "application/json"}
# postRes = requests.post(url=postUrl, headers=headers, data=data, verify=False)#  data支持字典或字符串


# 将data声明为字典格式（方便数据添加修改），然后再用json.dumps()方法把data转换为合法的JSON字符串格式
# data = {
#     "type": 1,
#     "platform": "wxapp"
# }
# headers = {"Content-Type": "application/json"}
#  将字典格式的data变量转换为合法的JSON字符串传给post的data参数
# postRes = requests.post(url=postUrl, headers=headers, data=json.dumps(data), verify=False)


# 直接将字典格式的data数据赋给post方法的JSON参数（会自动将字典格式转为合法的JSON文本并添加headers）
data = {
    "type": 1,
    "platform": "wxapp"
}
# JSON格式的请求，将数据赋给json参数
postRes = requests.post(url=postUrl, json=data, verify=False)

print(postRes.text)


