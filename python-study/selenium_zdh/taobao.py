from selenium import webdriver
from seleniumtools import find_element
driver = webdriver.Chrome(executable_path='./chromedriver.exe')
driver.get('https://www.taobao.com')
driver.maximize_window()
srk = ('id','q')
find_element(driver,srk).send_keys('海蓝之谜')
sousuo = ('xpath','//*[@id="J_TSearchForm"]/div[1]/button')
find_element(driver,sousuo).click()
# 动态查找元素，等待元素加载出来
driver.switch_to_alert().accept()   # 确定按钮
driver.switch_to_alert().dismiss()   # 取消按钮
 # 作用域切换到新的窗口
driver.switch_to_window(driver.window_handles[-1]) 
# 切换到 iframe嵌套的网页
i = ('id','ifcontent')
iframe = find_element(driver,i)
driver.switch_to_frame(iframe)
# 切换到默认的大网页
driver.switch_to_default_content()     

