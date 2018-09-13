# coding=utf-8
from appium import webdriver
import time

#
# desired_caps = {
#         'platformName': 'Android',
#         'deviceName': '192.168.235.101:5555',
#         'platformVersion': '6.0',
#         'app': 'D:\QQ.apk',
#         'unicodeKeyboard': 'True',
#         'resetKeyboard': 'True'
#     }
#
# start_p = 'com.tencent.mobileqq.activity.SplashActivity'
# start_a = 'com.tencent.mobileqq'
# driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
# driver.start_activity(start_p, start_a)
# time.sleep(3)
# driver.quit()


# 屏幕向上滑
def slideUp():
    time.sleep(2)
    window_size = driver.get_window_size()
    x = window_size['width']
    y = window_size['height']
    x1 = int(x * 0.5)
    y1 = int(y * 0.82)
    y2 = int(y * 0.31)
    driver.swipe(start_x=x1, start_y=y1, end_x=x1, end_y=y2, duration=500)


# 屏幕向下滑
def slideDown():
    time.sleep(2)
    window_size = driver.get_window_size()
    x = window_size['width']
    y = window_size['height']
    x1 = int(x * 0.5)
    y1 = int(y * 0.24)
    y2 = int(y * 0.85)
    driver.swipe(start_x=x1, start_y=y1, end_x=x1, end_y=y2, duration=500)

desired_caps = {}

desired_caps['platformName'] = 'Android'

desired_caps['platformVersion'] = '6.0'

desired_caps['deviceName'] = '612QKBQG222LL'

desired_caps['appPackage'] = 'com.xuwang.flashshop'

desired_caps['appActivity'] = 'com.beihui.aixin.ui.activity.WelcomeActivity'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# driver.find_element_by_id("url_field").send_keys("sokatv.com")
#
# driver.find_element_by_id("right_state_button").click()
#
# slideUp()
#
# driver.find_element_by_xpath("//*[@index='10' and @class='android.view.View']").click()
#
# slideDown()

time.sleep(10)

driver.quit()



