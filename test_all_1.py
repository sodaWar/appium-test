# coding=utf-8
import requests
import json
import hashlib
import time

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
    # access_key = '21a7dcdcec8dda1c'
    access_key = 'f45e02407333e53d1e1479dcac320689'
    #secret_key = '42391dd9e93f213e131280619128d23d'
    secret_key = '4042bb58863a509d9c76bd4d5de7eb8c'
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

#推送接口（数据写入到mongo中）
def get_push(url,name, uid, mobile,data, qtype,orgId):
    # 返回：{"code": 1000000,"msg": "成功","data": null}
    # name, uid, mobile,data = map(unicode2str, [name, uid, mobile,data])
    payload = json.dumps(
        dict(orgId=orgId, uid=uid, mobile=mobile, qtype = qtype,name=name,data=data), ensure_ascii=False)

    headers = signHeaders(payload)
    response = requests.post(url = url,  data=payload,headers=headers, timeout=5)
    print(response.status_code)
    print(response.text)
    return response

#黑名单上行接口（数据写入到mysql中）
def get_push_1(url,category,mobile,uid,timeoutDay):
    payload = json.dumps(
        dict( category = category,mobile = mobile,uid = uid,timeoutDay = timeoutDay), ensure_ascii=False)

    headers = signHeaders(payload)
    response = requests.post(url = url,  data=payload,headers=headers, timeout=5)
    print(response.status_code)
    print(response.text)
    return response

#注册用户上行接口（数据写入到mysql中）
def get_push_2(url,userName, mobile,orgType,orgName,registTime):
    userName, mobile, orgType, orgName, registTime = map(unicode2str, [userName, mobile,orgType,orgName,registTime])
    payload = json.dumps(
        dict(userName = userName, mobile = mobile,orgType = orgType,orgName = orgName,registTime = registTime), ensure_ascii=False)

    headers = signHeaders(payload)
    response = requests.post(url = url,  data=payload,headers=headers, timeout=5)
    print(response.status_code)
    print(response.text)
    return response

#芝麻分接口
# def get_push_3(url,notifyUrl,uid,mobile,name):


#拉取接口（从mongo中取出数据）
def get_pull(url,name, uid, mobile,dataOfOrgId):
    # 返回：{"code": 1000000,"msg": "成功","data": null}
    # name, uid, mobile = map(unicode2str, [name, uid, mobile])
    payload = json.dumps(
        dict(dataOfOrgId=dataOfOrgId, uid=uid, mobile=mobile, name=name), ensure_ascii=False)

    headers = signHeaders(payload)
    response = requests.post(url = url,  data=payload,headers=headers, timeout=5)
    # assert response.status_code == 200                                                          # 断言assert的作用是判断接下来的语句是否正确，如果断言成功即判断的布尔值返回为true,那么不执行任何操作,如果断言不成功,会触发AssertionError返回报错信息
    print(response.status_code)
    print(response.text)
    return response
    # text = response.text.split('data')
    # print(text[1])

#黑名单下行接口
def get_pull_1(url, category,uid,timeoutDay):
    payload = json.dumps(
        dict(category = category,uid = uid,timeoutDay=timeoutDay), ensure_ascii=False)

    headers = signHeaders(payload)
    response = requests.post(url = url,  data=payload,headers=headers, timeout=5)
    print(response.status_code)
    print(response.text)
    return response

#注册用户下行接口
def get_pull_2(url,mobile, orgType, registTime):
    mobile, orgType, registTime = map(unicode2str, [mobile, orgType, registTime])
    payload = json.dumps(
        dict(mobile = mobile, orgType = orgType, registTime = registTime), ensure_ascii=False)

    headers = signHeaders(payload)
    response = requests.post(url = url,  data=payload,headers=headers, timeout=5)
    print(response.status_code)
    print(response.text)
    return response

if __name__ == "__main__":

    #逾期数据推送
    # url1 = "http://47.98.155.93:8081/owapi/original/push/overdue"
    # data_x = {"timeOutDay" : "10","status" : "9","orderId" : "test20180620y8143d"}
    # data = json.dumps(data_x)
    # get_push(url1,"洪乃武", "360281199312211010", "17348518942",data)

    #黑名单数据推送
    # url2 = "http://47.98.155.93:8081/owapi/original/push"
    # detail_x = "this is test"
    # detail = json.dumps(detail_x)
    # data_x = {"label":"1","timeOutDay" : "10","detail" : detail}
    # data = json.dumps(data_x)
    # get_push(url2,"洪乃武", "360281199312211010", "17348518942",data,"2","91极速购")

    #设备数据推送
    # url3 = "http://47.98.155.93:8081/owapi/original/push/device"
    # data_x = {
    #     "appName":"android",
    #     "appVersion" : "6.0.0",
    #     "carrierOperator" : "中国电信",
    #     "cellIp" : "10.10.148.187",
    #     "deviceId" : "dd2038976asf213121",
    #     "deviceModel" : "SanSung 8",
    #     "deviceName" : "android",
    #     "diskTotalSpace" : "249989716 KB",
    #     "memoryTotal" : "3145728 KB",
    #     "screenBrightness" : "40",
    #     "screenH" : "2200",
    #     "screenW" : "500",
    #     "uploadTime" : "20180620163318255"
    #           }
    # data = json.dumps(data_x)
    # get_push(url3,"洪乃武", "360281199312211010", "17348518942",data,"2","91极速购")

    #芝麻分数据推送
    # url4 = "http://47.98.155.93:8081/owapi/original/push/sesameScores"
    # data_x = {
    #     "bizNo":"ZM201805083000000646500089895502",
    #     "name" : "洪乃武",
    #     "uid" : "360281199312211010",
    #     "mobile" : "17348518942",
    #     "score" : "788",
    #           }
    # data = json.dumps(data_x)
    # get_push(url4,"洪乃武", "360281199312211010", "17348518942",data,"2","91极速购")


    #逾期数据拉取
    url_a = "http://47.98.155.93:8081/orapi/original/pull/overdue"
    # url_b = "http://47.98.155.93:8081/orapi/original/pull/blackList"
    # url_c = "http://47.98.155.93:8081/orapi/original/pull/device"
    # url_d = "http://47.98.155.93:8081/orapi/original/pull/sesameScores"
    get_pull(url_a, "洪乃武", "360281199312211010", "17348518942","即呗网络")

    #黑名单数据上行接口
    # url_x = "http://47.98.155.93:8081/owapi/blackList/save"
    # get_push_1(url_x,"1","1","17348518942","360281199312211010")

    #注册用户上行接口
    # url_y = "http://47.98.155.93:8081/owapi/user/save"
    # get_push_2(url_y,"洪乃武","17348518942","1","51闪电购","2018-06-20 17:00:00")

    #黑名单下行接口
    # url_z = "http://47.98.155.93:8081/orapi/credit/blackList"
    # get_pull_1(url_z,"1","360281199312211010","5")

    #注册用户下行接口
    # url_r = "http://47.98.155.93:8081/orapi/user/pull"
    # get_pull_2(url_r,"17348518942","1","2018-06-20")