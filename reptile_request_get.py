# -* encoding:utf-8 *-
import requests
import time
import json

def match_reptile():
    now = int(round(time.time() * 1000))        #python的时间戳是以秒为单位输出的float,通过把秒转换毫秒的方法获得13位的时间戳
    print now
    now1 = time.time() * 1000

    values = {"bid": 11230, "pid" : "9573477-1478443907"}
    re_url = "http://buluo.qq.com/p/detail.html?"
    r = requests.get(url = re_url,params = values)
    end = r.text                    #获取接口返回的数据,json格式的数据
    print(r.status_code)
    end_json = json.loads(end)      #将json编码的字符串转换回一个python数据结构,该方法是将json数据库解码，而json.dump()是将字符串编码成json数据
    print end_json
    startTime = end_json['data']['startTime']
    endTime = end_json['data']['endTime']
    result = end_json['data']['list']      #根据匹配字典中的键来查询相应的值
    s1 = len(result)
    print s1       #list中的内容长度，该list为数列，即数列中有多少个值，只是每个值又是一个元组
    print startTime,endTime
match_reptile()
    # print result
    # a = result[1]         #list的索引为1的值，该值为元组
    # b = a['matchId']      #该元素的键matchId的值
    # print a
    # print b
    # for i in range(len(result)):
    #     result1 = result[i]
    #     # result_match = result['gameweek']
    #     print result1
        # print result_match
    # s3 = s1
    # for i in range(100):
    #     values = {"uid": "ea99d0954d508888975a18768c6f443f", "startTime": startTime, "endTime": endTime, "isback": 0}
    #     r = requests.get(url=re_url, params=values)
    #     end = r.text
    #     end_json = json.loads(end)
    #     # print end_json
    #     startTime = end_json['data']['startTime']
    #     endTime = end_json['data']['endTime']
    #     result = end_json['data']['list']
    #     s2 = len(result)
    #     if s2 == 0:
    #         print '数据已拉完'
    #         break
    #     else:
    #         s3 = s3 + s2                #注意该方式，要想使得每次循环后的结果都能够相加，那每次循环后的S3的值必须变化，所以s3在定义时需要定义在循环外面
    #         print s3                    #例如上面的s3=s1，只是初始化s3的值而已，将s3的值初始化成s1的值,然后每次循环后s3的值就能够发生变化，循环相加
    # return s3

            # print startTime, endTime