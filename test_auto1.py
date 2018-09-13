# -* encoding:utf-8 *-
from com.android.monkeyrunner import MonkeyRunner as mr
from com.android.monkeyrunner import MonkeyDevice as md
from com.android.monkeyrunner import MonkeyImage as mi
from com.android.monkeyrunner.easy import EasyMonkeyDevice as emd
from com.android.monkeyrunner.easy import By
#from test_cm_upgrade import *
import os
import traceback

device = mr.waitForConnection()
easy_device = emd(device)

def isAppExit():
    package_name = "adb shell pm list package"
    terminal_back = os.popen(package_name)  #查询出android设备中已经安装的所有应用包名（包括系统应用和用户应用），并获得返回值（返回值是一个文件对象，格式为fd）
    terminal_result = str(terminal_back.read())   #读取所返回的文件对象内容，并转换为string类型
    f_result = terminal_result.find("com.soka.football")  #find函数找不到时返回-1，找到了则返回查找到字符串的第一个出现的位置
    print f_result
    if not f_result == -1:
        print "app is exit"
        return 1
    else:
        print "app not exit"
        return 0


def isProcessExit():
    process_name = "adb shell dumpsys meminfo"
    terminal_back = os.popen(process_name)   #查询出android设备中系统的内存状况，其中包括进程的包名、PID等信息内容
    terminal_result = str(terminal_back.read())
    f_result = terminal_result.find("com.soka.football")
    print f_result
    if not f_result == -1:
        print "Soka Football app is run"
        return 1
    else:
        print "Soka Football app is not run"
        return 0


# def emailScreen():
#     conn, cur = connDB()
#     result = selectDBAuto(cur)
#     email = '893026751@qq.com'
#     print len(result)
#     for i in range(0, len(result)):
#         if (email == result[i][0]):
#             print "the email have existed:" + email
#             email = email[:8] + str(i + 1) + email[9:]
#     print ("the email is availabe:") + email
#     return email



def startActivity(time=[0]):
    package_name = "com.football.soccerbook"
    activity = "com.soka.football.home.ui.login.activity.SplashActivity"
    comment_name = package_name + '/' + activity
    device.startActivity(component=comment_name)

    new_time = time[0] + 1      #该段代码主要是为了检测是否是第一次打开APP，因此要返回运行该程序的次数
    time[0] = new_time
    print time[0]
    mr.sleep(1)
    auto_teach(new_time)

    return new_time


def auto_register():
    runStartApp()
    mr.sleep(2)

    #email = emailScreen()
    password = "12345"

    easy_device.touch(By.id('id/iv_avatar'), md.DOWN_AND_UP)
    mr.sleep(1)
    device.drag((1272, 1002), (249, 1105), 3, 10)
    mr.sleep(1)
    easy_device.touch(By.id('id/et_email'), md.DOWN_AND_UP)
    #device.type(email)
    mr.sleep(3)
    device.touch(136, 594, 'DOWN_AND_UP')
    device.type(password)
    mr.sleep(1)
    easy_device.touch(By.id('id/et_confirm_password'), md.DOWN_AND_UP)
    device.type(password)
    mr.sleep(2)
    easy_device.touch(By.id('id/btn_sign'), md.DOWN_AND_UP)
    mr.sleep(1)

    image = device.takeSnapshot()
    mr.sleep(2)
    image.writeToFile('/Users/apple/auto_test/AutoImage/RegisterN1.png', 'png')
    result = mr.loadImageFromFile('/Users/apple/auto_test/AutoImage/test1.png', 'png')
    if image.sameAs(result, 1):
        print ("register user is  match right")
    else:
        print ("the register function have problem!!")




#
# def runRegister():
#     auto_register()


