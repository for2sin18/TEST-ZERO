from selenium import webdriver
import time

driver=webdriver.Firefox()

url='http://www.baidu.com'
driver.get(url)

#定位搜索设置
driver.maximize_window()
el_1=driver.find_element_by_id('s-usersetting-top')
el_1.click()
time.sleep(1)
el_2=driver.find_element_by_css_selector('.setpref')
el_2.click()
time.sleep(1)
el_3=driver.find_element_by_class_name('prefpanelgo')
el_3.click()
time.sleep(1)
driver.switch_to.alert.accept()
