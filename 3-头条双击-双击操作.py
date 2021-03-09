from selenium.webdriver import ActionChains
from selenium import webdriver
import time

#创建浏览器对象
driver=webdriver.Firefox()
#访问头条
url = 'https://www.toutiao.com/'
driver.get(url)
#定位到需要双击操作的元素
el=driver.find_element_by_css_selector('.logo > img:nth-child(1)')
#双击定位元素
ActionChains(driver).double_click(el).perform()
time.sleep(3)
driver.quit()