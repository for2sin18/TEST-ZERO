from Commonlib.commonlib import Commonshare
import time
class Login(Commonshare):
    def login(self,user,pwd):
        #打开url,创建浏览器已经在Commonshare中初始化过了
        self.open_url('http://www.baidu.com')
        #点击登录按钮
        self.click('','')
        #进入登录界面后，分别定位用户框和密码框并输入
        self.input_data('locate_type','value',user)
        time.sleep(3)
        self.input_data('locate_type','value',pwd)
        #点击登录按钮
        self.click('locate_type','value')
        time.sleep(3)



