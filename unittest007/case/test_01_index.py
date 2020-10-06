import unittest       # 导入unittest
from selenium import webdriver         # 导入selenium
from utils.seleniumtools import find_element         # 导入动态查找

# @unittest.skip("都过了，就跳过吧")
# unittest 的测试用例是用类来管理的
class TestCaseIndex(unittest.TestCase):

    @classmethod   # 下边的这个方法是类方法,在类开始的时候执行一次
    def setUpClass(cls):       # cls 作用和self相同
        cls.driver = webdriver.Chrome(executable_path='driver/chromedriver.exe')
        cls.driver.maximize_window()

    # 在类结束的时候执行一次
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):    # 前置条件
        self.driver.get("http://118.24.255.132:9090/shopxo/")
        self.driver.delete_all_cookies()   # 获取到cookie之后登陆 
        cookies = {'domain': '118.24.255.132', 'httpOnly': True, 'name': 'PHPSESSID', 'path': '/', 'secure': False, 'value': '432qag80fhbt99dkq1k14llnf4'}
        self.driver.add_cookie(cookies)
        self.driver.refresh()

    def tearDown(self): # 后置条件
        print('这是TearDown方法')

    def test_01_baobao(self):
        baobao = ('xpath', '//*[@id="floor1"]/div[2]/div[2]/div[1]/div/div/a')
        bb = find_element(self.driver, baobao)
        assert bb.text == "MARNI Trunk 女士 中号拼色十字纹小牛皮 斜挎风琴包"

    def test_02_huaweishouji(self):
        huaweishouji = ('xpath', '//*[@id="floor1"]/div[2]/div[2]/div[5]/div/div/a')
        find_element(self.driver, huaweishouji).click()
        self.driver.switch_to_window(self.driver.window_handles[-1])
        assert self.driver.current_url == "http://118.24.255.132:9090/shopxo/index.php?s=/index/goods/index/id/4.html"

    def test_03_buy(self):
        huaweishouji = ('xpath', '//*[@id="floor1"]/div[2]/div[2]/div[5]/div/div/a')
        find_element(self.driver, huaweishouji).click()
        self.driver.switch_to_window(self.driver.window_handles[-1])
        buy = ('xpath', '/html/body/div[4]/div[2]/div[2]/div[3]/div[2]/div/button')
        find_element(self.driver, buy).click()

    def test_03_sousuo(self):
        sousuokuang = ('xpath', '//*[@id="search-input"]')
        find_element(self.driver, sousuokuang).send_keys('连衣裙')
        button = ('xpath', '//*[@id="ai-topsearch"]')
        find_element(self.driver, button).click()
        self.driver.switch_to_window(self.driver.window_handles[-1])
        assert self.driver.find_element_by_xpath('/html/body/div[4]/div/ul/li[1]/div/a/p').text == "ZK星星绣花雪纺连衣裙中长款sukol裙少女心温柔超仙女chic裙子夏"
        
    


"""
def setUp(self):        # 前置条件
        "Hook method for setting up the test fixture before exercising it."
        pass

    def tearDown(self):       # 后置条件
        "Hook method for deconstructing the test fixture after testing it."
        pass
"""

        



