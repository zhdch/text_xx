import unittest       # 导入unittest
from selenium import webdriver         # 导入selenium
from utils.seleniumtools import find_element         # 导入动态查找
from po.AdminLoginPage import AdminLoginPage      # 导入封装的 po

@unittest.skip("先跳过")
class TestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='driver/chromedriver.exe')
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        self.driver.get('http://118.24.255.132:9090/shopxo/admin.php')

    def tearDown(self):
        print('这是测试结果')

    def test_01_po_login(self):
        login_page = AdminLoginPage(self.driver)
        login_page.login("admin", "shopxo")