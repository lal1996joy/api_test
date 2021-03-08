#! /usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json
from request.read_excel import *
from request.test_ydy.case_log import log_case_info
from request.test_ydy.ydy_test import tip

from config import *

# 屏蔽建立连接日志
# logging.getLogger("requests").setLevel(logging.ERROR)


class TestUserLogin:

    def setup_class(self):
        self.data_list = excel_to_list("test_user_data.xlsx", "TestUserLogin")

    # 验证码登录成功
    def test_qlogin_normal(self):
        case_data = get_test_data(self.data_list, "test_qlogin_normal")
        if not case_data:  # 有可能为None
            logging.error("用例数据不存在")

        url = case_data.get('url')
        data = json.loads(case_data.get('data'))
        expect_res = case_data.get('expect_res')

        res = requests.post(url=url, json=data, verify=False)
        assert res.json()['code'] == expect_res
        # print(f"验证码登录成功： {res.reason}")
        logging.info("验证码登录成功：{}".format(res.reason))


        # res_text = res.text.encode()      # 需要编码
        res_text = json.dumps(res.json(), indent=2)
        log_case_info('test_user_login_normal', url, data, expect_res, res_text)    # 输出用例log信息

    # 验证码错误，登录失败
    def test_qlogin_wrong(self):
        case_data = get_test_data(self.data_list, 'test_qlogin_wrong')
        if not case_data:  # 有可能为None
            logging.error("用例数据不存在")

        url = case_data.get('url')
        headers = json.loads(case_data.get('headers'))
        data = json.loads(case_data.get('data'))
        data = json.dumps(data, ensure_ascii=False).encode("utf-8")
        expect_res = case_data.get('expect_res')

        res = requests.post(url=url, data=data, headers=headers, verify=False)
        jres = res.json()
        assert jres['code'] == expect_res
        print(f"验证码登录失败： {jres['msg']}")

    # 密码登录成功
    def test_pwd_login_normal(self):
        case_data = get_test_data(self.data_list, 'test_pwd_login_normal')

        url = case_data.get('url')
        data = case_data.get('data')
        expect_res = case_data.get('expect_res')

        res = requests.post(url=url, json=json.loads(data), verify=False)
        assert res.json()['code'] == expect_res
        print(f"密码登录成功： {res.reason}")

    # 密码登录失败
    def test_pwd_login_wrong(self):
        case_data = get_test_data(self.data_list, 'test_pwd_login_wrong')

        url = case_data.get('url')
        data = case_data.get('data')
        expect_res = case_data.get('expect_res')

        res = requests.post(url=url, json=json.loads(data), verify=False)
        jres = res.json()
        assert jres['code'] == expect_res
        print(f"密码登录失败： {jres['msg']}")
