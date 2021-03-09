import unittest
#集成TestCase类，testcase类是测试用例类
class Test1(unittest.TestCase):
    def setUp(self) -> None:
        print('hello')
    def tearDown(self) -> None:
        print('bye')

    def test_001(self):
        print('001')

    def test_002(self):
        print('002')

    def test_003(self):
        print('003')
if __name__ == '__main__':
    # unittest.main()
    #创建测试套件
    suit=unittest.TestSuite()
    #定义一个测试用例列表
    case_list=['test_001','test_002','test_003']
    for case in case_list:
        suit.addTest(Test1(case))
    #运行测试用例，verbosity=2为每个测试用例输出报告，run的参数是测试套件
    unittest.TextTestRunner(verbosity=2).run(suit)
#unittest.main()运行时，框架自动寻找TestCase子类并执行
#在TestCase类中，只把以test开头的方法当作测试用例然后执行
#setUp()用于初始化参数，在测试用例执行前自动被调用，tearDown用于清理，在测试用例被执行后调用
