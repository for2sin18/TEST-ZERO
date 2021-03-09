from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Firefox()

url='http://cn.bing.com/'
driver.get(url)

#定位到输入框
el=driver.find_element_by_id('sb_form_q')
el.send_keys('selenium')
time.sleep(1)
#执行剪切操作
el.send_keys(Keys.CONTROL,'a')
time.sleep(1)
el.send_keys(Keys.CONTROL,'x')
time.sleep(1)
#执行粘贴操作
el.send_keys(Keys.CONTROL,'v')
time.sleep(1)
el.clear()
el.send_keys('seleniumn')
time.sleep(1)
el.send_keys(Keys.BACK_SPACE)
time.sleep(5)
driver.quit()