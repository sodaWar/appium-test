# -* encoding:utf-8 *-
import email
from poplib import POP3_SSL
from email.parser import Parser
import re
import datetime
from email.header import decode_header     #对邮箱解码
from email.utils import parseaddr

def receiveEmail():
    r = []                          #验证码未超时的数列
    t = []                          #验证码超时的数列
    email = '893026750@qq.com'
    password = 'bmnvhnpikgjsbeji'
    pop3_server = 'pop.qq.com'        #QQ的POP3服务器地址

    server = POP3_SSL(pop3_server)    #连接到QQ的pop3服务器
    print (server.getwelcome())       #POP3服务器的欢迎文字
    #身份认证
    server.user(email)
    server.pass_(password)
    print ('Message: %s  Size:%s' % server.stat())    #stat()返回邮件数量和每个邮件所占用的空间

    resp,mails,octets = server.list()       #list()返回所有邮件的编号和占用空间
    print mails
    if len(mails) == 0:
        print '邮箱为空，未收到邮件，请进入邮箱查看'
    else:
        index = len(mails)          # 获取最新一封邮件, 注意索引号从1开始:
        for i in range(index):
            resp,lines,octets = server.retr(i+1)       # lines存储了邮件的原始文本的每一行,
            msg_content = '\r\n'.join(lines)           #获得整个邮件的原始文本:
            GMT_FORMAT = '%a, %d %b %Y %H:%M:%S +0000 (GMT)'    #GMT时间格式的字符串

            # hdr,message,octet=server.retr(1)   #读取第一个邮件信息，效果与上面一样
            msg = Parser().parsestr(msg_content)
            date = msg.get("Date")
            subject = msg.get("subject")                  #邮件标题
            From = msg.get("From")
            To = msg.get("To")

            # print date                                   #邮件发送时间（返回的是GMT时间格式）
            transform_time = datetime.datetime.strptime(date,GMT_FORMAT)      #将GMT时间格式的字符串转换为datetime类型
            now = datetime.datetime.now()                          #获取现在的时间，类型为datetime，但是该时间的秒数会精确到小数点后6位
            current_time1 = now.strftime("%Y-%m-%d %H:%M:%S")      #将now时间转换成对应的格式，类型为str类型
            current_time2 = datetime.datetime.strptime(current_time1,"%Y-%m-%d %H:%M:%S")       #将str类型的时间转换成datetime类型
            differ_time1 = current_time2 - transform_time       #两个str类型的时间不能进行加减操作，所以必须先转换成datetime类型
            differ_time2 = differ_time1.total_seconds()        #获取两个时间相差的总秒数，另外date、time和datetime类都支持与timedelta的加、减运算
            differ_time3 = int(differ_time2-28800)                 #减去8小时的与中国的时间差
            content = msg.get_payload(decode=True)        #获取邮件的内容
            # print type(content)
            # print msg
            # print "subject:",subject
            # print "From:",From
            # print "To:",To
            # print "Content:",content

            if subject == 'SOKA FOOTBALL Verification code' and differ_time3 < 7200:
                s = re.findall("\d+",content)[0]
                r.append(s)
            elif subject == 'SOKA FOOTBALL Verification code' and differ_time3 > 7200:
                s = re.findall("\d+",content)[0]
                t.append(s)
            else:
                print '该邮件不是SOKA FOOTBALL发送的验证码邮件'
    return (r,t)
if __name__ == "__main__":
    receiveEmail()