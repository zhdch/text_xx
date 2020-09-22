from selenium import webdriver
driver = webdriver.Chrome(executable_path='./chromedriver.exe')
driver.get('https://www.taobao.com')
driver.maximize_window()
a = driver.find_element_by_id('qq')
a.send_keys('海蓝之谜')
print(a)
b = driver.find_element_by_xpath('//*[@id="J_TSearchForm"]/div[1]/button')
b.click()
print(b)


