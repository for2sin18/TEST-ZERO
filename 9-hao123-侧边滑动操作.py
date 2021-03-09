from selenium import webdriver
import time
#
driver=webdriver.Firefox()

url='https://www.hao123.com/'
driver.get(url)
#(x,y)坐标系
js='window.scrollTo(0,1000)'
driver.execute_script(js)
time.sleep(3)
#value值代表从顶部往下移动多少位置
js1="var q=document.documentElement.scrollTop=0"
driver.execute_script(js1)