#selenium 执行jS脚本
from selenium import webdriver
import time


class TestJS():

    def test_js_scroll(self):
        self.driver = webdriver.Chrome()
        print("测试1")
        self.driver.get('http://www.baidu.com')
        print("测试2")
        self.driver.find_element_by_id('kw').send_keys("selenium")
        print("测试3")
        el = self.driver.execute_script("return document.getElementById('su')")
        el.click()
        time.sleep(3)
        self.driver.execute_script("document.documentElement.scrollTop=1000 ")
        self.driver.find_element_by_xpath('//*[@id="hotsearch-content-wrapper"]/li[1]/a/span[2]').click()
        time.sleep(3)