def auto_login(i):
    runStartApp()

    mr.sleep(2)
    easy_device.touch(By.id('id/iv_avatar'), md.DOWN_AND_UP)
    mr.sleep(1)

    if i == 0:         #邮箱只输入字母
        easy_device.touch(By.id('id/et_email'), md.DOWN_AND_UP)
        mr.sleep(1)
        device.type('abddsaqqcom')
        mr.sleep(1)
        easy_device.touch(By.id('id/et_password'), md.DOWN_AND_UP)

        image = device.takeSnapshot()
        mr.sleep(2)
        image.writeToFile('/Users/apple/auto_test/AutoImage/OnlyLetter1.png', 'png')
        result = mr.loadImageFromFile('/Users/apple/auto_test/AutoImage/OnlyLetter.png', 'png')
        if image.sameAs(result, 1):
            print ("input only letter match right")
        else:
            print ("there is a problem here,please check , and the number is:" + str(i))

    elif i == 1:     #邮箱只输入数字
        easy_device.touch(By.id('id/et_email'), md.DOWN_AND_UP)
        mr.sleep(1)
        device.type('89302675023')
        mr.sleep(1)
        easy_device.touch(By.id('id/et_password'), md.DOWN_AND_UP)

        image = device.takeSnapshot()
        mr.sleep(2)
        image.writeToFile('/Users/apple/auto_test/AutoImage/OnlyNumber1.png', 'png')
        result = mr.loadImageFromFile('/Users/apple/auto_test/AutoImage/OnlyNumber.png', 'png')
        if image.sameAs(result, 1):
            print ("input only number match right")
        else:
            print ("there is a problem here,please check , and the number is:" + str(i))

    elif i == 2:    #邮箱输入首部为空格
        easy_device.touch(By.id('id/et_email'), md.DOWN_AND_UP)
        mr.sleep(1)
        device.type(u'\u0020\u0020\u0020\u0020 893026750@163.com')
        mr.sleep(1)
        easy_device.touch(By.id('id/et_password'), md.DOWN_AND_UP)

        image = device.takeSnapshot()
        mr.sleep(2)
        image.writeToFile('/Users/apple/auto_test/AutoImage/PreludeNull1.png', 'png')
        result = mr.loadImageFromFile('/Users/apple/auto_test/AutoImage/PreludeNull.png', 'png')
        if image.sameAs(result, 1):
            print ("input prelude null match right")
        else:
            print ("there is a problem here,please check , and the number is:" + str(i))

    elif i == 3:    #邮箱输入中间为空格
        easy_device.touch(By.id('id/et_email'), md.DOWN_AND_UP)
        mr.sleep(1)
        device.type(u'893026750\u0020\u0020\u0020\u0020@163.com')
        mr.sleep(1)
        easy_device.touch(By.id('id/et_password'), md.DOWN_AND_UP)

        image = device.takeSnapshot()
        mr.sleep(2)
        image.writeToFile('/Users/apple/auto_test/AutoImage/MiddleNull1.png', 'png')
        result = mr.loadImageFromFile('/Users/apple/auto_test/AutoImage/MiddleNull.png', 'png')
        if image.sameAs(result, 1):
            print ("input middle null match right")
        else:
            print ("there is a problem here,please check , and the number is:" + str(i))

    elif i == 4:    #邮箱输入尾部为空格
        easy_device.touch(By.id('id/et_email'), md.DOWN_AND_UP)
        mr.sleep(1)
        device.type(u'893026750@163.com\u0020\u0020\u0020\u0020')
        mr.sleep(1)
        easy_device.touch(By.id('id/et_password'), md.DOWN_AND_UP)

        image = device.takeSnapshot()
        mr.sleep(2)
        image.writeToFile('/Users/apple/auto_test/AutoImage/TailNull1.png', 'png')
        result = mr.loadImageFromFile('/Users/apple/auto_test/AutoImage/TailNull.png', 'png')
        if image.sameAs(result, 1):
            print ("input tail null match right")
        else:
            print ("there is a problem here,please check , and the number is:" + str(i))

    elif i == 5:    #邮箱输入没有点号
        easy_device.touch(By.id('id/et_email'), md.DOWN_AND_UP)
        mr.sleep(1)
        device.type('893026750@163com')
        mr.sleep(1)
        easy_device.touch(By.id('id/et_password'), md.DOWN_AND_UP)

        image = device.takeSnapshot()
        mr.sleep(2)
        image.writeToFile('/Users/apple/auto_test/AutoImage/NoDot1.png', 'png')
        result = mr.loadImageFromFile('/Users/apple/auto_test/AutoImage/NoDot.png', 'png')
        if image.sameAs(result, 1):
            print ("input no dot match right")
        else:
            print ("there is a problem here,please check , and the number is:" + str(i))

    elif i == 6:    #邮箱输入没有@符号
        easy_device.touch(By.id('id/et_email'), md.DOWN_AND_UP)
        mr.sleep(1)
        device.type('893026750163.com')
        mr.sleep(1)
        easy_device.touch(By.id('id/et_password'), md.DOWN_AND_UP)

        image = device.takeSnapshot()
        mr.sleep(2)
        image.writeToFile('/Users/apple/auto_test/AutoImage/No@1.png', 'png')
        result = mr.loadImageFromFile('/Users/apple/auto_test/AutoImage/No@.png', 'png')
        if image.sameAs(result, 1):
            print ("input no @ match right")
        else:
            print ("there is a problem here,please check , and the number is:" + str(i))

    elif i == 7:    #密码输入只有5位
        easy_device.touch(By.id('id/et_password'), md.DOWN_AND_UP)
        mr.sleep(1)
        device.type('abcde')
        mr.sleep(1)
        easy_device.touch(By.id('id/et_email'), md.DOWN_AND_UP)

        image = device.takeSnapshot()
        mr.sleep(2)
        image.writeToFile('/Users/apple/auto_test/AutoImage/FiveNumberPs1.png', 'png')
        result = mr.loadImageFromFile('/Users/apple/auto_test/AutoImage/FiveNumberPs.png', 'png')
        if image.sameAs(result, 1):
            print ("input five number password  match right")
        else:
            print ("there is a problem here,please check , and the number is:" + str(i))

    elif i == 8:    #密码输入有20位
        easy_device.touch(By.id('id/et_password'), md.DOWN_AND_UP)
        mr.sleep(1)
        device.type('abcdejhsas32328976jsm')
        mr.sleep(1)
        easy_device.touch(By.id('id/et_email'), md.DOWN_AND_UP)

        image = device.takeSnapshot()
        mr.sleep(2)
        image.writeToFile('/Users/apple/auto_test/AutoImage/TwentyOnePs1.png', 'png')
        result = mr.loadImageFromFile('/Users/apple/auto_test/AutoImage/TwentyOnePs.png', 'png')
        if image.sameAs(result, 1):
            print ("input twenty one password  match right")
        else:
            print ("there is a problem here,please check , and the number is:" + str(i))


