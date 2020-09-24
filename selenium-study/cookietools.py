import time
from selenium import webdriver
from seleniumtools import find_element

driver = webdriver.Chrome(executable_path="./chromedriver")
driver.maximize_window()  # 让浏览器最大化
driver.get("https://www.bilibili.com/")

# step1:手动的输入账号密码，去登录成功然后获取登录之后的cookie
time.sleep(30)
print(driver.get_cookies()) # 获取cookie

# step2:使用登录之后的cookie去访问网页，就能绕过登录
driver.delete_all_cookies()   # 获取到cookie之后登陆 哔哩哔哩
coo = [{'domain': '.bilibili.com',  'httpOnly': False, 'name': 'bili_jct', 'path': '/', 'secure': False, 'value': 'af682bdf6122b6529bd2dae3b5108a81'}, {'domain': '.bilibili.com', 'httpOnly': True, 'name': 'SESSDATA', 'path': '/', 'secure': False, 'value': 'bffbd5a3%2C1616249786%2Ced722*91'}, {'domain': '.bilibili.com',  'httpOnly': False, 'name': 'DedeUserID', 'path': '/', 'secure': False, 'value': '485699691'}, {'domain': '.bilibili.com',  'httpOnly': False, 'name': 'sid', 'path': '/', 'secure': False, 'value': '703ksjmu'}, {'domain': 'www.bilibili.com', 'httpOnly': False, 'name': 'finger', 'path': '/', 'secure': False, 'value': '481832271'}, {'domain': '.bilibili.com', 'httpOnly': False, 'name': 'buvid3', 'path': '/', 'secure': False, 'value': 'C2D49D42-170B-48C7-B916-707AFE49B2EC143097infoc'}, {'domain': '.bilibili.com',  'httpOnly': False, 'name': 'DedeUserID__ckMd5', 'path': '/', 'secure': False, 'value': '8a0e1d565e63f583'}, {'domain': '.bilibili.com',  'httpOnly': False, 'name': '_uuid', 'path': '/', 'secure': False, 'value': '8D416BC3-177E-4AF2-076F-6CD3C5788DE864102infoc'}]
for c in coo:
    driver.add_cookie(c)
driver.refresh()