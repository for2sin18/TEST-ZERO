import unittest
from Commonlib.HTMLTestRunner import HTMLTestRunner
from Testcase.testcase import Testcase

class Testsuit(unittest.TestCase):
    #创建测试套件
    def test_suit(self):

        mysuit = unittest.TestSuite()

        #向测试套件中添加测试用例
        case_list =['test_001','test_002','test_003','test_004']
        for case in case_list:
            mysuit.addTest(Testcase(case))



        with open ('../report.html','wb')as f :
              HTMLTestRunner(
                  stream=f,
                  title="",
                  description="",
                  verbosity=2

              ).run(mysuit)