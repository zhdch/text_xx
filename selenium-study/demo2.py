# 导入selenium
from selenium import webdriver

# 第一步：打开谷歌浏览器，并获得浏览器的句柄（把柄）
driver = webdriver.Chrome(executable_path="./chromedriver.exe")

# 第二步：打开网页
driver.get("https://www.baidu.com/")

# 第三步：操作元素
# 1.通过id定位元素
driver.find_element_by_id('kw').send_keys('这是来自selenium的搜索')
# 2.通过xpath定位
driver.find_element_by_xpath(//*[@id="su"]).click()     # .click 元素点击方法
# 3.通过classname来定位
driver.find_element_by_class_name('s_ipt').send_keys('初学者的好奇心')
# 4.通过name来定位
driver.find_element_by_name('wd').send_keys('好奇心害死猫')
# 5.通过css selector来定位
driver.find_element_by_css_selector('#kw').send_keys('这是来自selenium的搜索')
# 6.通过文本值定位超链接
driver.find_element_by_link_text('学术').click()
# 7.通过部分文字定位超链接
driver.find_element_by_partial_link_text('术').click()
# 8.通过标签来定位：tag（不推荐）
driver.find_element_by_tag_name('').click()
driver.maximize_window    # 让网页全屏