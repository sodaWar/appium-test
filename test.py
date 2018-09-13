# -* encoding:utf-8 *-
# from appium import webdriver
from  test_cm_upgrade import *
from  reptile_request_get import *
from receive_email import *
from Tkinter import *
import tkMessageBox
import time
from collections import Counter

print 10
# conn,cur = connDB()
# result = select_subscribption(cur,241)
# e = len(result)
# s1 = []
# b = []
# for i in range(e):
#     s2 = result[i][0]
#     s1.append(s2)
# print s1
#
# for m in range(len(s1)):
#     a = select_match_subcribption(cur, s1[m])
#     for n in range(len(a)):
#         b.append(a[n][1])
#         print b
#     # print a1
# # c =Counter(a1)                                        #显示出列表中所有元素重复的次数，返回值是一个字典，注意要导入Counter包
# s3 = list(set(b))                                      #去除列表中重复的元素
# print len(s3)
    # s3 = s3 + a
    # print s3


# def a():
#     conn, cur = connDB()
#     result = selectDBAuto(cur, 'identity', 'identity')
#     email = '830@qq.com'
#     # print result[0][0]
#     for i in range(0, len(result)):
#         a = str(i)
#         if (email == result[i][0]):
#             print "the email have existed:" + email
#             if len(email) == 10:
#                 email = email[:2] + a + email[3:]
#                 print email
#             elif len(email) == 11:
#                 email = email[:2] + a + email[4:]
#                 print email
#             elif len(email) == 12:
#                 email = email[:2] + a + email[5]
#                 print email
#     print ("the email is availabe:") + email
#     return email
# # print email
# b = a()
# print b

# import json
#
# values = {"id": 33,"status" : 0}
# delivery_data = json.dumps(values)
# delivery_url = "http://api.admin.test.sokafootball.com/admin/banner/update"
# delivery_headers = {"Content-Type" : "application/json"}
# r = requests.post(url = delivery_url,data = delivery_data,headers=delivery_headers)





# def printentry():            #弹出输入框并获取其值
#     print var.get()
# from Tkinter import *
# root=Tk()
# var=StringVar()
# Entry(root,textvariable=var).pack() #设置输入框对应的文本变量为var
# Button(root,text="print entry",command=printentry).pack()
# root.mainloop()

#
# from Tkinter import *
#
# from tkMessageBox import *
#
#
# def answer():
#     showerror("Answer", "Sorry, no answer available")       #弹出对话框的一种方式，用python内置函数Tkinter库来实现
#
#
# def callback():
#     if askyesno('Verify', 'Really quit?'):
#
#         showwarning('Yes', 'Not yet implemented')
#
#     else:
#
#         showinfo('No', 'Quit has been cancelled')
#
#
# Button(text='Quit', command=callback).pack(fill=X)
#
# Button(text='Answer', command=answer).pack(fill=X)
#
# mainloop()
#
# import easygui                 #弹出对话框的一种方式，用python第三方库来实现
# Yes_or_No = easygui.buttonbox("Yes of No?", choices = ['Yes','No'])
# print Yes_or_No




# def installApp(self):
#     if self.driver.is_app_installed("com.football.soccerbook") == 'True':
#         self.driver.remove_app("com.football.soccerbook")
#         self.driver.install_app("/Users/apple/sokafootball2.1.2.apk")
#     else:
#         self.driver.install_app("/Users/apple/sokafootball2.1.2.apk")
#
# desired_caps = {
#     'platformName': 'Android',
#     'deviceName': '192.168.56.101:5555',
#     'platformVersion': '4.4.4',
#     'app' : '/Users/apple/sokafootball2.1.2.apk',
#     # 'appPackage': 'com.football.soccerbook',
#     # 'appActivity': 'com.soka.football.home.ui.login.activity.SplashActivity',
#     'unicodeKeyboard': 'True',
#     'resetKeyboard': 'True'
# }
#
#
# driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', desired_caps)
# driver.start_activity("com.football.soccerbook","com.soka.football.home.ui.login.activity.SplashActivity")
# time.sleep(3)
#
# if driver.is_app_installed("com.football.soccerbook"):
#     driver.remove_app("com.football.soccerbook")
#     driver.install_app("/Users/apple/sokafootball2.1.2.apk")

#
# conn, cur = connDB()
# r = show_matchIndex(cur)
# status = r[1]
# match_mes = r[0]
# print 'A队名称:',match_mes[0],'   B队名称:',match_mes[1],'   联盟名称:',match_mes[2],'   比赛开始时间:',match_mes[3]
#
#
# def emailScreen(self):
#     conn, cur = connDB()
#     result = selectDBAuto(cur, 'identity', 'identity')
#     email = '893026750@qq.com'
#     print len(result)
#     for i in range(0, len(result)):
#         if (email == result[i][0]):
#             print "the email have existed:" + email
#             email = email[:8] + str(i + 1) + email[9:]
#     print ("the email is availabe:") + email
#     return email
# update_matchIndex(conn,cur,status)

# print isinstance(result1,int)
# uid = result1+1
#
# result2 = insert_permission(conn,cur,uid)
# print result2


# content = '893026751@qq.com'
# print len(result)
# for i in range(0, len(result)):
#     if (email == result[i][0]):
#         print "the email have existed:" + email
#         email = email[:8] + str(i + 1) + email[9:]
# print ("the email is availabe:") + email




# else:
#     driver.install_app("/Users/apple/sokafootball2.1.2.apk")


# print driver.is_app_installed("com.football.soccerbook")
# if driver.is_app_installed("com.football.soccerbook") == 'True':
    # driver.remove_app("com.football.soccerbook")
# else:
#


# driver.implicitly_wait(2)
# time.sleep(2000)

# driver.find_element_by_id("tv_standard").click()
# driver.find_element_by_id("title_bar_iv_left").click()
# driver.find_element_by_id("tv_myCoin").click()
# driver.find_element_by_id("tv_sign_in").click()
# driver.find_element_by_id("tv_task_name").click()
# driver.find_element_by_id("rb_match").click()
#
#
# time.sleep(3)
# # driver.swipe(240, 600, 240, 230,3000)
#
#
#
#
# window_size = driver.get_window_size()
# x = window_size['width']
# y = window_size['height']
# x1 = int(x * 0.5)
# y1 = int(y * 0.82)
# y2 = int(y * 0.31)
# driver.swipe(start_x = x1,start_y = y1,end_x = x1,end_y = y2,duration = 2000)
#
#
#
#
#查看并使用该代码的用法:
# WebDriverWait(dr, 30).until(lambda the_driver: the_driver.find_element_by_id('qsbk.app:id/tabPanel').is_displayed())