def serverPolicy():
    runStartApp()

    mr.sleep(2)
    easy_device.touch(By.id('id/iv_avatar'), md.DOWN_AND_UP)
    mr.sleep(1)
    device.touch(348, 880, 'DOWN_AND_UP')
    mr.sleep(5)

    image = device.takeSnapshot()
    mr.sleep(2)
    image.writeToFile('/Users/apple/auto_test/AutoImage/TeamServer1.png', 'png')
    result = mr.loadImageFromFile('/Users/apple/auto_test/AutoImage/TeamServer.png', 'png')
    if image.sameAs(result, 1):
        print ("the team server page  match right")
    else:
        print ("there is a problem here,please check , and the number is: the team server page" )

    mr.sleep(2)
    easy_device.touch(By.id('id/title_bar_iv_left'), md.DOWN_AND_UP)
    mr.sleep(1)
    device.touch(571, 880, 'DOWN_AND_UP')
    mr.sleep(5)

    image = device.takeSnapshot()
    mr.sleep(2)
    image.writeToFile('/Users/apple/auto_test/AutoImage/PrivacyPolicy1.png', 'png')
    result = mr.loadImageFromFile('/Users/apple/auto_test/AutoImage/PrivacyPolicy.png', 'png')
    if image.sameAs(result, 1):
        print ("the privacy policy page  match right")
    else:
        print ("there is a problem here,please check , and the number is: the privacy policy page")


