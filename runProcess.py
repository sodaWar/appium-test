# -*encoding:utf-8 *-
import unittest
from auto_login import AutoTest
from HTMLTestRunner import HTMLTestRunner

if __name__ == "__main__":
    suite = unittest.TestSuite()

    tests = [AutoTest("test_teach"),AutoTest("test_tearDown"),AutoTest("test_skipFunction")]
    suite.addTests(tests)
    #
    # with open('UnittestTextReport.txt', 'a') as f:   #将结果输出到文件中，其中'r'读模式、'w'写模式、'a'追加模式、'b'二进制模式、'+'读/写模式。
    #     runner = unittest.TextTestRunner(stream=f,verbosity=2)
    #     runner.run(suite)


    with open('HTMLReport.html', 'w') as f:    #将结果输出到HTML网页报告中
        runner = HTMLTestRunner(stream=f,title="auto test sokafootball  case report",
                                description="generated by HTMLTestRunner",verbosity=2)
        runner.run(suite)

