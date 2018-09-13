# -* encoding:utf-8 *-
from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP_SSL


smtp_server = 'smtp.qq.com'             # QQ的SMTP服务器地址
sender_qq_adr = '893026750@qq.com'      #发送人的邮箱地址
password = 'bmnvhnpikgjsbeji'           #QQ邮箱的授权码
receiver_qq_adr = '893026750@qq.com'    #收件人的邮箱地址

mail_content = 'hello,this email is python send to you'    #邮件的正文内容
mail_title = 'python send email '               #邮件标题

smtp = SMTP_SSL(smtp_server)         #SSL登录
smtp.set_debuglevel(1)               #用来调试的，1为开启调试模式，可以在控制台打印出和SMTP服务器交互的所有信息
smtp.ehlo(smtp_server)   #what't mean
smtp.login(sender_qq_adr,password)   #登录SMTP服务器

#邮件主题、如何显示发件人、收件人等信息并不是通过SMTP协议发给MTA，而是包含在发给MTA的文本中的
msg = MIMEText(mail_content,'plain','utf-8')  #构造MIMEText对象
msg['Subject'] = Header(mail_title,'utf-8')
msg['From'] = sender_qq_adr                   #将邮件主题、发件人和收件人添加到MIMEText中
msg['To'] = receiver_qq_adr
smtp.sendmail(sender_qq_adr,receiver_qq_adr,msg.as_string())        #邮件正文是一个str，所以需要将MIMEText对象变成str类型，这一个特别注意，是将对象转换成字符串类型的方法
print 'send ok'

smtp.quit()
