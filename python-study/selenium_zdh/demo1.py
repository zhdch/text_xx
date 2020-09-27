# 第一步：导入selenium
from selenium import webdriver


# 第二步：打开谷歌浏览器，并获得浏览器的句柄（把柄）
driver = webdriver.Chrome(executable_path="./chromedriver.exe")

# 第三步：打开百度
driver.get("https://www.baidu.com/")

# 第四步：输入搜索关键字
element1 = driver.find_element_by_id("kw")
element1.send_keys("斗地主")

# 第五步： 点击搜索按钮
element2 = driver.find_element_by_id("su")
element2.click()

driver.implicitly_wait(10)
element3 = driver.find_element_by_xpath('//*[@id="6"]/h3/a').click()

driver.implicitly_wait(10)
element4 = driver.find_element_by_xpath('/html/body/div/div[1]/div/div[5]/div/a[1]').click()

# # 最后一步: 结束测试
# driver.quit()


