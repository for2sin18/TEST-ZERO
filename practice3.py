import unittest
from Business.Login import Login
class Testcase(unittest.TestCase):
    def setUp(self) -> None:
        pass
    def tearDown(self) -> None:
        pass
    #下面开始写测试用例
    #用户名和密码都正确的测试用例
    def test_001(self):
        log = Login()
        log.login('user','pwd')
    #只输入用户名的情况，并断言一下是否有错误提示
    def test_002(self):
        log = Login()
        log.login('user','')
        #获取断言后的错误提示信息
        data = log.get_text('','')
        self.assertEqual("要比较值",data)