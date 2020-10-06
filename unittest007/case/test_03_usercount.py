import unittest, time       # 导入unittest
from selenium import webdriver         # 导入selenium
from utils.seleniumtools import find_element         # 导入动态查找

# unittest 的测试用例是用类来管理的
@unittest.skip("你先暂停吧")
class TestAdminUserCount(unittest.TestCase):

    @classmethod   # 下边的这个方法是类方法,在类开始的时候执行一次
    def setUpClass(cls):       # cls 作用和self相同
        cls.driver = webdriver.Chrome(executable_path='driver/chromedriver.exe')
        cls.driver.maximize_window()

    # 在类结束的时候执行一次
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        self.driver.get('http://118.24.255.132:9090/shopxo/admin.php')
        # 判断用户是否登陆,这种情况用于没有验证码的登陆，直接判断，如果没有登陆，那就执行登陆。
        curl = "http://118.24.255.132:9090/shopxo/admin.php?s=/admin/logininfo.html"
        if self.driver.current_url == curl:
            username = ('name', 'username')
            password = ('name', 'login_pwd')
            loginbtn = ('xpath', '/html/body/div[1]/div/div[2]/div/form/div/div[3]/button')
            find_element(self.driver, username).send_keys("admin")
            find_element(self.driver, password).send_keys("shopxo")
            find_element(self.driver, loginbtn).click()

        # 进入首页之后，切换到小网页
        eframe = find_element(self.driver, ('id', 'ifcontent'))
        self.driver.switch_to_frame(eframe)
        time.sleep(3)

    def test_01_count(self):
        usercount = ('xpath', '/html/body/div[1]/div/div[1]/ul/li[1]/div/p[2]')
        assert find_element(self.driver, usercount).text == "47"

    def test_02_order_count(self):
        ordercount = ('xpath', '/html/body/div[1]/div/div[1]/ul/li[2]/div/p[2]')
        assert find_element(self.driver, ordercount).text == "90"


