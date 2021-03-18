from time import sleep

from HtmlTestRunner import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = 'https://www.pyy365.cn/edyLS/dist/adminlogin'
# 打开浏览器
driver = webdriver.Chrome()
driver.implicitly_wait(5)
# 打开网页
driver.get(url)
driver.maximize_window()
# 当前网页标题
print(driver.title)
# 当前url
print(driver.current_url)
# print(driver.page_source)


# driver.find_element_by_class_name('testLink').click()
# sleep(2)
# 后退
# driver.back()
# 前进
# driver.forward()
# 刷新
# driver.refresh()

# 点击显示颜色
def style(xpath):
    js = "arguments[0].setAttribute('style', arguments[1]);"
    element = driver.find_element_by_xpath(xpath)
    style = "background: red; border: 2px solid yellow;"
    driver.execute_script(js, element, style)


# 登录
# class相同的一组元素用elements索引
cn = driver.find_elements_by_class_name('el-input__inner')
cn[0].send_keys('admin')  # 用户名
cn[1].send_keys('1q2w3eadmin')  # 密码

driver.find_element_by_class_name('loginBtn').click()

# 订单管理
area = driver.find_elements_by_xpath(
    '//div[@class="el-submenu__title"] //i[@class="el-submenu__icon-arrow el-icon-arrow-down"]')
# 订单管理—预约订单
area[0].click()

# 订单管理—快递配送订单
# driver.find_element_by_xpath('''//ul[@class="el-menu el-menu--inline"]//*[contains(text(),'快递配送订单')]''').click()
driver.find_element_by_xpath('//*[@id="app"]/div/section/aside/div/div[2]/ul/div[2]/li/ul/li[2]/ul/li').click()

# 右击
right_click = driver.find_element_by_xpath('//*[@id="app"]/div/section/aside/div/div[2]/ul/div[2]/li/ul/li[2]/ul/li')
ActionChains(driver).context_click(right_click).perform()



# js = "document.getElementsByClassName('el-range-input')[0].click()"
# driver.execute_script(js)
#
# js = "document.getElementsByClassName('el-range-input')[1].value='2021-03-10 23:59:59'"
# driver.execute_script(js)

area = driver.find_elements_by_xpath("//input[@class='el-range-input']")
area[0].send_keys('2021-03-01 23:59:59')
area[1].send_keys('2021-03-11 23:59:59')

js = "document.getElementsByClassName('el-button el-picker-panel__link-btn el-button--default el-button--mini is-disabled is-plain')[0].click()"
driver.execute_script(js)
sleep(5)
xpath = "//div[@class='table-body']//tbody"
if driver.find_element_by_xpath(xpath) != '':
    driver.find_element_by_xpath("//button[@class='el-button el-button--primary']").click()
style("//button[@class='el-button el-button--primary']")


HTMLTestRunner

# 订单管理—本地快送订单
# driver.find_element_by_xpath('''//ul[@class="el-menu el-menu--inline"]//*[contains(text(),'本地快送订单')]''').click()


# 用户回访
# driver.find_element_by_class_name('el-icon-user-solid').click()

# 药品管理
# area[1].click()

# 关闭当前页面
# driver.close()

# 退出浏览器
# driver.quit()
