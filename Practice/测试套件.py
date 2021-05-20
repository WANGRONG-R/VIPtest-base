#coding:utf-8

import my_module1

from Pra_unittest.跳过和verbosity的学习 import TestMyFun

if __name__ == '__main__':
    suite = my_module1.TestSuite()

    tests = [TestMyFun("test_add"), TestMyFun("test_minus"), TestMyFun("test_divide")]   # 添加测试用例列表
    suite.addTests(tests)   # 将测试用例列表添加到测试组中
    suite.addTest(TestMyFun("test_multi"))  # 直接用addTest方法添加单个TestCase
    # 用addTests + TestLoader。不过用TestLoader的方法是无法对case进行排序的
    # loadTestsFromName()，传入'模块名.TestCase名'
    suite.addTests(my_module1.TestLoader().loadTestsFromName('test_myfun.TestMyFun'))
    suite.addTests(my_module1.TestLoader().loadTestsFromNames(['test_myfun.TestMyFun']))  # loadTestsFromNames()，类似，传入列表

    # loadTestsFromTestCase()，传入TestCase
    suite.addTests(my_module1.TestLoader().loadTestsFromTestCase(TestMyFun))

    # suite中也可以套suite

    # 将测试结果输出到测试报告中
    # with open('UnittestTextReport.txt', 'a') as f:
    #     runner = unittest.TextTestRunner(stream=f, verbosity=2)
    #     runner.run(suite)

    # 将测试结果输出到测试报告html中
    # with open('HTMLReport.html', 'w') as f:
    #     runner = HTMLTestRunner(stream=f,
    #                             title='MathFunc Test Report',
    #                             description='generated by HTMLTestRunner.',
    #                             verbosity=2
    #                             )
    #     runner.run(suite)

    # 直接将结果输出到控制台
    runner = my_module1.TextTestRunner(verbosity=2)
    runner.run(suite)
