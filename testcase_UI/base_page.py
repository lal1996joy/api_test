'''
这个类主要是完成所有页面的一些公共方法的封装
'''

from selenium.webdriver.support.wait import WebDriverWait


class Action(object):
    # 初始化
    def setup_class(self, se_driver):
        self.driver = se_driver

    # 打开浏览器，窗口最大化
    def open(self, url):
        self.driver.get(url)
        self.driver.maximize_window()

    # 定位元素
    def find_element(self, *loc):
        try:
            WebDriverWait(self.driver, 20).until(lambda driver: driver.find_element(*loc).is_displayed())
            return self.driver.find_element(*loc)
        except Exception as e:
            print("未找到%s" % (self, loc))

    # 执行js脚本
    def script(self, js):
        self.driver.execute_script(js)

    # 输入send_keys()
    def send_keys(self, loc, value, clear_first=True, clik_first=True):
        try:
            if clik_first:
                self.find_element(*loc).click()
            if clear_first:
                self.find_element(*loc).clear()
                self.find_element(*loc).send_keys(value)
        except AttributeError:
            print("未找到%s" % (self, loc))
