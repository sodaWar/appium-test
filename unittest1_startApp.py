# -* encoding:utf-8 *-
from appium import webdriver
import time
import unittest
import os
import math

class AutoTest(unittest.TestCase):
    def test_setUp(self):
        desired_caps = {
            'platformName' : 'Android',      #测试平台的名称
            'deviceName' : '192.168.56.101:5555',    #连接的设备号，通过adb devices查看所得
            'platformVersion' : '4.4.4',     #测试平台版本，移动设备固件的版本号
            'appPackage' : 'com.football.soccerbook',    #应用包名
            'appActivity' : 'com.soka.football.home.ui.login.activity.SplashActivity',  #应用活动名
            'unicodeKeyboard' : 'True',  #是否使用unicode键盘输入，true则允许输入中文和特殊字符
            'resetKeyboard' : 'True'  #用例执行完后重置键盘为原始状态
        }

        # self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub',desired_caps)
        self.driver.implicitly_wait(3)    #隐式等待，作用介绍如下：
#当查找元素或元素并没有立即出现的时候，隐式等待将等待一段时间再查找 DOM，默认的时间是0；一旦设置了隐式等待，则它存在整个 WebDriver 对象实例的声明周期中
#它将会在寻找每个元素的时候都进行等待，这样会增加整个测试执行的时间

    # def test_login(self):


    # def tearDown(self):
    #     self.driver.quit()

if __name__ == '__main__':
    # suite = unittest.TestLoader().loadTestsFromTestCase(AutoTest)
    # unittest.TextTestRunner(verbosity=2).run(suite)
    unittest.main()