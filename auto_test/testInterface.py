# coding=utf-8
from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP_SSL
import requests
import json
import hashlib
import time
import logging
import os
import xlrd                                                                                                             # 操作xlsx文件的库
import base64                                                                                                           # 生成的编码可逆,速度快,生成ascii字符,但是容易破解,仅适用于加密非关键信息的场合
from pyDes import *                                                                                                     # 使用pydes库进行des加密
from requests.exceptions import Timeout
reload(sys)
sys.setdefaultencoding('utf8')                                                                                          # 编码转换,转换之后默认编码格式是utf8,详细见笔记


log_file = os.path.join(os.getcwd(),'D:\\MyProgram\\AppiumProject\\appium-test\\auto_test\\interfaceLog.txt')
log_format = '[%(asctime)s] [%(levelname)s] %(message)s'                                                                # 指定日志输出的格式和内容,format可以输出很多有用的信息,asctime是打印日志的时间,levelname是打印日志级别名称,message是打印日志信息
logging.basicConfig(format=log_format,filename=log_file,filemode='w',level=logging.DEBUG)
#定义一个StreamHandler，将INFO级别或debug级别或者更高的日志信息打印到标准错误，并将其添加到当前的日志处理对象,logging有一个日志处理的主对象，其它处理方式都是通过addHandler添加进去的
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
# console.setLevel(logging.INFO)
formatter = logging.Formatter(log_format)
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)


def unicode2str(u):
    return u if isinstance(u, str) else u.encode('utf8')


def get_millis():
    # 同Java System.currentTimeMillis()方法
    return str(int(round(time.time() * 1000)))


def get_md5hex(source):
    # 同Java md5Hex()方法
    m = hashlib.md5()
    m.update(source)
    return m.hexdigest()

def signHeaders(payload):
    access_key = '7ef9a26e5a32ca9699b930541875dbfb'
    secret_key = '8040c5dbf6978f315e104e5c0bca3e8e2baa4221'
    req_time = get_millis()

    sign = ''.join([secret_key, req_time, payload])
    sign = get_md5hex(get_md5hex(sign))

    headers = {
        'accesskey': access_key,
        'reqtime': req_time,
        'sign': sign,
        'content-type': "application/json"
    }
    return headers


# 获取执行测试用例
def runTest(TestCase):
    testCase = os.path.join(os.getcwd(), TestCase)                                                                      # join()函数是连接字符串数组,os.path.join()函数是将多个路径组合后返回,os.getcwd()是返回当前进程的工作目录,TestCase是测试用例文件的目录地址
    if not os.path.exists(testCase):
        logging.error('测试用例文件不存在！')
        sys.exit()
    testCase = xlrd.open_workbook(testCase)                                                                             # 打开文件
    table = testCase.sheet_by_index(0)                                                                                  # 根据shell索引获取sheet内容
    pwd = '123456'
    errorCase = []                                                                                                      # 用于保存接口返回的内容和HTTP状态码

    for i in range(1, table.nrows):                                                                                     # 循环行列表数据,table.nrows是获取行数
        if table.cell(i,10).value.replace('\n','').replace('\r','') != 'Yes':                                           # table.cell().value获取某个单元格的内容值,该方法第一个参数是行数,第二个参数是列数
            continue
        num = str(int(table.cell(i,0).value)).replace('\n','').replace('\r','')
        api_purpose = table.cell(i,1).value.replace('\n','').replace('\r','')
        api_host = table.cell(i,2).value.replace('\n','').replace('\r','')
        request_url = table.cell(i,3).value.replace('\n','').replace('\r','')
        request_method = table.cell(i,4).value.replace('\n','').replace('\r','')
        request_data_type = table.cell(i,5).value.replace('\n','').replace('\r','')
        request_data = table.cell(i,6).value.replace('\n','').replace('\r','')
        encryption = table.cell(i,7).value.replace('\n','').replace('\r','')
        check_point = table.cell(i,8).value
        # correlation = table.cell(i,9).value.replace('\n','').replace('\r','').split(';')


        if encryption == 'MD5':                                                                                         # 如果数据采用md5加密，便先将数据加密,这里加密的密码需要跟不同接口的session有关系
            request_data = json.loads(request_data)
            request_data['pwd'] = hashlib.md5().update(request_data['pwd']).hexdigest()
        elif encryption == 'DES':                                                                                       # 数据采用des加密
            k = des('secretKEY', padmode=PAD_PKCS5)
            desPwd = base64.b64encode(k.encrypt(json.dumps(pwd)))

        status,resp = interfaceTest(num, api_purpose, api_host, request_url, request_method,request_data_type,request_data,encryption, check_point)
        if status != 200:                                                                                               # 如果状态码不为200，那么证明接口产生错误，保存错误信息。
            errorCase.append((num + '、' + api_purpose, str(status) + api_host + request_url,resp))
            continue
    return errorCase

