from selenium import webdriver
from selenium.webdriver import ActionChains
import time


driver=webdriver.Firefox()

url='https://www.vip.com/?wxsdk=1'
driver.get(url)
driver.maximize_window()
time.sleep(5)
el_list = driver.find_elements_by_css_selector('ul[id="J_main_nav_link"]>li')
print(el_list)
for el in el_list:
 ActionChains(driver).move_to_element(el).perform()
 time.sleep(1)