def auto_teach(i):
    device.press('KEYCODE_DPAD_DOWN', 'DOWN_AND_UP')
    mr.sleep(2)
    if i == 0:  # 第一次打开APP时
        easy_device.touch(By.id('id/tv_standard'), md.DOWN_AND_UP)
        mr.sleep(1)
        easy_device.touch(By.id('id/title_bar_iv_left'), md.DOWN_AND_UP)
        mr.sleep(1)
        easy_device.touch(By.id('id/tv_myCoin'), md.DOWN_AND_UP)
        mr.sleep(1)
        easy_device.touch(By.id('id/tv_sign_in'), md.DOWN_AND_UP)
        mr.sleep(1)
        easy_device.touch(By.id('id/iv_hint'), md.DOWN_AND_UP)
    else:   #再次打开APP时教学页面不存在了
        easy_device.touch(By.id('id/title_bar_iv_left'), md.DOWN_AND_UP)
        print "you have complete the teach"


def runStartApp():
    if isAppExit() == 0:    #如果App不存在，则安装APP并启动
        device.installPackage('/Users/apple/auto_test/formal.apk')
        startActivity()
    elif isAppExit() == 1 and isProcessExit() == 1:   #如果App存在且进程已经开启
        os.system("adb shell am force-stop com.soka.football")    #杀掉该进程，再启动APP
        print ('kill the progress success')
        startActivity()
    else:
        startActivity()


def runLogin():
    for i in range(9):
        auto_login(i)
        # print "执行+ %d +测试用例完毕" + i
        print "execute case and NO:" + str(i)


def main():
    result = True
    print ("please chage a operate:")
    print ("1.tech page function")
    print ("2.login function")
    print ("3.forget password")
    print ("4.server and privacy")
    print ("5.register function")
    print ("input Q and ending the procedure")

    while (result):

        number = mr.input("enter you number:")
        if number is None:     #判断没有输入数字，直接点确定按钮时的情况
            print "please input Q and ending the procedure"
        elif not number:
            print "please input number or input Q  to  ending the procedure"
        else:
            nm_first = str(number)
            print nm_first

            if (nm_first == 'q' or nm_first == 'Q'):
                print ("procedure is ending....")
                mr.sleep(3)
                break

            elif (nm_first.isspace() == True):
                print ("input is can not be null and input again")
                mr.sleep(2)
                break

            elif (nm_first == '1'):
                try:
                    print ("tech page is begin start...")
                    runStartApp()
                except Exception:
                    traceback.print_exc()
                finally:
                    print ("test is end")

            elif (nm_first == '2'):
                try:
                    print ("login page is begin start")
                    runLogin()
                except Exception:
                    traceback.print_exc()
                finally:
                    print ("test is end")

            elif (nm_first == '3'):
                try:
                    print ("forget password function is begin")

                except Exception:
                    traceback.print_exc()

            elif (nm_first == '4'):
                try:
                    print ("server page is begin....")

                except Exception:
                    traceback.print_exc()

            elif (nm_first == '5'):
                try:
                    print ("register page is begin....")
                   # emailScreen()

                except Exception:
                    traceback.print_exc()

            else:
                try:
                    print ("input is invalid")
                    mr.sleep(2)
                    break
                except ValueError:
                    traceback.print_exc()
                    print ("input is invalid")
                    mr.sleep(2)
                    break

            mr.sleep(2)
            print ("please chage a operate:")
            print ("1.tech page function")
            print ("2.login function")
            print ("3.forget password")
            print ("4.server and privacy")
            print ("5.register function")
            print ("input Q and ending the procedure")



if __name__ == "__main__":
    main()