# 接口调用函数
def interfaceTest(num, api_purpose, api_host, request_url, request_method,request_data_type,request_data, encryption,check_point):
    data = eval(request_data)                                                                                           # 将str类型转换成字典类型
    payload = json.dumps(data)
    headers = signHeaders(payload)
    url = api_host + request_url
    if request_method == 'POST' and request_data_type != 'File':
        try:
            response = ''
            if request_data_type == "Data":
                response = requests.post(url=url, data=payload, headers=headers, timeout=5)
                print(2)
            elif request_data_type == 'Form':
                response = requests.post(url=url, data=data, headers=headers, timeout=5)
                print(1)
            status = response.status_code
            resp1 = response.text
            print(status)
            print(resp1)
            resp2 = resp1.encode("utf-8")

            if status == 200:
                if check_point in resp2:
                    logging.info(num + '. ' + api_purpose + ' 成功, ' + str(status) + ', ' + resp2)
                else:
                    logging.error(num + '.' + api_purpose + ' 失败！！！, [ ' + str(status) + ' ], ' + resp2)
                return status, resp2
            else:
                logging.error(num + ' ' + api_purpose + ' 失败！！！, [ ' + str(status) + ' ], ' + resp2)
                return status, resp2
        except Timeout:
            logging.error(num + ' .' + api_purpose + ':' + url + '超时响应,请注意!!')
            mail_title = '接口响应超时: ' + api_purpose + ':' + url
            overTimeWarn(mail_title)
    elif request_method == 'GET':
        try:
            response = requests.get(url=request_url,params=request_data,timeout = 5)
            status = response.status_code
            resp1 = response.text
            resp2 = resp1.encode("utf-8")
            # resp = response.read()
            print(status)
            print(resp2)
            return status, resp2

        except Timeout:
            logging.error(num + ' .' + api_purpose + ':' + url + '超时响应,请注意!!')
            mail_title = '接口响应超时: ' + api_purpose + ':' + url
            overTimeWarn(mail_title)

    elif request_data_type == 'File':
        dataFile = request_data
        if not os.path.exists(dataFile):
            logging.error(num + ' ' + api_purpose + ' 文件路径配置无效，请检查[Request Data]字段配置的文件路径是否存在！！！')
        fopen = open(dataFile, 'rb')
        data = fopen.read()
        fopen.close()
        # request_data = '''
        return request_data_type

# 接口超时预警邮件,发送文本格式的邮件
def overTimeWarn(mail_title):
    smtp_server = 'smtp.qq.com'                                                                                         # QQ的SMTP服务器地址
    sender_qq_adr = '893026750@qq.com'                                                                                  # 发送人的邮箱地址
    password = 'bmnvhnpikgjsbeji'                                                                                       # QQ邮箱的授权码
    receiver_qq_adr = '893026750@qq.com'                                                                                # 收件人的邮箱地址

    mail_content = 'warn,interface request overtime,please look out!!'                                                  # 邮件的正文内容
    mail_title = mail_title                                                                                             # 邮件标题

    smtp = SMTP_SSL(smtp_server)                                                                                        # SSL登录
    smtp.set_debuglevel(1)                                                                                              # 用来调试的，1为开启调试模式，可以在控制台打印出和SMTP服务器交互的所有信息
    smtp.ehlo(smtp_server)                                                                                              # what't mean
    smtp.login(sender_qq_adr, password)                                                                                 # 登录SMTP服务器

    # 邮件主题、如何显示发件人、收件人等信息并不是通过SMTP协议发给MTA，而是包含在发给MTA的文本中的
    msg = MIMEText(mail_content, 'plain', 'utf-8')                                                                      # 构造MIMEText对象
    msg['Subject'] = Header(mail_title, 'utf-8')
    msg['From'] = sender_qq_adr                                                                                         # 将邮件主题、发件人和收件人添加到MIMEText中
    msg['To'] = receiver_qq_adr
    smtp.sendmail(sender_qq_adr, receiver_qq_adr,
                  msg.as_string())                                                                                      # 邮件正文是一个str，所以需要将MIMEText对象变成str类型，这一个特别注意，是将对象转换成字符串类型的方法
    print 'send ok'

    smtp.quit()


# 接口请求测试完成后的通知邮件,发送html格式的邮件
def sendMail(text):
    smtp_server = 'smtp.qq.com'
    sender = '893026750@qq.com'                                                                                         # 发送人
    receiver = ['893026750@qq.com']                                                                                     # 收件人
    mailToCc = ['893026750@qq.com']                                                                                     # 抄送人
    subject = '[AutomantionTest]接口自动化测试报告通知'                                                                    # 邮件标题
    username = '893026750'                                                                                              # 用户邮箱的账号
    password = 'bmnvhnpikgjsbeji'

    msg = MIMEText(text, 'html', 'utf-8')
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ';'.join(receiver)
    msg['Cc'] = ';'.join(mailToCc)
    smtp = SMTP_SSL(smtp_server)
    smtp.connect(smtp_server)
    smtp.login(username, password)
    smtp.sendmail(sender, receiver + mailToCc, msg.as_string())
    smtp.quit()



def main():
    errorTest = runTest('D:\\MyProgram\\AppiumProject\\appium-test\\auto_test\\TestCase.xlsx')
    if len(errorTest) > 0:
        html = '<html><body>接口自动化定期扫描，共有 ' + str(len(errorTest)) + ' 个异常接口，列表如下：' + '</p><table><tr><th style="width:100px;">接口</th><th style="width:50px;">状态</th><th style="width:200px;">接口地址</th><th>接口返回值</th></tr>'
        for test in errorTest:
            print(test)
            html = html + '<tr><td>' + test[0] + '</td><td>' + test[1] + '</td><td>' + test[2] + '</td></tr>'
        html = html + '</table></body></html>'
        sendMail(html)

if __name__ == '__main__':
    main()



