from selenium import webdriver
#下拉框选择使用selenium下的webdriver的support下的select包中的Select类
from selenium.webdriver.support.select import Select
import time

driver=webdriver.Firefox()

url='http://tieba.baidu.com/f/index/forumclass'
driver.get(url)
driver.maximize_window()
#定位高级搜索
el_1=driver.find_element_by_class_name('senior-search-link')
el_1.click()
time.sleep(1)
#定位下拉框元素
el=driver.find_element_by_name('rn')
#创建下拉框对象
selobj=Select(el)
selobj.select_by_value('20')
time.sleep(3)
selobj.select_by_value('30')