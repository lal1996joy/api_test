from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = 'https://www.pyy365.cn/edyLS/dist/adminlogin'
# 打开浏览器
browser = webdriver.Chrome()
browser.implicitly_wait(5)
# 打开网页
browser.get(url)
# browser.maximize_window()
# 当前网页标题
print(browser.title)
# 当前url
print(browser.current_url)
# print(browser.page_source)


# browser.find_element_by_class_name('testLink').click()
# sleep(2)
# 后退
# browser.back()
# 前进
# browser.forward()
# 刷新
# browser.refresh()

# 登录
# class相同的一组元素用elements索引
cn = browser.find_elements_by_class_name('el-input__inner')
cn[0].send_keys('admin')  # 用户名
cn[1].send_keys('1q2w3eadmin')  # 密码

browser.find_element_by_class_name('loginBtn').click()

# 订单管理
area = browser.find_elements_by_xpath(
    '//div[@class="el-submenu__title"] //i[@class="el-submenu__icon-arrow el-icon-arrow-down"]')
# 订单管理—预约订单
area[0].click()

# 订单管理—快递配送订单
# browser.find_element_by_xpath('''//ul[@class="el-menu el-menu--inline"]//*[contains(text(),'快递配送订单')]''').click()
browser.find_element_by_xpath('//*[@id="app"]/div/section/aside/div/div[2]/ul/div[2]/li/ul/li[2]/ul/li').click()



# 订单管理—本地快送订单
# browser.find_element_by_xpath('''//ul[@class="el-menu el-menu--inline"]//*[contains(text(),'本地快送订单')]''').click()


# 用户回访
# browser.find_element_by_class_name('el-icon-user-solid').click()

# 药品管理
# area[1].click()

# 关闭当前页面
# browser.close()

# 退出浏览器
# browser.quit()
