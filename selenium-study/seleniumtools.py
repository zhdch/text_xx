from selenium.webdriver.support.ui import WebDriverWait

def find_element(driver, locator, timeout=60):
    return WebDriverWait(driver, timeout).until(lambda s: s.find_element(*locator))
    # 找到了元素，就返回元素，没有找到元素，就等待 timeout的时间