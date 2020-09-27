from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path='./chromedriver.exe')

driver.get('http://118.24.255.132:9090/shopxo/')
driver.maximize_window()
driver.find_element_by_xpath('/html/body/div[7]/div[1]/div[2]/div[2]/div[5]/div/div/a').click()
driver.implicitly_wait(5)
driver.switch_to_window(driver.window_handles[-1])
driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[2]/div[3]/div[2]/div/button').click()
