import unittest       # 导入unittest
from selenium import webdriver         # 导入selenium
from utils.seleniumtools import find_element         # 导入动态查找

# unittest 的测试用例是用类来管理的
class TestCaseIndex(unittest.TestCase):
    def test_01_baobao(self):
        driver = webdriver.Chrome(executable_path='driver/chromedriver')
        driver.maximize_window()
        driver.get("http://118.24.255.132:9090/shopxo/")
        baobao = ('xpath', '//*[@id="floor1"]/div[2]/div[2]/div[1]/div/div/a')
        bb = find_element(driver, baobao)
        assert bb.text == "MARNI Trunk 女士 中号拼色十字纹小牛皮 斜挎风琴包"
"""
def setUp(self):        # 前置条件
        "Hook method for setting up the test fixture before exercising it."
        pass

    def tearDown(self):       # 后置条件
        "Hook method for deconstructing the test fixture after testing it."
        pass
"""

        



