# 1.导入appium的webdriver
from appium import webdriver
desired_caps = {}
desired_caps['platformName'] = 'Android'                    # 打开什么平台的app，固定的 > 启动安卓平台
desired_caps['platformVersion'] = '9'                   # 安卓系统的版本号：adb shell getprop ro.build.version.release
desired_caps['deviceName'] = 'MI 6'                # 手机/模拟器的型号：adb shell getprop ro.product.model
desired_caps['appPackage'] = '364ae2e u0 com.miui.home/.launcher.Launcher t1'               # app的名字：
                                                            # 安卓8.1之前：adb shell dumpsys activity | findstr "mFocusedActivity"
                                                            # 安卓8.1之后：adb shell dumpsys activity | findstr "mResume"
desired_caps['appActivity'] = '淘宝'              # 同上↑
desired_caps['unicodeKeyboard'] = True                      # 为了支持中文
desired_caps['resetKeyboard'] = True                        # 设置成appium自带的键盘
desired_caps['noReset'] = True                # 绕过登陆
# 去打开app，并且返回当前app的操作对象
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

driver.find_element_by_accessibility_id('')       # 通过aid来定位
driver.find_element_by_xpath('')              # 通过xpath来定位
driver.find_element_by_id('')            # 通过id来定位
driver.find_element_by_android_uiautomator('new UiSelector().text("")')           # 通过文本值来定位