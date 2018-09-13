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

def get_push(url,name, uid, mobile,data, orgId='51闪电购'):
    # 返回：{"code": 1000000,"msg": "成功","data": null}
    name, uid, mobile,data = map(unicode2str, [name, uid, mobile,data])
    payload = json.dumps(
        dict(orgId=orgId, uid=uid, mobile=mobile, name=name,data=data), ensure_ascii=False)

    headers = signHeaders(payload)
    response = requests.post(url = url,  data=payload,headers=headers, timeout=5)
    print(response.status_code)
    print(response.text)
    return response
    # text = response.text.split('data')
    # print(text[1])

def get_pull(url,name, uid, mobile, dataOfOrgId='51闪电购'):
    # 返回：{"code": 1000000,"msg": "成功","data": null}
    name, uid, mobile = map(unicode2str, [name, uid, mobile])
    payload = json.dumps(
        dict(dataOfOrgId=dataOfOrgId,uid=uid, mobile=mobile, name=name), ensure_ascii=False)

    headers = signHeaders(payload)
    response = requests.post(url = url,  data=payload,headers=headers, timeout=5)
    print(response.status_code)
    print(response.text)
    return response
    # text = response.text.split('data')
    # print(text[1])

if __name__ == "__main__":
    # url = "https://sharedata.51sdgo.com/owapi/original/push/blackList"
    # detail_x = "this is a test detail"
    # detail = json.dumps(detail_x)
    # data_x = {"label" : "51闪电购","timeOutDay" : "10","detail" : detail}
    # data = json.dumps(data_x)
    # get_push(url,"洪乃武", "360281199312211010", "17348518942",data)
    #
    # url = "https://sharedata.51sdgo.com/owapi/original/push/overdue"
    # values = {"orderId" : "","timeOutDay" : "5","isSelf" : "1","status" : "8"}
    # data = json.dumps(values)
    # get_push(url,"洪乃武", "360281199312211010", "17348518942",data)
    #
    # url = "https://sharedata.51sdgo.com/owapi/original/push/device"
    # values = {
    #     "appName" : "android",
    #     "appVersion" : "1.2.0",
    #     "carrierOperator" : "中国移动",
    #     "cellIp" : "10.10.148.187",
    #     "country" : "zh_CN",
    #     "cpuArchitecture" : "ARM64",
    #     "cpuProcessorNum" : "6",
    #     "deviceId" : "dd2064a920aa2d294312332",
    #     "deviceModel" : "sumsung 8",
    #     "deviceName" : "sumsung",
    #     "deviceType" : "sumsung",
    #     "diskTotalSpace" : "249989716 KB",
    #     "memoryTotal" : "3145728 KB",
    #     "os" : "android",
    #     "osVersion" : "8.0.1",
    #     "partnerId" : "test",
    #     "platform" : "android",
    #     "screenBrightness" : "36",
    #     "screenH" : "1400",
    #     "screenW" : "300",
    #     "uploadTime" : "20180521153840255"
    # }
    # data = json.dumps(values)
    # get_push(url,"洪乃武", "360281199312211010", "17348518942",data)
    #
    #
    # url = "https://sharedata.51sdgo.com/owapi/original/push/sesameScores"
    # values = {
    #     "bizNo": "ZM201805083000000646500089895502",
    #     "name": "洪乃武",
    #     "uid": "360281199312211010",
    #     "mobile": "17348518942",
    #     "score": "1234"
    # }
    # data = json.dumps(values)
    # get_push(url,"洪乃武", "360281199312211010", "17348518942",data)

    url1 = "https://sharedata.51sdgo.com/orapi/original/pull/overdue"
    url2 = "https://sharedata.51sdgo.com/orapi/original/pull/blackList"
    url3 = "https://sharedata.51sdgo.com/orapi/original/pull/device"
    url4 = "https://sharedata.51sdgo.com/orapi/original/pull/sesameScores"
    get_pull(url3,"洪乃武", "360281199312211010", "17348518942")

