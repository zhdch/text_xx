# 整个工具的入口：都是固定的

import unittest
from utils.HTMLTestRunner import HTMLTestRunner

# 1.自动查找所有的测试用例
testcase = unittest.defaultTestLoader.discover('case','test_*.py')

# 2.使用htmltestrunner工具来帮我们自动运行所有的case和生成测试报告
title = "这是第一次web框架测试"
descr = "unttest的测试报告"

filepath = "./report/report.html"
with open(filepath, 'wb') as f:
    runner = HTMLTestRunner(stream=f, title=title, description=descr)
    runner.run(testcase)