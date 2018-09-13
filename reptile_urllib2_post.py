# coding=utf-8
import urllib2
import hashlib
import json

password = "naiwu3425"
password_md5 = hashlib.md5(password)   #将字符串加密成一段唯一的固定长度的代码，称为md5加密
password_encrypt = password_md5.hexdigest()

values = {"identity": "893026755@qq.com", "type": 0, "password": password_encrypt, "os": 1}
data = json.dumps(values)          #将输入的参数数据由字典格式转换为json格式
print(data)
url = "http://api.test.sokafootball.com:8092/register/email"
headers = {"Content-Type" : "application/json"}     #第一种方式，其效果都是一样的
request = urllib2.Request(url, data ,headers)
#request.add_header("Content-Type","application/json")       #在请求接口时加入特定的header头部信息的第二种方式
response = urllib2.urlopen(request)
print response.read()
