from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

driver=webdriver.Chrome()
url='http://www.baidu.com'
driver.get(url)

el=WebDriverWait(driver,10,0.5).until(EC.presence_of_element_located((By.ID,'lg')))
driver.close()