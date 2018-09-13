# coding=utf-8
import requests
import json
import hashlib
import time

# password = "123456"
# password_md5 = hashlib.md5(password)
# password_encrypt = password_md5.hexdigest()
# print(password_encrypt)





data1 = {"a":3,"b":1,"c":8}
data = json.dumps(data1)
values = {"orgId": "即呗网络", "uid": "420922198912212834", "mobile": "18626876673", "name": "李彬彬", "data" : data}
delivery_data = json.dumps(values)
delivery_url = "http://47.98.155.93:9010/original/push/blackList"
delivery_headers = {"Content-Type": "application/json"}
r = requests.post(url=delivery_url, data=delivery_data, headers=delivery_headers)
print r.status_code
print r.text
print r.encoding





# values = {"mobile": "15682502234", "orgType": "1", "registTime": "2018-05-04"}
# a = str(values)
# delivery_data = json.dumps(values)
# password = "8040c5dbf6978f315e104e5c0bca3e8e2baa4221" + "1525519902" + a
# password_md5 = hashlib.md5(password)
# password_encrypt = password_md5.hexdigest()
# print(password_encrypt)
# b = hashlib.md5(password_encrypt)
# c = b.hexdigest()
# print(c)
#
#
# delivery_url = "http://47.98.155.93:8081/orapi/user/pull"
# delivery_headers = {"Content-Type": "application/json","accessKey" : "7ef9a26e5a32ca9699b930541875dbfb","reqTime" : "1525519902","sign" : "4cb3982720fecadcf78886927481b6b3"}
# print(delivery_headers)
# r = requests.post(url=delivery_url, data=a, headers=delivery_headers)
# print r.status_code
# print r.text
# print r.encoding

