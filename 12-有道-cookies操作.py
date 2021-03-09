from selenium import webdriver

driver=webdriver.Firefox()

url = 'http://www.youdao.com/'
driver.get(url)
data = driver.get_cookies()
print(data)
#删除cookies
driver.delete_all_cookies()
#设置cookies
cookie={"name":"itcast","value":"soft_test"}
driver.add_cookie(cookie)
#获取
data1 = driver.get_cookies()
print(data1)
