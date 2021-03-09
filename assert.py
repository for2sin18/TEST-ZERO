import unittest

#自己创建的测试用例类继承自unittest.Test类
class  Test(unittest.TestCase):
    def setUp(self):
        print("start")

    def tearDown(self):
         print("end")
    #判断预期值和实际值是否相等
    def test_001(self):
        self.assertEqual('1','1')

     #判断预期值和实际值是否相等
    def test_002(self):
        self.assertEqual('1','2')


if __name__ == '__main__':
    unittest.main()
