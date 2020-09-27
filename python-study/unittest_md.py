# unittest简介
# python自带的测试框架，用于单元测试，自动化测试

# 测试用例
# 模块名：test_01_模块名.py
# 每一个case是一个成员方法

# 测试结果
# .代表通过
# F代表断言失败
# E代表测试用例或代码异常

# 生命周期
# setupclass >> setup(01) >> test(01) >> teardowm(01) >> setup(02) >> test(02) >> teardown(02) >>...>> teardownclass
# setup是每一个case的前置条件，teardown是后置条件，不一定每个用例都用，看具体是否需要

# web自动化测试用例
# web自动化用例都在在功能测试用例中选取的，选取适合自动化测试的测试用例

# 对于falicase和errorcass,最后需要人工验证一下。

# web自动化一般都到系统稳定了以后，再去做的

# po是selenium的设计思想
# 把每个页面用到的元素和动作封装到类中，元素封装到成员变量，动作封装成成员方法
# 在po文件夹下：
"""
from utils.seleniumtools import find_element
class AdminLoginPage():

    def __init__(self, driver):

        # 把用到的元素封装到成员变量
        self.driver = driver
        self.username = ('name', 'username')
        self.password = ('name', 'login_pwd')
        self.login_button = ('xpath', '/html/body/div[1]/div/div[2]/div/form/div/div[3]/button')
        self.url = "http://118.24.255.132:9090/shopxo/admin.php?s=/admin/logininfo.html"

        # 封装操作的步骤
        def login(self, u, p):
            find_element(self.driver, self.username).send_keys(u)
            find_element(self.driver, self.password).send_keys(p)
            find_element(self.driver, self.login_button).click()
"""
# 在case文件夹里面调用：
"""
    def test_07_po_login(self):
        driver = webdriver.Chrome(executable_path='./driver/chromedriver.exe')
        driver.get("http://118.24.255.132:9090/shopxo/admin.php")

        login_page = AdminLoginPage(driver)
        login_page.login("admin", "shopxo")
"""
# 调用 po封装好的方法的好处：
# 方便脚本的维护
# po执行的顺序： case调用po，po调用find_element
