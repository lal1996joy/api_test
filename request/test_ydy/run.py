import pytest
#
# from request.test_ydy.test_login import TestUserLogin
#
# if __name__ == '__main__':
#     # 登录
#     pytest.main(['-s', 'test_login.py', '--alluredir=report/allure'])
    #
    # 注册
    # pytest.main(['-s', 'test_register.py', '--alluredir=report/allure'])
    # 老用户注册
    # pytest.main(['-s', '-m', 'tag01'])

    # pytest.main(['-s', 'test_ydy',
    #              '--html=report/test.html',
    #              '--alluredir=report/allure'])


    # pytest.main(['-s', 'test_B2B/test_search.py'])
    # tul = TestUserLogin()
    # tul.test_qlogin_normal()


import unittest
# from HTMLTestReportCN import HTMLTestRunner
from config import *
from send_email import send_email

logging.info("====================== 测试开始 =======================")
# suite = unittest.defaultTestLoader.discover("./")

with open("report.html", 'wb') as f:  # 改为with open 格式
    # HTMLTestRunner(stream=f, title="Api Test", description="测试描述", tester="卡卡").run(suite)

    pytest.main(['-s', 'test_login.py', '--alluredir=report/allure'])

send_email('report.html')  # 发送邮件
logging.info("======================= 测试结束 =======================")
