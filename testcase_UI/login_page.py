from selenium import webdriver

from testcase_UI.base_page import Action


class LoginPage(Action):

    def setup_class(self):
        # 打开浏览器
        webdriver.Chrome()
        # 打开网页
        self.open('https://www.pyy365.cn/edyLS/dist/adminlogin')

    # 定位用户名输入框
    def get_name_element(self):
        name = '''//*[@id="app"]/div/div[1]/div[2]/div/input'''  # 用户名
        return self.find_element(name)

    # 定位密码输入框
    def get_pwd_element(self):
        pwd = '''//*[@id="app"]/div/div[1]/div[3]/div/input'''  # 密码
        return self.find_element(pwd)

    # 定位登录按钮
    def get_loginbutton_element(self):
        return self.find_element('loginBtn')
