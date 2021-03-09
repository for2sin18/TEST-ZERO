from selenium import webdriver
from selenium.webdriver import ActionChains
import time

driver=webdriver.Firefox()

url='https://www.baidu.com'
driver.get(url)
el = driver.find_element_by_css_selector('#lg > map:nth-child(3) > area:nth-child(1)')
ActionChains(driver).context_click(el).perform()
time.sleep(2)
driver.close()