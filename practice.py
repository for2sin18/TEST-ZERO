from selenium import webdriver
import time
class Commonshare(object):
    #初始化(创建浏览器+浏览器最大化)
    def __init__(self):
        #创建浏览器
        self.driver = webdriver.Firefox()

        #浏览器最大化
        self.driver.maximize_window()

    #打开url
    def open_url(self):
        url = 'http://www.baidu.com'
        self.driver.get(url)
    #关闭url
    def close_url(self):
        self.driver.quit()


    #元素定位方法
    def LocateElement(self,locate_type,value):
        el = None
        if locate_type =='id':
            el = self.driver.find_element_by_id(locate_type,value)
        elif locate_type == 'name':
            el = self.driver.find_element_by_name(locate_type,value)
        elif locate_type =='class':
            el = self.driver.find_element_by_class_name(locate_type,value)
        elif locate_type == 'tag':
            el = self.driver.find_element_by_tag_name(locate_type,value)
        elif locate_type =='css':
            el = self.driver.find_element_by_css_selector(locate_type,value)
        elif locate_type =='xpath':
            el = self.driver.find_element_by_xpath(locate_type,value)
        elif locate_type =='partial':
            el = self.driver.find_element_by_partial_link_text(locate_type,value)
        elif locate_type =='text':
            el = self.driver.find_element_by_link_text(locate_type,value)

        if el is not None:
            return el

    #点击封装
    def click(self,locate_type,value):
        #调用locateElement先定位元素
         el = self.LocateElement(locate_type,value)
        #调用click
         el.click()

    #直接对定位的元素文本输出
    def input_data(self,locate_type,value,data):
        el = self.LocateElement(locate_type,value)
        el.send_keys(data)

    #获取定位到的参数的文本内容
    def get_text(self,locate_type,value):
        el = self.LocateElement(locate_type,value)
        return el.text

    #获取定位到的元素标签属性
    def get_attr(self,locate_type,value,data):
        el = self.LocateElement(locate_type,value)
        return el.get_attribute(data)


    #结束时清理
    def __del__(self):
        time.sleep(5)
        self.driver.quit()


