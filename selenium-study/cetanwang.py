from selenium import webdriver
from seleniumtools import find_element
driver = webdriver.Chrome(executable_path='./chromedriver.exe')
driver.get('http://118.24.105.78:8080/ljindex/')
driver.maximize_window
a1 = ('link_text','注册')
find_element(driver,a1).click()
a2 = driver.find_element_by_id
a2('username').send_keys('zhdchzhdch')
a2('phonenum').send_keys('13312121212')
a2('password').send_keys('zhdch123456')
a2('confirpw').send_keys('zhdch123456')
a2('emailnum').send_keys('zhdch@163.com')
a2('userRegist').click()
a2('username').send_keys('zhdchzhdch')
a2('password').send_keys('zhdch123456')
a2('userlogin').click()