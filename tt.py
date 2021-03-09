from selenium import webdriver
import time
class Common(object):
    #初始化
    def __init__(self):
        #创建浏览器
        self.driver=webdriver.Firefox()
        #浏览器最大化
        self.driver.maximize_window()

    def open_url(self,url):
            self.driver.get(url)
            self.driver.implicitly_wait(10)

    def close_url(self):
            self.driver.quit()

    #结束时清理
    def __del__(self):
        time.sleep(3)
        self.driver.quit()
#判断文件是否自身执行，如果是，则执行之后的语句！
if __name__ =='__main__':
   com = Common()
   com.open_url('http://www.baidu.com')
   com.open_url('http://www.163.com')
   com.close_url()