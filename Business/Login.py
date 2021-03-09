from Commonlib.commonlib import Commonshare
import time
class Login(Commonshare):
    def login(self,user,pwd):
        #测试首先要创建浏览器(已继承)，打开url
        self.open_url('http://localhost/iwebshop/')
        #定位到登录按钮并点击，点击之后进入登录界面
        self.click('css','.loginfo > a:nth-child(1)')
        #定位用户名并输入数据
        self.input_data('name','login_info',user)
        time.sleep(3)
        #定位并输入密码
        self.input_data('name','password',pwd)
        time.sleep(3)
        #点击登录
        self.click('class','submit_login')
        time.sleep(3)


if __name__ == '__main__':
            log =Login()
            log.login('烟雨d蓝','7315141')
