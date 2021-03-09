#多浏览器处理
from selenium import webdriver
import os


class Base():
    def setup(self):
        browser = os.getenv('browser')
        if browser == 'firefox':
            self.driver = webdriver.Firefox()
        elif browser == 'headless':
            self.driver = webdriver.PhantomJS()
        else:
            self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(1)
        self.driver.maximize_window()


    def teardown(self):
        self.driver.quit()


# if __name__ == '__main__':
#     base = Base()
#     base.setup("firefox")
#     base.driver.get("http://www.baidu.com")
#     base.driver.close()