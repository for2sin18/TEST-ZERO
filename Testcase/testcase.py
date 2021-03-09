import unittest
from Business.Login import Login


class Testcase(unittest.TestCase):
    def setUp(self) -> None:
        print('start')
    def tearDown(self) -> None:
        print('end')
    #登录成功的情况
    def test_001(self):
        log = Login()
        log.login("烟雨d蓝","7315141")
        #获取用于断言的登陆后用户名
        data = log.get_text('class','f14')
        self.assertEqual('您好，烟雨d蓝 欢迎回来!',data)

    # 验证账号密码都不输入的测试用例
    def test_002(self):
        log = Login()
        log.login('', '')
        # 获取用于断言的登陆后用户名
        data = log.get_text('class', 'invalid-msg')
        self.assertEqual('填写用户名或邮箱', data)

    # 验证只输入账号的测试用例
    def test_003(self):
        log = Login()
        log.login('烟雨d蓝', '')
        # 获取用于断言的登陆后用户名
        data = log.get_text('class', 'invalid-msg')
        self.assertEqual('填写密码', data)

        # 验证只输入密码的测试用例
    def test_004(self):
            log = Login()
            log.login('', '7315141')
            # 获取用于断言的登陆后用户名
            data = log.get_text('class', 'valid-msg')
            self.assertEqual('验证通过', data)

if __name__ == '__main__':
    unittest.main()