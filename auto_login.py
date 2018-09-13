# -* encoding:utf-8 *-
from appium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from appium.webdriver.common.multi_action import MultiAction
from collections import Counter                                 #使用Counter(列表)的方法时可以需要导入该报
from test_cm_upgrade import *
from reptile_request_get import *
from receive_email import  *
import unittest
import time
import requests
import json
import os



class AutoTest(unittest.TestCase):
    desired_caps = {
        'platformName': 'Android',
        'deviceName': '192.168.56.101:5555',
        'platformVersion': '4.4.4',
        'app': '/Users/apple/test2.2.0.apk',
        # 'appPackage': 'com.football.soccerbook',
        # 'appActivity': 'com.soka.football.home.ui.login.activity.SplashActivity',
        'unicodeKeyboard': 'True',
        'resetKeyboard': 'True'
    }

    driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', desired_caps)
    start_p = 'com.football.supergoal'
    start_a = 'com.soka.football.home.ui.login.activity.SplashActivity'

    # 卸载重新安装APP，在测试订阅的时候用，其他页面隐藏
    if driver.is_app_installed("com.football.supergoal"):
        driver.remove_app("com.football.supergoal")
        driver.install_app("/Users/apple/test2.2.0.apk")
    else:
        print 'app have installed'

    time.sleep(3)
    driver.start_activity(start_p, start_a)
    driver.implicitly_wait(5)

    @classmethod
    def setUpClass(cls):    #每个测试函数运行前运行，即每个test方法运行前运行一次，setUpClass（cls）是所有test运行前运行，即某个类中所有test方法运行前运行
        #如果运行一个类中的测试用例放，那么setUpClass()方法只运行一次，如果该类中有3个test方法，则setUp()方法运行3次
        print 'process is set up now'

    @classmethod
    def tearDownClass(cls):       #每个测试函数运行完后运行，tearDownClass(cls)所有test运行完后运行一次,记住setUpClass方法定义时必须加@classmethod,而tearDown()方法不用加
        print "clean the process after it down "


    #测试用例方法开始处

    #检验email是否存在，并生成一个可用的email
    def emailScreen(self):
        conn, cur = connDB()
        result = selectDBAuto(cur, 'identity', 'identity')
        email = '840@qq.com'
        # print result[0][0]
        for i in range(0, len(result)):
            a = str(i)
            if (email == result[i][0]):
                if len(email) == 10:
                    email = email[:2] + a + email[3:]
                elif len(email) == 11:
                    email = email[:2] + a + email[4:]
                elif len(email) == 12:
                    email = email[:2] + a + email[5:]
                elif len(email) == 13:
                    email = email[:2] + a + email[6:]
                else:
                    print '邮箱已到达14位了，请在循环条件中添加'
        print ("the email is availabe:") + email
        return email

    #删除文本框内容
    def editTextClear(self,text):
        driver = self.driver
        driver.keyevent(123)              #该方法将光标移到最后
        for i in range(0,len(text)):
            driver.keyevent(67)              #退格键，删除作用

    #屏幕向上滑
    def slideUp(self):
        time.sleep(2)
        window_size = self.driver.get_window_size()
        x = window_size['width']
        y = window_size['height']
        x1 = int(x * 0.5)
        y1 = int(y * 0.82)
        y2 = int(y * 0.31)
        self.driver.swipe(start_x=x1, start_y=y1, end_x=x1, end_y=y2, duration=500)
    #屏幕向下滑
    def slideDown(self):
        time.sleep(2)
        window_size = self.driver.get_window_size()
        x = window_size['width']
        y = window_size['height']
        x1 = int(x * 0.5)
        y1 = int(y * 0.24)
        y2 = int(y * 0.75)
        self.driver.swipe(start_x=x1, start_y=y1, end_x=x1, end_y=y2, duration=500)
    #屏幕向右滑
    def slideRight(self):
        time.sleep(2)      #该段休眠代码很重要，不然会报错
        window_size = self.driver.get_window_size()
        x = window_size['width']
        y = window_size['height']
        x1 = int(x * 0.36)
        x2 = int(x * 0.84)
        y1 = int(y * 0.5)
        self.driver.swipe(start_x=x1,start_y=y1,end_x=x2,end_y=y1,duration=500)
    #屏幕向左滑
    def slideLeft(self):
        time.sleep(2)      #该段休眠代码很重要，不然会报错
        window_size = self.driver.get_window_size()
        x = window_size['width']
        y = window_size['height']
        x1 = int(x * 0.84)
        y1 = int(y * 0.36)
        x2 = int(x * 0.1)
        self.driver.swipe(start_x=x1, start_y=y1, end_x=x2, end_y=y1, duration=500)

    #教学页面
    def test_teach(self):                        #旧版本有教学页面，现在版本取消该功能了
        driver = self.driver
        time.sleep(2)
        driver.reset()
        time.sleep(2)
        self.slideLeft()
        self.slideLeft()
        driver.find_element_by_id("btn_enter").click()

        driver.find_element_by_id("tv_standard").click()
        # driver.find_element_by_id("title_bar_iv_left").click()
        # driver.find_element_by_id("tv_myCoin").click()
        # driver.find_element_by_id("tv_sign_in").click()
        # driver.find_element_by_id("tv_task_name").click()

    #setting、copyright、server页面的跳转
    def test_anotherPage(self):
        driver = self.driver

        driver.find_element_by_id("title_bar_iv_left").click()
        driver.find_element_by_id("tv_setting").click()           #个人中心setting页面
        time.sleep(2)
        driver.get_screenshot_as_file('/Users/apple/AppiumTestPng/set_w.png')
        time.sleep(1)
        driver.find_element_by_id("title_bar_iv_left").click()

        time.sleep(1)
        driver.find_element_by_id("title_bar_iv_left").click()
        driver.find_element_by_id("tv_copyright").click()      #个人中心copyright页面
        time.sleep(2)
        driver.get_screenshot_as_file('/Users/apple/AppiumTestPng/copyright_w.png')
        time.sleep(1)
        driver.find_element_by_id("title_bar_iv_left").click()

        time.sleep(1)
        window_size = self.driver.get_window_size()
        x = window_size['width']        #该模拟器的宽是480
        y = window_size['height']       #该模拟器的长是728
        x1 = int(x * 0.24)
        y1 = int(y * 0.54)
        y2 = int(y * 0.357)
        self.driver.swipe(start_x=x1, start_y=y1, end_x=x1, end_y=y2, duration=1000)

        time.sleep(1)
        driver.find_element_by_id("tv_service").click()      #个人中心service页面
        time.sleep(2)
        driver.get_screenshot_as_file('/Users/apple/AppiumTestPng/server_w.png')
        driver.find_element_by_id("title_bar_iv_left").click()

        driver.find_element_by_id("tv_policy").click()       #个人中心privacy页面
        time.sleep(2)
        driver.get_screenshot_as_file("/Users/apple/AppiumTestPng/privacy_policy.png")
        driver.find_element_by_id("title_bar_iv_left").click()

        self.driver.swipe(start_x=x1, start_y=y2, end_x=x1, end_y=y1, duration=1000)

        time.sleep(1)
        driver.find_element_by_id("iv_avatar").click()
        time.sleep(3)
        driver.tap([(285,593)])     #登录页面中service页面，通过元素坐标点击，注意该方式点击，在tap方法内传入的position参数值必须是元组
        time.sleep(3)
        driver.get_screenshot_as_file("/Users/apple/AppiumTestPng/login_service.png")
        driver.find_element_by_id("title_bar_iv_left").click()

        time.sleep(1)
        driver.tap([(102,611)])            #登录页面中privacy页面
        time.sleep(3)
        driver.get_screenshot_as_file("/Users/apple/AppiumTestPng/login_privacy.png")
        driver.find_element_by_id("title_bar_iv_left").click()

        time.sleep(1)
        driver.find_element_by_id("rb_sign_up").click()
        time.sleep(1)
        driver.tap([(366,583)])       #注册页面中service页面
        time.sleep(3)
        driver.get_screenshot_as_file("/Users/apple/AppiumTestPng/register_service.png")
        driver.find_element_by_id("title_bar_iv_left").click()

        time.sleep(1)
        driver.tap([(202,605)])        #注册页面中privacy页面
        time.sleep(3)
        driver.get_screenshot_as_file("/Users/apple/AppiumTestPng/register_privacy.png")
        driver.find_element_by_id("title_bar_iv_left").click()

    #feedback页面
    def test_feedback(self):
        driver = self.driver
        driver.find_element_by_id("title_bar_iv_left").click()
        driver.find_element_by_id("tv_feedback").click()
        # time.sleep(1)
        driver.find_element_by_id("btn_send").click()
        time.sleep(1)

        driver.get_screenshot_as_file("/Users/apple/AppiumTestPng/fb_noinput_w.png")
        time.sleep(1)

        a = driver.find_element_by_id("et_suggest")
        a.click()
        a.send_keys('this is autotest')      #用户反馈功能的测试用例编写，还有部分可待之后再补
        driver.find_element_by_id("btn_send").click()
        driver.get_screenshot_as_file("/Users/apple/AppiumTestPng/fb_normal1_w.png")
        time.sleep(1)
        driver.get_screenshot_as_file("/Users/apple/AppiumTestPng/fb_normal2_w.png")
        # time.sleep(1)

        conn, cur = connDB()
        result = feedbackAuto(cur)    #注意，这里content的内容写死了，之后变化需要同步进行更改
        return result[0][0]      #该代码作用是查询出刚发送消息的用户Uid

    #coinsmall页面
    def test_mall(self):
        uid = self.test_feedback()
        print uid
        print isinstance(uid,int)
        driver = self.driver

        conn, cur = connDB()
        result1 = permission(cur,uid)     #查询出刚发送feedback的用户，是否具有积分兑换权限
        if result1 == 0:     #0代表该用户没有权限
            driver.find_element_by_id("title_bar_iv_left").click()
            driver.find_element_by_id("tv_mall").click()
            time.sleep(5)
            driver.get_screenshot_as_file("/Users/apple/AppiumTestPng/mall_noper_w.png")   #用户没有权限时页面的显示情况
            time.sleep(2)

            insert_permission(conn, cur, uid)   #新增用户积分兑换权限
            time.sleep(3)
            driver.find_element_by_id("title_bar_iv_left").click()
            driver.find_element_by_id("tv_mall").click()
            time.sleep(5)
            driver.get_screenshot_as_file("/Users/apple/AppiumTestPng/mall_haveper_w.png")  #用户拥有权限时页面的显示情况
            time.sleep(2)


        elif result1 == 1:
            driver.find_element_by_id("title_bar_iv_left").click()
            driver.find_element_by_id("tv_mall").click()
            time.sleep(5)
            driver.get_screenshot_as_file("/Users/apple/AppiumTestPng/mall_haveper_w.png")
            time.sleep(2)

            delete_permission(conn, cur, uid)  #删除权限
            time.sleep(3)
            driver.find_element_by_id("title_bar_iv_left").click()
            driver.find_element_by_id("tv_mall").click()
            time.sleep(5)
            driver.get_screenshot_as_file("/Users/apple/AppiumTestPng/mall_noper_w.png")
            time.sleep(2)
        else:
            print '数据库中积分兑换权限的字段值发生了变化，请核对之'

    #注册页面
    def test_register(self):
        for i in range(1000):
            driver = self.driver
            email = self.emailScreen()
            password = '123456'
            # time.sleep(1)
            if i == 0:
                driver.find_element_by_id("title_bar_iv_left").click()
            else:
                driver.find_element_by_id("iv_avatar").click()
                driver.find_element_by_id("rb_sign_up").click()
                # time.sleep(2)
                a = driver.find_element_by_id("et_email")   #输入数据库中不存在且格式正确的email
                a.click()
                a.send_keys(email)
                b = driver.find_element_by_id("et_password")   #输入格式正确的密码
                # b.click()
                # b.send_keys('12345')       #输入少于6位数的密码
                # driver.find_element_by_id("et_confirm_password").click()
                # driver.get_screenshot_as_file("/Users/apple/AppiumTestPng/wrong_password1.png")
                #
                # b.click()
                # b.send_keys('123456789012345678901')        #输入大于20位数的密码
                # driver.find_element_by_id("et_confirm_password").click()
                # driver.get_screenshot_as_file("/Users/apple/AppiumTestPng/wrong_password2.png")

                b.click()
                b.send_keys(password)           #输入6位数正确的密码

                c = driver.find_element_by_id("et_confirm_password")
                c.click()
                # c.send_keys('1234567')                              #确认密码错误
                # driver.find_element_by_id("et_password").click()
                # driver.get_screenshot_as_file("/Users/apple/AppiumTestPng/wrong_confirmPassword.png")


                c.send_keys(password)                          #注册的冒烟测试
                driver.find_element_by_id("btn_sign").click()
                # time.sleep(1)
                driver.find_element_by_id("iv_avatar").click()
                driver.find_element_by_id("btn_logout").click()
                driver.find_element_by_id("btn_confirm").click()
                # time.sleep(1)
                # driver.get_screenshot_as_file("/Users/apple/AppiumTestPng/normal_register_w.png")

    #登录页面
    def test_login(self):
        driver = self.driver
        driver.find_element_by_id('title_bar_iv_left').click()
        driver.find_element_by_id("iv_avatar").click()
        time.sleep(2)
        a = driver.find_element_by_id("et_email")
        a.click()
        a.send_keys('abddsaqqcom')
        b = driver.find_element_by_id("et_password")
        b.click()
        driver.get_screenshot_as_file("/Users/apple/AppiumTestPng/wrong1_login_email.png")   #邮箱只输入字母

        a.click()
        a.send_keys('89302675023')
        b.click()
        driver.get_screenshot_as_file("/Users/apple/AppiumTestPng/wrong2_login_email.png")   #邮箱只输入数字

        a.click()
        a.send_keys('     893026750@163.com')                                       #邮箱输入首部为空格
        b.click()
        driver.get_screenshot_as_file("/Users/apple/AppiumTestPng/wrong3_login_email.png")

        a.click()
        a.send_keys('893026750@163.com')
        for i in range(1,7):                                                        #邮箱输入尾部为空格
            driver.keyevent(62)
        b.click()
        driver.get_screenshot_as_file("/Users/apple/AppiumTestPng/wrong4_login_email.png")

        a.click()
        a.send_keys('893026750      @163.com')                                     #邮箱输入中间为空格
        b.click()
        driver.get_screenshot_as_file("/Users/apple/AppiumTestPng/wrong5_login_email.png")

        a.click()
        a.send_keys('893026750@163com')                                             #邮箱输入没有点号
        b.click()
        driver.get_screenshot_as_file("/Users/apple/AppiumTestPng/wrong6_login_email.png")

        a.click()
        a.send_keys('893026750163.com')                                             #邮箱输入没有@符号
        b.click()
        driver.get_screenshot_as_file("/Users/apple/AppiumTestPng/wrong7_login_email.png")

        a.click()
        a.send_keys('h893026750@qq.com')                                            #邮箱输入格式正确
        b.click()
        driver.get_screenshot_as_file("/Users/apple/AppiumTestPng/wrong8_login_email.png")

        b.send_keys('12345')                                                      #密码输入格式只有5位
        a.click()
        driver.get_screenshot_as_file("/Users/apple/AppiumTestPng/wrong1_login_password.png")

        b.click()
        b.send_keys('naiwu0113425hongnaiwu')                                      #密码输入格式有21位
        a.click()
        driver.get_screenshot_as_file("/Users/apple/AppiumTestPng/wrong2_login_password.png")

        b.click()
        b.send_keys('aiwu0113425hongnaiwu')                                        #密码输入有20位
        a.click()
        driver.get_screenshot_as_file("/Users/apple/AppiumTestPng/wrong3_login_password.png")

        b.click()
        b.send_keys('123456')
        a.click()                                                                        #输入6位格式正确的密码
        driver.get_screenshot_as_file("/Users/apple/AppiumTestPng/wrong4_login_password.png")

        driver.find_element_by_id('btn_login').click()
        time.sleep(1)
        driver.get_screenshot_as_file("/Users/apple/AppiumTestPng/login_emailWrong.png")   #登录一个数据库不存在的即未注册的账号

        a.click()
        a.send_keys('893026750@qq.com')
        b.click()
        b.send_keys('12345678')
        driver.find_element_by_id('btn_login').click()
        time.sleep(1)
        driver.get_screenshot_as_file("/Users/apple/AppiumTestPng/login_passwordWrong.png")       #登录密码错误

        b.click()
        b.send_keys('123456')
        driver.find_element_by_id('btn_login').click()
        time.sleep(2)
        driver.get_screenshot_as_file("/Users/apple/AppiumTestPng/login_normal.png")         #登录正确的账号密码

        driver.find_element_by_id('iv_avatar').click()                                       #用户退出登录
        time.sleep(1)
        driver.find_element_by_id('btn_logout').click()
        driver.find_element_by_id('btn_confirm').click()
        driver.find_element_by_id('iv_avatar').click()

        a.click()
        a.send_keys('h893026750qq.com')                                                     #邮箱格式不正确
        driver.find_element_by_id('tv_forget').click()
        driver.get_screenshot_as_file('/Users/apple/AppiumTestPng/forgotPW_emailWrong1.png')

        a.click()
        a.send_keys('h893026750@qq.com')
        driver.find_element_by_id('tv_forget').click()                                      #邮箱在数据库中不存在
        time.sleep(2)
        driver.get_screenshot_as_file('/Users/apple/AppiumTestPng/forgotPW_emailWrong2.png')

        a.click()
        a.send_keys('893026750@qq.com')
        driver.find_element_by_id('tv_forget').click()                                      #邮箱正确且存在
        time.sleep(2)
        driver.get_screenshot_as_file('/Users/apple/AppiumTestPng/forgotPW_normal.png')

        c = driver.find_element_by_id('et_new')
        c.click()
        c.send_keys('123456')

        d = driver.find_element_by_id('et_confirm')                              #再次输入的密码错误
        d.click()
        d.send_keys('1234567')
        e = driver.find_element_by_id('et_code')
        e.click()
        driver.get_screenshot_as_file('/Users/apple/AppiumTestPng/forgotPW_confirmW.png')

        d.click()
        d.send_keys('123456')                                                 #验证码输入错误
        e.send_keys('asj1')
        driver.find_element_by_id('btn_change').click()
        time.sleep(2)
        driver.get_screenshot_as_file('/Users/apple/AppiumTestPng/forgotPW_code1.png')

        r, t = receiveEmail()
        time.sleep(2)
        e.click()
        text = e.get_attribute('text')
        self.editTextClear(text)
        e.send_keys(t[0])                            #怎么输入超时的验证码，输入在解码邮箱时，加个多重判断筛选，已实现
        driver.find_element_by_id('btn_change').click()                           #输入超时的验证码
        time.sleep(2)
        driver.get_screenshot_as_file('/Users/apple/AppiumTestPng/forgotPW_code2.png')

        e.click()
        text = e.get_attribute('text')
        self.editTextClear(text)
        e.send_keys(r[0])
        driver.find_element_by_id('btn_change').click()                        #输入正确的验证码
        time.sleep(2)
        driver.get_screenshot_as_file('/Users/apple/AppiumTestPng/forgotPW_code3.png')

    #完成签到任务
    def test_cplSingInTask(self):
        uid = self.test_feedback()                  #获取用户的uid值
        print uid
        # print isinstance(uid,int)                 #判断uid值是否是int类型
        conn, cur = connDB()
        delete_userSign(conn, cur, uid)
        print '删除用户签到记录成功'
        driver = self.driver

        driver.find_element_by_id('title_bar_iv_left').click()
        driver.find_element_by_id('tv_myCoin').click()
        time.sleep(2)
        driver.get_screenshot_as_file('/Users/apple/AppiumTestPng/myCoins.png')       #我的金币页面
        driver.find_element_by_id('tv_sign_in').click()
        driver.find_element_by_id('tv_sign_in').click()
        time.sleep(2)
        driver.get_screenshot_as_file('/Users/apple/AppiumTestPng/complete_SingInTask1.png')    #签到第一天的截图
        driver.tap([(106, 131)])
        time.sleep(2)
        driver.get_screenshot_as_file('/Users/apple/AppiumTestPng/complete_SingInTask2.png')   #查看第一天签到后金币是否加1的截图

        for i in range(7):                #再签到7天,查看签到后的截图
            update_userSign(conn, cur, uid)
            driver.find_element_by_id('title_bar_iv_left').click()
            driver.find_element_by_id('tv_myCoin').click()
            driver.find_element_by_id('tv_sign_in').click()
            driver.find_element_by_id('tv_sign_in').click()
            time.sleep(2)
            if i == 0:
                driver.get_screenshot_as_file('/Users/apple/AppiumTestPng/complete_SingInTask3.png')  #签到第二天的截图
                driver.tap([(106, 131)])
                time.sleep(2)
                driver.get_screenshot_as_file('/Users/apple/AppiumTestPng/complete_SingInTask4.png')  #查看第二天签到后金币是否加2的截图
            elif i == 1:
                driver.get_screenshot_as_file('/Users/apple/AppiumTestPng/complete_SingInTask5.png')  # 签到第三天的截图
                driver.tap([(106, 131)])
                time.sleep(2)
                driver.get_screenshot_as_file('/Users/apple/AppiumTestPng/complete_SingInTask6.png')  #查看第三天签到后金币是否加3的截图
            elif i == 2:
                driver.get_screenshot_as_file('/Users/apple/AppiumTestPng/complete_SingInTask7.png')  # 签到第四天的截图
                driver.tap([(106,131)])
                time.sleep(2)
                driver.get_screenshot_as_file('/Users/apple/AppiumTestPng/complete_SingInTask8.png')  #查看第四天签到后金币是否加4的截图
            elif i == 3:
                driver.get_screenshot_as_file('/Users/apple/AppiumTestPng/complete_SingInTask9.png')  # 签到第五天的截图
                driver.tap([(106,131)])
                time.sleep(2)
                driver.get_screenshot_as_file('/Users/apple/AppiumTestPng/complete_SingInTask10.png')  #查看第五天签到后金币是否加5的截图
            elif i == 4:
                driver.get_screenshot_as_file('/Users/apple/AppiumTestPng/complete_SingInTask11.png')  # 签到第六天的截图
                driver.tap([(106,131)])
                time.sleep(2)
                driver.get_screenshot_as_file('/Users/apple/AppiumTestPng/complete_SingInTask12.png')  #查看第六天签到后金币是否加6的截图
            elif i == 5:
                driver.get_screenshot_as_file('/Users/apple/AppiumTestPng/complete_SingInTask13.png')  # 签到第七天的截图
                driver.tap([(106,131)])
                time.sleep(2)
                driver.get_screenshot_as_file('/Users/apple/AppiumTestPng/complete_SingInTask14.png')  #查看第七天签到后金币是否加7的截图
            elif i == 6:
                driver.get_screenshot_as_file('/Users/apple/AppiumTestPng/complete_SingInTask15.png')  # 签到第八天的截图
                driver.tap([(106,131)])
                time.sleep(2)
                driver.get_screenshot_as_file('/Users/apple/AppiumTestPng/complete_SingInTask16.png')  #查看第八天签到后金币是否只加7的截图
            else:
                print '循环出错，请查看程序'
        driver.find_element_by_id('tv_myCoin').click()
        time.sleep(2)
        driver.get_screenshot_as_file('/Users/apple/AppiumTestPng/complete_SingInTask17.png')
        self.slideUp()
        time.sleep(2)
        driver.get_screenshot_as_file('/Users/apple/AppiumTestPng/complete_SingInTask18.png')

    #完成日常任务
    def test_dailyTask(self):
        uid = self.test_feedback()  # 获取用户的uid值
        print uid
        conn, cur = connDB()
        delete_userFetch(conn, cur, 241)
        print '删除用户观看视频文章的记录成功'
        delete_point_record(conn, cur, 241)
        print '删除用户完成任务的记录成功'
        driver = self.driver
        driver.find_element_by_id('title_bar_iv_left').click()
        driver.find_element_by_id('tv_myCoin').click()
        time.sleep(2)
        driver.get_screenshot_as_file('/Users/apple/AppiumTestPng/myCoins.png')       #我的金币页面

        driver.find_element_by_id('title_bar_iv_left').click()                  #完成日常video任务
        driver.tap([(352,320)])
        self.slideUp()
        time.sleep(2)
        driver.find_element_by_id('tv_title').click()
        time.sleep(2)
        driver.get_screenshot_as_file('/Users/apple/AppiumTestPng/complete_task1.png')
        driver.find_element_by_id('tv_view').click()
        time.sleep(2)
        driver.get_screenshot_as_file('/Users/apple/AppiumTestPng/complete_task2.png')

        driver.find_element_by_id('title_bar_iv_left').click()
        driver.find_element_by_id('tv_like').click()                            #完成日常like任务
        time.sleep(2)
        driver.get_screenshot_as_file('/Users/apple/AppiumTestPng/complete_task3.png')

        driver.find_element_by_id('iv_back').click()
        driver.find_element_by_id('title_bar_iv_left').click()
        driver.find_element_by_id('tv_myCoin').click()
        time.sleep(2)
        driver.get_screenshot_as_file('/Users/apple/AppiumTestPng/complete_task4.png')

        driver.find_element_by_id('title_bar_iv_left').click()                  #完成日常news任务
        driver.tap([(363,376)])
        # driver.find_element_by_id('rb_news').click()                          #该方式不能点击news元素，待之后查找原因
        driver.find_element_by_xpath("//*[@text='NEWS']").click()
        time.sleep(4)
        driver.find_element_by_id('tv_views').click()
        time.sleep(2)
        driver.get_screenshot_as_file('/Users/apple/AppiumTestPng/complete_task5.png')
        driver.find_element_by_id('title_bar_iv_left').click()
        driver.find_element_by_id('title_bar_iv_left').click()
        driver.find_element_by_id('tv_myCoin').click()
        time.sleep(2)
        driver.get_screenshot_as_file('/Users/apple/AppiumTestPng/complete_task6.png')    #查看是否任务完成

        team_A_name, team_B_name, match_id, status = select_match(cur)  # 完成日常match任务
        driver.find_element_by_id('title_bar_iv_left').click()
        driver.tap([(352,320)])
        driver.find_element_by_xpath("//*[@text='MATCH']").click()
        text1 = driver.find_element_by_id('tv_left_name').text
        text2 = driver.find_element_by_id('tv_right_name').text
        if team_A_name == text1 and team_B_name == text2:
            driver.find_element_by_id('tv_left_name').click()           #比赛状态为未开始，观看该比赛时任务未完成的截图
            time.sleep(2)
            driver.get_screenshot_as_file('/Users/apple/AppiumTestPng/complete_task7.png')

            driver.find_element_by_id('title_bar_iv_left').click()
            update_match(conn,cur,match_id,status)                      #更改比赛状态为直播中
            driver.find_element_by_id('tv_left_name').click()
            time.sleep(2)
            driver.get_screenshot_as_file('/Users/apple/AppiumTestPng/complete_task8.png')      #观看直播状态的比赛，任务完成的截图

            driver.find_element_by_id('title_bar_iv_left').click()
            driver.find_element_by_id('title_bar_iv_left').click()
            driver.find_element_by_id('tv_myCoin').click()
            time.sleep(2)
            driver.get_screenshot_as_file('/Users/apple/AppiumTestPng/complete_task9.png')      #观看比赛任务完成后金币页面截图

            driver.find_element_by_id('tv_myCoin').click()
            time.sleep(2)
            driver.get_screenshot_as_file('/Users/apple/AppiumTestPng/complete_task10.png')      #查看任务完成金币记录页面

        else:
            print '该比赛显示与数据库中查询出的结果不同，请核对检验'





        # a = 'Huddersfield'
        # driver.find_element_by_xpath("//*[@text=a]").click()          #这种方法是通过text内容来定位元素的，但是text不能使用a变量的值，这个问题待之后处理
        # driver.find_element_by_android_uiautomator('new UiSelector().text("Huddersfield")').click()       #该方法也是通过text内容定位元素的，问题与上面一样

    #完成其他任务
    def test_otherTask(self):
        email = self.emailScreen()
        password = '123456'
        driver = self.driver
        driver.find_element_by_id('title_bar_iv_left').click()
        driver.find_element_by_id('tv_myCoin').click()
        self.slideUp()
        driver.get_screenshot_as_file('/Users/apple/AppiumTestPng/other_task1.png')      #其他任务未完成的截图

        driver.find_element_by_id('title_bar_iv_left').click()
        driver.find_element_by_id('iv_avatar').click()
        driver.find_element_by_id('rb_sign_up').click()
        a = driver.find_element_by_id('et_email')                                       #新注册一个用户然后会自动登录
        a.click()
        a.send_keys(email)
        b = driver.find_element_by_id('et_password')
        b.click()
        b.send_keys(password)
        c = driver.find_element_by_id('et_confirm_password')
        c.click()
        c.send_keys(password)
        driver.find_element_by_id('btn_sign').click()

        time.sleep(3)
        driver.get_screenshot_as_file('/Users/apple/AppiumTestPng/other_task2.png')     #新注册用户是否有1000金币赠送的截图

        driver.find_element_by_id('iv_avatar').click()
        time.sleep(2)
        driver.find_element_by_id('tv_birthday').click()
        driver.find_element_by_id('tv_cancel').click()
        driver.get_screenshot_as_file('/Users/apple/AppiumTestPng/other_task3.png')          #取消设置生日的截图

        driver.find_element_by_id('tv_birthday').click()
        driver.find_element_by_id('tv_confirm').click()
        time.sleep(2)
        driver.get_screenshot_as_file('/Users/apple/AppiumTestPng/other_task4.png')         #设置生日时的任务完成截图

        driver.find_element_by_id('iv_avatar').click()
        driver.find_element_by_id('tv_cancel').click()
        driver.get_screenshot_as_file('/Users/apple/AppiumTestPng/other_task5.png')         #取消设置头像的截图

        driver.find_element_by_id('iv_avatar').click()
        driver.find_element_by_id('tv_one').click()
        time.sleep(1)
        driver.tap([(99,225)])                #以下三个根据模拟器的坐标来实现点击的，如果换个不同手机分辨率或者手机中图片文件有更改，可能会导致寻找不到该元素
        time.sleep(2)
        driver.tap([(241,428)])
        time.sleep(2)
        driver.tap([(105,71)])
        time.sleep(4)
        driver.get_screenshot_as_file('/Users/apple/AppiumTestPng/other_task6.png')       #上传头像的任务完成截图

        driver.find_element_by_id('tv_nickname').click()
        driver.tap([(202,156)])
        driver.press_keycode(32)
        driver.press_keycode(8)
        driver.press_keycode(9)
        driver.press_keycode(39)
        driver.find_element_by_id('title_bar_iv_left').click()
        driver.get_screenshot_as_file('/Users/apple/AppiumTestPng/other_task7.png')         #取消设置昵称的截图

        driver.find_element_by_id('tv_nickname').click()
        driver.tap([(202, 156)])
        driver.press_keycode(32)
        driver.press_keycode(8)
        driver.press_keycode(9)
        driver.press_keycode(39)
        driver.find_element_by_id('title_bar_tv_right').click()
        time.sleep(2)
        driver.get_screenshot_as_file('/Users/apple/AppiumTestPng/other_task8.png')      #设置昵称任务完成的截图

        driver.find_element_by_id('title_bar_iv_left').click()
        driver.find_element_by_id('tv_myCoin').click()
        time.sleep(2)
        self.slideUp()
        driver.get_screenshot_as_file('/Users/apple/AppiumTestPng/other_task9.png')       #其他任务都完成的任务页面展示
        self.slideDown()
        driver.find_element_by_id('tv_myCoin').click()
        time.sleep(3)
        driver.get_screenshot_as_file('/Users/apple/AppiumTestPng/other_task10.png')      #任务完成后金币记录页面展示


        #资讯页面

    #充值功能
    def test_recharge(self):
        uid = self.test_feedback()  # 获取用户的uid值
        print uid
        conn,cur = connDB()
        driver = self.driver

        driver.find_element_by_id('title_bar_iv_left').click()
        driver.tap([(352,320)])
        driver.find_element_by_id('rb_prediction').click()
        time.sleep(3)
        driver.get_screenshot_as_file('/Users/apple/AppiumTestPng/recharge1.png')       #用户没有充值权限的截图

        a = select_recharge(cur, uid)
        update_recharge(conn,cur,uid,a)
        self.slideDown()
        time.sleep(3)
        driver.get_screenshot_as_file('/Users/apple/AppiumTestPng/recharge2.png')       #增加用户充值权限的截图

        driver.find_element_by_id('tv_recharge').click()
        contexts = driver.contexts              #context是代表两个不同的环境，driver.contexts获取native和webview页面环境，返回数列值
        # souce = driver.page_source            #获取当前页面的源代码
        # f = open("page_source.txt",'wb')      #打开一个文件，没有就新建一个，w是新建（会覆盖原有文件），b是二进制文件，a的话就是在末尾追加
        # f.write(souce+'\n')                   #wb就是以二进制写模式打开
        # f.close()                             #写入的内容格式会自动换行，但是不能根据元素换行，即不能显示于网站形式一样，这个问题待之后研究
        driver.switch_to.context(contexts[1])   #切换到webview环境,切换回native环境按以上步骤再次操作即可
        now = driver.current_context
        print now
        # WebDriverWait(driver, 5).until(lambda driver: driver.find_elements_by_class_name('wrapper')[1],message='该元素检测超时，查看网络情况')
        driver.find_element_by_class_name('records').click()
        time.sleep(5)
        driver.switch_to.context("NATIVE_APP")          #切换到原生环境，不然不能够使用下一行截图的代码
        driver.get_screenshot_as_file('/Users/apple/AppiumTestPng/recharge3.png')       #无充值记录时的页面显示
        driver.find_element_by_id('title_bar_iv_left').click()

        driver.switch_to.context(contexts[1])
        for i in range(4):
            time.sleep(2)
            driver.switch_to.context(contexts[1])
            x = driver.find_elements_by_class_name('wrapper')  # 第一个默认金额的元素
            time.sleep(2)       #该段休眠也最好加上，不然也可能会出现运行速度过快，还未获取总的x元素后就再次点击的情况，导致IndexError的错误
            print len(x)        #该段代码不能删，不然会报IndexError异常，超出数列极限,且不能跟上面print len(x)换位置
            print i             #该原因待之后查询
            x[i].click()
            driver.switch_to.context(contexts[0])
            self.slideUp()
            # driver.find_element_by_class_name('recharge').click()           #该代码会报‘不允许使用复合类名称’的错误，但实际看源码并不是复合类，该问题待之后查找
            driver.tap([(235,408)])
            time.sleep(5)
            if i == 0:
                driver.get_screenshot_as_file('/Users/apple/AppiumTestPng/recharge4.png')   #充值流程的第一个页面截图
            elif i == 1:
                driver.get_screenshot_as_file('/Users/apple/AppiumTestPng/recharge9.png')
            elif i == 2:
                driver.get_screenshot_as_file('/Users/apple/AppiumTestPng/recharge14.png')
            elif i == 3:
                driver.get_screenshot_as_file('/Users/apple/AppiumTestPng/recharge19.png')
            else:
                print '第一个页面截图时，出现程序异常，请注意'

            driver.switch_to.context(contexts[1])
            driver.find_elements_by_class_name('em-ico')[0].click()       #元素不唯一，可以用复数定位，把所有的相同元素定位出来，按下标取第几个就行
            driver.switch_to.context(contexts[0])
            driver.tap([(226,478)])
            driver.switch_to.context(contexts[1])
            # b = driver.find_element_by_class_name('lipa_input_box')   #注意，该元素虽然可以被选中，但是不能被点击，会报'ElementNotVisibleException'异常，即元素不可点击
            b = driver.find_element_by_id('inputEmail')                #以上不能点击的问题通过ActionChains这个类来解决，该类基本满足所有对鼠标操作的需求
            ActionChains(driver).click(b).perform()
            b.clear()
            ActionChains(driver).send_keys('893026750@qq.com').perform()
            c = driver.find_element_by_id('lipaBtnBox')
            ActionChains(driver).click(c).perform()
            driver.switch_to.context(contexts[0])
            if i == 0:
                driver.get_screenshot_as_file('/Users/apple/AppiumTestPng/recharge5.png')        #充值流程的第二个页面的截图
            elif i == 1:
                driver.get_screenshot_as_file('/Users/apple/AppiumTestPng/recharge10.png')
            elif i == 2:
                driver.get_screenshot_as_file('/Users/apple/AppiumTestPng/recharge15.png')
            elif i == 3:
                driver.get_screenshot_as_file('/Users/apple/AppiumTestPng/recharge20.png')
            else:
                print '第二个页面截图时，出现程序异常，请注意'
            time.sleep(8)

            driver.switch_to.context(contexts[1])
            driver.find_element_by_xpath("//*[@placeholder='0000 0000 0000 0000']").send_keys('4084084084084081')
            driver.find_element_by_xpath("//*[@placeholder='MM / YY']").send_keys('0120')
            driver.find_element_by_xpath("//*[@placeholder='123']").send_keys('408')
            driver.find_element_by_id('pay-btn').click()
            driver.switch_to.context(contexts[0])
            time.sleep(3)
            if i == 0:
                driver.get_screenshot_as_file('/Users/apple/AppiumTestPng/recharge6.png')    #充值流程的第三个页面截图
            elif i == 1:
                driver.get_screenshot_as_file('/Users/apple/AppiumTestPng/recharge11.png')
            elif i == 2:
                driver.get_screenshot_as_file('/Users/apple/AppiumTestPng/recharge16.png')
            elif i == 3:
                driver.get_screenshot_as_file('/Users/apple/AppiumTestPng/recharge21.png')
            else:
                print '第三个页面截图时，出现程序异常，请注意'
            time.sleep(3)
            if i == 0:
                driver.get_screenshot_as_file('/Users/apple/AppiumTestPng/recharge7.png')    #充值流程的第四个页面，充值流程结束页面
            elif i == 1:
                driver.get_screenshot_as_file('/Users/apple/AppiumTestPng/recharge12.png')
            elif i == 2:
                driver.get_screenshot_as_file('/Users/apple/AppiumTestPng/recharge17.png')
            elif i == 3:
                driver.get_screenshot_as_file('/Users/apple/AppiumTestPng/recharge22.png')
            else:
                print '第四个页面截图时，出现程序异常，请注意'
            driver.tap([(235,440)])
            # driver.find_element_by_css_selector('a')        #该异常是由于python selenium包的一个错误，可以通过降级版本来解决，将版本降级到Appium-Python-Client == 0.14和Selenium == 2.45.0
            # driver.find_element_by_tag_name('a')         #该定位方式以及by_css、by_link_text等方式时会报不支持该会话，错误的定位器策略异常
            time.sleep(2)
            if i == 0:
                driver.get_screenshot_as_file('/Users/apple/AppiumTestPng/recharge8.png')    #充值完成后跳转回充值页面的截图，第五个截图
            elif i == 1:
                driver.get_screenshot_as_file('/Users/apple/AppiumTestPng/recharge13.png')
            elif i == 2:
                driver.get_screenshot_as_file('/Users/apple/AppiumTestPng/recharge18.png')
            elif i == 3:
                driver.get_screenshot_as_file('/Users/apple/AppiumTestPng/recharge23.png')
            else:
                print '第五个页面截图时，出现程序异常，请注意'

        driver.switch_to.context(contexts[1])
        time.sleep(3)
        driver.find_element_by_class_name('records').click()
        time.sleep(3)
        driver.switch_to.context(contexts[0])
        driver.get_screenshot_as_file('/Users/apple/AppiumTestPng/recharge24.png')       #用户充值后查看充值记录

        driver.find_element_by_id('title_bar_iv_left').click()
        driver.switch_to.context(contexts[1])
        # y = driver.find_element_by_xpath("//*[@placeholder='point']")
        y = driver.find_element_by_css_selector("[placeholder='point']")
        y.send_keys('0')
        driver.switch_to.context(contexts[0])
        self.slideUp()
        driver.tap([(235,408)])
        time.sleep(2)
        driver.get_screenshot_as_file('/Users/apple/AppiumTestPng/recharge25.png')      #输入的金币数量为0

        driver.switch_to.context(contexts[1])
        y.clear()
        y.send_keys('9.9')
        time.sleep(2)
        driver.switch_to.context(contexts[0])
        driver.get_screenshot_as_file('/Users/apple/AppiumTestPng/recharge26.png')      #输入的金币数量为小数

        driver.switch_to.context(contexts[1])
        y.clear()
        y.send_keys('9@qq')
        driver.switch_to.context(contexts[0])
        self.slideUp()
        driver.tap([(235,408)])
        time.sleep(2)
        driver.get_screenshot_as_file('/Users/apple/AppiumTestPng/recharge27.png')      #输入的金币数量为特殊字符

        driver.switch_to.context(contexts[1])
        y.clear()
        y.send_keys('9')
        driver.switch_to.context(contexts[0])
        self.slideUp()
        driver.tap([(235,408)])
        time.sleep(2)
        driver.get_screenshot_as_file('/Users/apple/AppiumTestPng/recharge28.png')      #输入的金币数量值小于10

        driver.switch_to.context(contexts[1])
        current_window1 = driver.window_handles[0]
        print current_window1                                                #充值流程第一个页面的窗口
        y.clear()
        y.send_keys('10')
        driver.switch_to.context(contexts[0])
        self.slideUp()
        driver.get_screenshot_as_file('/Users/apple/AppiumTestPng/recharge29.png')      #输入的金币数量值为10,未点击之前截图
        driver.tap([(235,408)])
        time.sleep(5)
        driver.get_screenshot_as_file('/Users/apple/AppiumTestPng/recharge30.png')      #输入的金币数量值为10，点击后截图

        driver.find_element_by_id('title_bar_iv_left').click()
        driver.press_keycode(4)                                 #按手机上的返回键
        driver.find_element_by_id('tv_recharge').click()
        time.sleep(3)
        driver.tap([(192,566)])
        driver.press_keycode(8)
        time.sleep(1)                                           #注意这段休眠很重要，不然可能输入的结果只有1，而不是11.
        driver.press_keycode(8)
        self.slideUp()
        driver.get_screenshot_as_file('/Users/apple/AppiumTestPng/recharge31.png')  # 输入的金币数量值为11,未点击之前截图
        driver.tap([(235, 408)])
        time.sleep(3)
        driver.get_screenshot_as_file('/Users/apple/AppiumTestPng/recharge32.png')  # 输入的金币数量值为11，点击后截图

        driver.press_keycode(4)
        driver.find_element_by_id('tv_recharge').click()
        time.sleep(3)
        driver.tap([(192,566)])
        time.sleep(2)
        driver.press_keycode(8)
        driver.press_keycode(7)
        driver.press_keycode(7)
        driver.press_keycode(8)
        self.slideUp()
        driver.get_screenshot_as_file('/Users/apple/AppiumTestPng/recharge33.png')  # 输入的金币数量值为1001,未点击之前截图
        driver.tap([(235, 408)])
        time.sleep(3)
        driver.get_screenshot_as_file('/Users/apple/AppiumTestPng/recharge34.png')  # 输入的金币数量值为1001，点击后截图

        driver.press_keycode(4)                                 #按手机上的返回键
        driver.find_element_by_id('tv_recharge').click()
        time.sleep(3)
        driver.tap([(192,566)])
        time.sleep(2)
        driver.press_keycode(9)
        time.sleep(2)
        driver.press_keycode(12)
        self.slideUp()
        driver.get_screenshot_as_file('/Users/apple/AppiumTestPng/recharge35.png')  # 输入的金币数量值为25正常值,未点击之前截图
        time.sleep(3)
        driver.tap([(235, 408)])
        driver.get_screenshot_as_file('/Users/apple/AppiumTestPng/recharge36.png')  # 输入的金币数量值为25正常值，点击后截图
        time.sleep(3)
        driver.tap([(414, 481)])
        time.sleep(2)
        driver.tap([(157, 483)])
        time.sleep(2)
        driver.tap([(255, 541)])
        time.sleep(2)
        driver.keyevent(123)             # 该方法将光标移到最后
        for i in range(0, 20):
            driver.keyevent(67)
        s1 = "adb shell input text '893026750'"
        s2 = "adb shell input keyevent KEYCODE_AT"
        s3 = "adb shell input text 'qq.com'"
        os.system(s1)
        os.system(s2)
        os.system(s3)
        driver.tap([(231,641)])
        time.sleep(15)
        driver.get_screenshot_as_file('/Users/apple/AppiumTestPng/recharge37.png')
        driver.tap([(157,368)])
        s4 = "adb shell input text '4084084084084081'"
        os.system(s4)
        time.sleep(3)
        driver.tap([(112,468)])
        s5 = "adb shell input text '0120'"
        os.system(s5)
        driver.tap([(325,463)])
        s6 = "adb shell input text '408'"
        os.system(s6)
        driver.tap([(229,558)])
        time.sleep(8)
        driver.get_screenshot_as_file('/Users/apple/AppiumTestPng/recharge38.png')
        driver.tap([(235,440)])
        time.sleep(2)
        driver.get_screenshot_as_file('/Users/apple/AppiumTestPng/recharge39.png')
        print '充值功能测试完成'

        #adb shell命令，待之后可用
        # package_name = "adb shell pm list package"
        # terminal_back = os.popen(package_name)  # 查询出android设备中已经安装的所有应用包名（包括系统应用和用户应用），并获得返回值（返回值是一个文件对象，格式为fd）
        # terminal_result = str(terminal_back.read())  # 读取所返回的文件对象内容，并转换为string类型
        # print terminal_result
        # f_result = terminal_result.find("com.football.supergoal")  # find函数找不到时返回-1，找到了则返回查找到字符串的第一个出现的位置
        # print f_result
        # os.system("adb shell am force-stop com.football.supergoal")    #杀掉该进程，再启动APP

        #以下代码待之后解决，这个noSuchWindowException异常需研究怎么解决
        # all_windows = driver.window_handles
        # current_window2 = all_windows[0]
        # print current_window2
        # for i in all_windows:
        #     if current_window2 != i:
        #         print 'y'
        #         driver.switch_to.window(current_window2)          该行代码执行时会报没有这个窗口的异常，研究从这里开始
        #         print 'y'
        #         y.send_keys('11')
        #         print 'y'
        #     else:
        #         driver = driver.switch_to.window(current_window2)
        # y.send_keys('11')
        # print 'y'
        # driver.switch_to.context(contexts[0])
        # self.slideUp()
        # driver.get_screenshot_as_file('/Users/apple/AppiumTestPng/recharge31.png')  # 输入的金币数量值为11,未点击之前截图
        # driver.tap([(235, 408)])
        # time.sleep(3)
        # driver.get_screenshot_as_file('/Users/apple/AppiumTestPng/recharge32.png')  # 输入的金币数量值为11，点击后截图
        #
        # driver.find_element_by_id('title_bar_iv_left').click()
        # driver.find_element_by_id('tv_recharge').click()
        # driver.switch_to.context(contexts[1])
        # y.send_keys('1001')
        # driver.switch_to.context(contexts[0])
        # self.slideUp()
        # driver.get_screenshot_as_file('/Users/apple/AppiumTestPng/recharge33.png')  # 输入的金币数量值为1001,未点击之前截图
        # driver.tap([(235, 408)])
        # time.sleep(3)
        # driver.get_screenshot_as_file('/Users/apple/AppiumTestPng/recharge34.png')  # 输入的金币数量值为1001，点击后截图

    #竞猜功能
    def test_prediction(self):
        driver = self.driver
        driver.find_element_by_id('rb_prediction').click()
        time.sleep(3)
        driver.find_element_by_id('tv_prediction_records').click()
        time.sleep(3)
        driver.get_screenshot_as_file('/Users/apple/AppiumTestPng/prediction1.png')
        driver.find_element_by_id('title_bar_iv_left').click()

    #订阅功能
    def test_subscribe(self):
        driver = self.driver
        uid = self.test_feedback()
        conn,cur = connDB()
        delete_subscription(conn,cur,uid)
        driver.find_element_by_id('title_bar_iv_left').click()
        driver.tap([(339,571)])
        for i in range(2):
            driver.find_element_by_id('rb_match').click()
            time.sleep(2)
            s1 = "adb shell am force-stop com.football.supergoal"
            os.system(s1)
            start_p = 'com.football.supergoal'
            start_a = 'com.soka.football.home.ui.login.activity.SplashActivity'
            driver.start_activity(start_p, start_a)
        driver.find_element_by_id('rb_match').click()
        time.sleep(2)
        driver.get_screenshot_as_file('/Users/apple/AppiumTestPng/subscribe1.png')   #用户第一次打开match页面时展示subscribe页面的截图

        driver.find_element_by_xpath("//*[(@index='6' and @class='android.widget.RelativeLayout')]").click()
        driver.find_element_by_xpath("//*[(@index='11' and @class='android.widget.RelativeLayout')]").click()
        driver.find_element_by_xpath("//*[(@text='La Liga')]").click()
        time.sleep(1)
        driver.find_element_by_xpath("//*[(@index='2' and @class='android.widget.RelativeLayout')]").click()
        driver.find_element_by_xpath("//*[(@index='8' and @class='android.widget.RelativeLayout')]").click()
        driver.find_element_by_id('title_bar_tv_right').click()
        time.sleep(1)
        driver.find_element_by_xpath("//*[(@index='0' and @text='Subscribe')]").click()
        time.sleep(2)
        driver.get_screenshot_as_file('/Users/apple/AppiumTestPng/subscribe2.png')          #用户从match页面进入然后再订阅球队

        result = select_subscribption(cur, uid)                                         #从数据库中查看该用户订阅球队的比赛总共有多少个（比赛开始时间大于现在的）
        e = len(result)
        s1 = []
        b = []
        for i in range(e):
            s2 = result[i][0]
            s1.append(s2)
        print s1

        for m in range(len(s1)):                                        #循环出每个用户订阅的球队
            a = select_match_subcribption(cur, s1[m])
            for n in range(len(a)):                                         #循环出每个球队的比赛
                b.append(a[n][1])                                           #将每个比赛的matchId添加到一个列表中
        # d =Counter(a1)                                        #显示出列表中所有元素重复的次数，返回值是一个字典，注意要导入Counter包
        c = list(set(b))                                       # 去除列表中重复的元素
        s3 = len(c)
        print s3
        s4 = match_reptile()                                                                #接口返回的用户订阅球队比赛数量
        if s4 == s3:
            print '接口返回的数据与数据库查询出的结果相同，用户订阅球队比赛显示的数量没有问题'
        else:
            print '注意!数据不同，请核对'

        #刷新与定位到当前日期比赛的按钮测试
        for i in range(5):
            driver.find_element_by_id('iv_locate').click()
            time.sleep(1)
            if i == 0:
                driver.get_screenshot_as_file('/Users/apple/AppiumTestPng/subscribe3.png')        #点击定位按钮后截图
            elif i == 1:
                driver.get_screenshot_as_file('/Users/apple/AppiumTestPng/subscribe4.png')
            elif i == 2:
                driver.get_screenshot_as_file('/Users/apple/AppiumTestPng/subscribe5.png')
            elif i == 3:
                driver.get_screenshot_as_file('/Users/apple/AppiumTestPng/subscribe6.png')
            elif i == 4:
                driver.get_screenshot_as_file('/Users/apple/AppiumTestPng/subscribe7.png')
            else:
                print '循环出错，请核对之'
        for i in range(5):
            self.slideDown()
            time.sleep(2)
            if i == 0:
                driver.get_screenshot_as_file('/Users/apple/AppiumTestPng/subscribe8.png')        #下拉刷新拉出所订阅的球队历史比赛的截图
            elif i == 1:
                driver.get_screenshot_as_file('/Users/apple/AppiumTestPng/subscribe9.png')
            elif i == 2:
                driver.get_screenshot_as_file('/Users/apple/AppiumTestPng/subscribe10.png')
            elif i == 3:
                driver.get_screenshot_as_file('/Users/apple/AppiumTestPng/subscribe11.png')
            elif i == 4:
                driver.get_screenshot_as_file('/Users/apple/AppiumTestPng/subscribe12.png')
            else:
                print '循环出错，请核对之'


        delete_subscription(conn,cur,uid)
        driver.find_element_by_id('title_bar_iv_left').click()
        driver.find_element_by_id('tv_subscribed').click()
        time.sleep(1)
        driver.get_screenshot_as_file('/Users/apple/AppiumTestPng/subscribe13.png')          #用户未订阅时的订阅页面显示截图
        # driver.find_element_by_id('tv_subscribe').click()
        # time.sleep(2)
        # driver.get_screenshot_as_file('/Users/apple/AppiumTestPng/subscribe14.png')     #由subscribe按钮进入订阅比赛页面
        # driver.find_element_by_id('title_bar_iv_left').click()
        driver.find_element_by_id('title_bar_tv_right').click()
        time.sleep(2)
        driver.get_screenshot_as_file('/Users/apple/AppiumTestPng/subscribe15.png')     #由add more按钮进入订阅比赛页面
        driver.find_element_by_xpath("//*[(@index='5' and @class='android.widget.RelativeLayout')]").click()
        driver.find_element_by_xpath("//*[(@index='10' and @class='android.widget.RelativeLayout')]").click()
        driver.get_screenshot_as_file('/Users/apple/AppiumTestPng/subscribe16.png')      #用户订阅EPL球队的截图

        driver.find_element_by_xpath("//*[(@text='La Liga')]").click()
        time.sleep(1)
        driver.find_element_by_xpath("//*[(@index='3' and @class='android.widget.RelativeLayout')]").click()
        driver.find_element_by_xpath("//*[(@index='11' and @class='android.widget.RelativeLayout')]").click()
        driver.get_screenshot_as_file('/Users/apple/AppiumTestPng/subscribe17.png')      #用户订阅LaLiga球队的截图

        driver.find_element_by_xpath("//*[(@text='Bundesliga')]").click()
        # time.sleep(1)
        self.slideUp()
        time.sleep(1)
        driver.find_element_by_xpath("//*[(@index='9' and @class='android.widget.RelativeLayout')]").click()
        driver.find_element_by_xpath("//*[(@index='13' and @class='android.widget.RelativeLayout')]").click()
        driver.get_screenshot_as_file('/Users/apple/AppiumTestPng/subscribe18.png')     # 用户订阅Bundesliga球队的截图

        driver.find_element_by_xpath("//*[(@text='Ligue 1')]").click()
        time.sleep(1)
        driver.find_element_by_xpath("//*[(@index='0' and @class='android.widget.RelativeLayout')]").click()
        driver.find_element_by_xpath("//*[(@index='15' and @class='android.widget.RelativeLayout')]").click()
        driver.get_screenshot_as_file('/Users/apple/AppiumTestPng/subscribe19.png')      #用户订阅Ligue 1球队的截图

        driver.find_element_by_xpath("//*[(@text='serie A')]").click()
        time.sleep(1)
        driver.find_element_by_xpath("//*[(@index='14' and @class='android.widget.RelativeLayout')]").click()
        driver.find_element_by_xpath("//*[(@index='6' and @class='android.widget.RelativeLayout')]").click()
        driver.get_screenshot_as_file('/Users/apple/AppiumTestPng/subscribe20.png')      # 用户订阅serie A球队的截图
        driver.find_element_by_id('title_bar_tv_right').click()
        time.sleep(2)
        driver.get_screenshot_as_file('/Users/apple/AppiumTestPng/subscribe21.png')      # 用户订阅球队后的截图
        self.slideUp()
        driver.get_screenshot_as_file('/Users/apple/AppiumTestPng/subscribe22.png')      #滑动屏幕后查看是否总共有10个球队

        a = driver.find_elements_by_id('tv_subscribed')
        a[6].click()
        time.sleep(1)
        driver.get_screenshot_as_file('/Users/apple/AppiumTestPng/subscribe23.png')      #由subscribed按钮取消订阅球队的截图
        driver.find_element_by_id('tv_cancel').click()
        time.sleep(1)
        driver.get_screenshot_as_file('/Users/apple/AppiumTestPng/subscribe24.png')      #操作取消后的页面截图
        a[6].click()
        driver.find_element_by_id('tv_unsub').click()
        time.sleep(2)
        driver.get_screenshot_as_file('/Users/apple/AppiumTestPng/subscribe25.png')      #取消订阅某个球队后的页面截图

        # 由add more按钮取消订阅球队
        driver.find_element_by_id('title_bar_tv_right').click()
        driver.find_element_by_xpath("//*[(@text='La Liga')]").click()
        time.sleep(1)
        driver.find_element_by_xpath("//*[(@index='3' and @class='android.widget.RelativeLayout')]").click()
        driver.find_element_by_xpath("//*[(@index='11' and @class='android.widget.RelativeLayout')]").click()
        driver.find_element_by_xpath("//*[(@text='Bundesliga')]").click()
        # time.sleep(1)
        self.slideUp()
        time.sleep(1)
        driver.find_element_by_xpath("//*[(@index='9' and @class='android.widget.RelativeLayout')]").click()
        driver.find_element_by_xpath("//*[(@index='13' and @class='android.widget.RelativeLayout')]").click()
        driver.find_element_by_xpath("//*[(@text='Ligue 1')]").click()
        time.sleep(1)
        driver.find_element_by_xpath("//*[(@index='0' and @class='android.widget.RelativeLayout')]").click()
        driver.find_element_by_xpath("//*[(@index='15' and @class='android.widget.RelativeLayout')]").click()
        driver.find_element_by_id('title_bar_tv_right').click()
        time.sleep(2)
        driver.get_screenshot_as_file('/Users/apple/AppiumTestPng/subscribe26.png')    #由add more按钮取消订阅球队后的截图,只留下LPL和serie A的球队

        driver.find_element_by_id('title_bar_iv_left').click()
        time.sleep(1)
        driver.tap([(339,571)])
        driver.find_element_by_id('rb_match').click()
        driver.find_element_by_xpath("//*[(@index='0' and @text='Subscribe')]").click()
        time.sleep(1)
        driver.get_screenshot_as_file('/Users/apple/AppiumTestPng/subscribe27.png')    #通过match进入subscribe页面，显示用户取消订阅球队是否成功的截图

        result = select_subscribption(cur, uid)  # 从数据库中查看该用户订阅球队的比赛总共有多少个（比赛开始时间大于现在的）
        e = len(result)
        s5 = []
        b = []
        for i in range(e):
            s6 = result[i][0]
            s5.append(s6)
        print s5

        for m in range(len(s5)):  # 循环出每个用户订阅的球队
            a = select_match_subcribption(cur, s5[m])
            for n in range(len(a)):  # 循环出每个球队的比赛
                b.append(a[n][1])  # 将每个比赛的matchId添加到一个列表中
        # d =Counter(a1)                                        #显示出列表中所有元素重复的次数，返回值是一个字典，注意要导入Counter包
        c = list(set(b))  # 去除列表中重复的元素
        s7 = len(c)
        print s7
        s8 = match_reptile()  # 接口返回的用户订阅球队比赛数量
        if s8 == s7:
            print '接口返回的数据与数据库查询出的结果相同，用户订阅球队比赛显示的数量没有问题'
        else:
            print '注意!数据不同，请核对'
        print '订阅功能测试结束'


     #新闻页面

    #新闻页面
    def test_new(self):
        self.test_teach()
        driver = self.driver
        time.sleep(2)
        driver.find_element_by_id("rb_news").click()
        time.sleep(5)
        driver.find_elements_by_id("tv_title")[3].click()
        time.sleep(5)
        driver.get_screenshot_as_file("/Users/apple/AppiumTestPng/news_normal_w.png")  #正常点击
        time.sleep(1)
        driver.find_element_by_id("tv_cancel").click()
        driver.find_element_by_id("title_bar_iv_left").click()
        time.sleep(1)

        self.slideDown()
        time.sleep(8)
        driver.get_screenshot_as_file("/Users/apple/AppiumTestPng/news_slideDown1_w.png")  #下拉刷新
        time.sleep(2)
        driver.find_elements_by_id("tv_title")[3].click()
        time.sleep(5)
        driver.get_screenshot_as_file("/Users/apple/AppiumTestPng/news_slideDown2_w.png")  # 下拉刷新后点击
        driver.find_element_by_id("title_bar_iv_left").click()
        time.sleep(1)


        self.slideUp()
        time.sleep(2)
        driver.get_screenshot_as_file("/Users/apple/AppiumTestPng/news_slideUp1_w.png")  #屏幕向上滑
        time.sleep(1)
        driver.find_elements_by_id("tv_title")[3].click()
        time.sleep(4)
        driver.get_screenshot_as_file("/Users/apple/AppiumTestPng/news_slideUp2_w.png")  # 滑动后点击
        driver.find_element_by_id("title_bar_iv_left").click()
        time.sleep(2)


        for i in range(7):
            self.slideUp()
            time.sleep(1)
        time.sleep(2)
        driver.get_screenshot_as_file("/Users/apple/AppiumTestPng/news_slideUp3_w.png")  #上拉刷新
        time.sleep(1)
        driver.find_elements_by_id("tv_title")[3].click()
        time.sleep(4)
        driver.get_screenshot_as_file("/Users/apple/AppiumTestPng/news_slideUp4_w.png")  #上拉刷新后点击

    #video页面之banner区域，遗留一个点击新增的banner然后截图问题！
    def test_videoBanner(self):
        self.test_teach()
        driver = self.driver
        time.sleep(5)
        driver.find_element_by_id("tv_banner_title").click()
        time.sleep(5)
        driver.get_screenshot_as_file("/Users/apple/AppiumTestPng/banner_article_w.png") #banner文章
        driver.find_element_by_id("tv_cancel").click()
        driver.find_element_by_id("title_bar_iv_left").click()

        time.sleep(3)
        self.slideLeft()
        driver.find_element_by_id("tv_banner_title").click()
        time.sleep(5)
        driver.get_screenshot_as_file("/Users/apple/AppiumTestPng/banner_match_w.png")  #banner比赛
        driver.find_element_by_id("title_bar_iv_left").click()

        time.sleep(4)
        self.slideLeft()
        driver.find_element_by_id("tv_banner_title").click()
        time.sleep(5)
        driver.get_screenshot_as_file("/Users/apple/AppiumTestPng/banner_video_w.png")  #banner视频
        driver.find_element_by_id("iv_back").click()

        # 新增一个banner文章
        delivery_url = "http://api.admin.test.sokafootball.com/admin/banner/update"
        values = {"id": 33, "status": 0}
        delivery_data = json.dumps(values)
        delivery_headers = {"Content-Type": "application/json"}
        requests.post(url=delivery_url, data=delivery_data, headers=delivery_headers)  #调用缓存post接口
        time.sleep(5)
        print ("新增文章接口调用成功")
        self.slideDown()
        time.sleep(5)
        driver.get_screenshot_as_file("/Users/apple/AppiumTestPng/banner_newly1_w.png")
        driver.find_element_by_id("tv_banner_title").click()
        time.sleep(5)
        driver.get_screenshot_as_file("/Users/apple/AppiumTestPng/banner_newlyArticle_w.png")
        driver.find_element_by_id("title_bar_iv_left").click()

        # 新增一个banner比赛，#新增的比赛，是否正确点击到所新增的比赛

        delivery_url = "http://api.admin.test.sokafootball.com/admin/banner/update"
        values = {"id": 36, "status": 0}
        delivery_data = json.dumps(values)
        delivery_headers = {"Content-Type": "application/json"}
        requests.post(url=delivery_url, data=delivery_data, headers=delivery_headers)  #调用缓存post接口
        time.sleep(5)
        print ("新增比赛接口调用成功")
        self.slideDown()
        time.sleep(5)
        driver.get_screenshot_as_file("/Users/apple/AppiumTestPng/banner_newly2_w.png")
        driver.find_element_by_id("tv_banner_title").click()
        time.sleep(5)
        driver.get_screenshot_as_file("/Users/apple/AppiumTestPng/banner_newlyMatch_w.png")
        driver.find_element_by_id("title_bar_iv_left").click()

        #下线一个banner
        delivery_url = "http://api.admin.test.sokafootball.com/admin/banner/update"
        values_list = [36,33,34,40,39]
        for id in values_list:
            try:
                values = {"id": id, "status": 1}
                delivery_data = json.dumps(values)
                delivery_headers = {"Content-Type": "application/json"}
                requests.post(url=delivery_url, data=delivery_data, headers=delivery_headers)

                time.sleep(5)
                self.slideDown()
                time.sleep(5)
                if id == 36:
                    driver.get_screenshot_as_file("/Users/apple/AppiumTestPng/banner_offline1_w.png")
                elif id == 33:
                    driver.get_screenshot_as_file("/Users/apple/AppiumTestPng/banner_offline2_w.png")
                elif id == 34:
                    driver.get_screenshot_as_file("/Users/apple/AppiumTestPng/banner_offline3_w.png")
                elif id == 40:
                    driver.get_screenshot_as_file("/Users/apple/AppiumTestPng/banner_offline4_w.png")
                elif id == 39:
                    driver.get_screenshot_as_file("/Users/apple/AppiumTestPng/banner_offline5_w.png")
                else:
                    print ("banner list异常，请查看之")
            except IndentationError,e:
                traceback.print_exc()
                print "所要下线的banner中有某个已下线，请查看之"
            else:
                print ("下线" + str(id) + "号banner成功")


        # update_banner1(conn, cur, 33,1)  # 需要在控制台弹出来这个1，弹出框怎么显示需要学习下

    #video页面之match区域
    def test_videoMatch(self):
        self.test_teach()
        driver = self.driver
        conn, cur = connDB()
        r = show_matchIndex(cur)
        match_mes = r[0]
        print 'A队名称:', match_mes[0], '   B队名称:', match_mes[1], '   联盟名称:', match_mes[2], '   比赛开始时间:', match_mes[3]
        status = r[1]
        if status == 1:
            time.sleep(4)
            driver.get_screenshot_as_file("/Users/apple/AppiumTestPng/video_matchShow1_w.png")

            #注意：这里只是一部分，之后还需要根据比赛状态来进行点击查看。如这里只是一场比赛还未开始时的页面显示情况，
            # 还有比赛结束后（有数据和无数据）、比赛过程中等情况的页面显示情况
            driver.find_element_by_id("tv_time").click()    #主页显示的比赛详细信息，其页面显示情况。
            time.sleep(5)
            driver.get_screenshot_as_file("/Users/apple/AppiumTestPng/video_matchLive1_w.png")

            driver.find_element_by_android_uiautomator('new UiSelector().text("Prediction")').click()
            time.sleep(5)
            driver.get_screenshot_as_file("/Users/apple/AppiumTestPng/video_matchPre_w.png")

            driver.find_element_by_android_uiautomator('new UiSelector().text("Overview")').click()
            time.sleep(5)
            driver.get_screenshot_as_file("/Users/apple/AppiumTestPng/video_matchOver_w.png")

            driver.find_element_by_android_uiautomator('new UiSelector().text("Line-up")').click()
            time.sleep(5)
            driver.get_screenshot_as_file("/Users/apple/AppiumTestPng/video_matchLine_w.png")

            driver.find_element_by_android_uiautomator('new UiSelector().text("Statistics")').click()
            time.sleep(5)
            driver.get_screenshot_as_file("/Users/apple/AppiumTestPng/video_matchSta_w.png")

            driver.find_element_by_android_uiautomator('new UiSelector().text("Live")').click()
            time.sleep(5)
            driver.get_screenshot_as_file("/Users/apple/AppiumTestPng/video_matchLive2_w.png")
            driver.find_element_by_id("title_bar_iv_left")

            #更改主页显示比赛的状态

            update_matchIndex(conn, cur, status)
            time.sleep(5)

            self.slideDown()
            time.sleep(5)
            driver.get_screenshot_as_file("/Users/apple/AppiumTestPng/video_matchShow2_w.png")
            print ("截图完毕，请查看之")

        elif status == 0:
            time.sleep(4)
            driver.get_screenshot_as_file("/Users/apple/AppiumTestPng/video_matchShow2_w.png")

            # 更改主页显示比赛的状态
            update_matchIndex(conn, cur, status)
            time.sleep(5)

            self.slideDown()
            time.sleep(5)
            driver.get_screenshot_as_file("/Users/apple/AppiumTestPng/video_matchShow1_w.png")

            driver.find_element_by_id("tv_time").click()
            time.sleep(5)
            driver.get_screenshot_as_file("/Users/apple/AppiumTestPng/video_matchLive1_w.png")

            driver.find_element_by_android_uiautomator('new UiSelector().text("Prediction")').click()
            time.sleep(5)
            driver.get_screenshot_as_file("/Users/apple/AppiumTestPng/video_matchPre_w.png")

            driver.find_element_by_android_uiautomator('new UiSelector().text("Overview")').click()
            time.sleep(5)
            driver.get_screenshot_as_file("/Users/apple/AppiumTestPng/video_matchOver_w.png")

            driver.find_element_by_android_uiautomator('new UiSelector().text("Line-up")').click()
            time.sleep(5)
            driver.get_screenshot_as_file("/Users/apple/AppiumTestPng/video_matchLine_w.png")

            driver.find_element_by_android_uiautomator('new UiSelector().text("Statistics")').click()
            time.sleep(5)
            driver.get_screenshot_as_file("/Users/apple/AppiumTestPng/video_matchSta_w.png")

            driver.find_element_by_android_uiautomator('new UiSelector().text("Live")').click()
            time.sleep(5)
            driver.get_screenshot_as_file("/Users/apple/AppiumTestPng/video_matchLive2_w.png")
            driver.find_element_by_id("title_bar_iv_left")
            print ("截图完毕，请查看之")

    #测试用例方法结束处


    def test_tearDown(self):
        self.driver.close_app()   #关闭当前的app应用窗口
        self.driver.quit()        #不仅关闭了当前的app应用窗口还彻底的退出WedDriver,释放了Driver与Server之间的链接，quit会更好的释放资源



    @unittest.skipIf(True,"I don't want to run this case ,and skip it")
    #unittest.skip是无条件跳过某个case的执行，该方法是condition为True时跳过，unittest.skipUnless是condition为False时跳过
    def test_skipFunction(self):
        print "hello python"


if __name__ == "__main__":
    # unittest.main()
    suite = unittest.TestSuite()    #可以将TestSuite看成是包含所有测试用例的一个容器
    testCase = [AutoTest("test_prediction"),AutoTest("test_tearDown"),AutoTest("test_skipFunction")]   #可以将TestCase看成是对特定类进行测试的方法的集合
    suite.addTests(testCase)  #将测试用例添加到TestSuite这个容器中


    unittest.TextTestRunner(verbosity=2).run(suite)  #TextTestRunner是用来执行测试用例的
    #其中的run(test)会执行TestSuite/TestCase中的run(result)方法，也就是说TestCase有个内置函数也叫run()方法


    # suite1 = unittest.TestLoader.loadTestsFromTestCase(AutoTest)
    #TestLoader是用来加载TestCase到TestSuite
    #loadTestsFromTestCase方法是从代码中每个地方去寻找TestCase，并创建它们的实例,将TestCase的实例add到TestSuiter中，再返回一个TestSuiter实例


