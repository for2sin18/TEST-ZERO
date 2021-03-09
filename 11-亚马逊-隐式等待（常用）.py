from selenium import webdriver

driver=webdriver.Firefox()

url='https://www.amazon.cn/'
driver.get(url)
driver.implicitly_wait(20)
driver.close()