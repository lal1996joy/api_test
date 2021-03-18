import pytest

from request.read_excel import *
from request.test_ydy.ydy_test import *
from request.test_ydy.db_user import *


# 数据准备
# NEW_USER_MOBILE = '18842326682'
# OLD_USER_MOBILE = '18245284815'


class TestUserRegister:
    def setup_class(self):
        self.data_list = excel_to_list('test_user_data.xlsx', 'TestUserRegister')

    db = DBUSER()

    # 新用户注册成功
    def test_user_reg_normal(self):
        case_data = get_test_data(self.data_list, 'test_user_reg_normal')
        if not case_data:
            # print("用例数据不存在")
            logging.error("用例数据不存在")

        url = case_data.get('url')
        headers = json.loads(case_data.get('headers'))
        data = json.loads(case_data.get('data'))
        new_user_mobile = data.get('mobile')
        # print(new_user_mobile)
        logging.debug("手机号：{}".format(new_user_mobile))
        expect_res = case_data.get('expect_res')

        # 环境检查
        if self.db.query_user(new_user_mobile):
            self.db.del_user(new_user_mobile)

        # 发送请求
        res = requests.post(url=url, headers=headers, data=json.dumps(data), verify=False)

        # 响应断言
        assert res.json()['code'] == expect_res
        # print(f"注册成功：{res.reason}")
        logging.info("注册成功：{}".format(res.reason))

        # 数据库断言
        assert self.db.query_user(new_user_mobile) == True

        # 环境清理（由于注册接口向数据库写入了用户信息）
        self.db.del_user(new_user_mobile)

    # 老用户注册失败
    # @pytest.mark.skip(reason='我要跳过')
    def test_user_reg_exsit(self):
        case_data = get_test_data(self.data_list, 'test_user_reg_exsit')
        if not case_data:
            print("用例数据不存在")

        url = case_data.get('url')
        headers = json.loads(case_data.get('headers'))
        data = json.loads(case_data.get('data'))
        old_user_mobile = data.get('mobile')
        expect_res = case_data.get('expect_res')

        if self.db.query_user(old_user_mobile):
            res = requests.post(url=url, headers=headers, data=json.dumps(data), verify=False)
            assert res.json()['code'] == expect_res
            print(res.json()['msg'])
