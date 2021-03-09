from selenium import webdriver
import os


driver=webdriver.Firefox()

#获取浏览器访问路径
file_path='file:///' +os.path.abspath('example_frame.html')
print(file_path)

#访问本地文件
driver.get(file_path)

#切换到第一个表单中
driver.switch_to.frame('itcast_frame1')

#切换到第二层表单中
driver.switch_to.frame('itcast_frame2')



#定位输入框
el = driver.find_element_by_id('sb_form_q')
el.send_keys('selenium')
el_sub=driver.find_element_by_id('sb_form_go')
el_sub.click()

#定位一个元素，验证已经到达深层表单
el_search=driver.find_element_by_id('sb_form')
print('依然在最深层表单中')
driver.switch_to.default_content()
try:
    el_search = driver.find_element_by_id('sb_form')
except:
    print('已经从表单中退出')