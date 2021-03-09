from selenium import webdriver
from selenium.webdriver import ActionChains
import time


driver=webdriver.Firefox()

url='https://www.jd.com'
driver.get(url)
driver.maximize_window()
time.sleep(5)
el_list = driver.find_elements_by_class_name('cate_menu_item')
for el in el_list:
 ActionChains(driver).move_to_element(el).perform()
 time.sleep(1)
