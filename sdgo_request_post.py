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


def get_data1(name, uid, mobile, q_type='4', org_id='51闪电购'):
    # 返回：{"code": 1000000,"msg": "成功","data": null}
    name, uid, mobile = map(unicode2str, [name, uid, mobile])
    payload = json.dumps(
        dict(dataOfOrgId=org_id, qtype=q_type, uid=uid, mobile=mobile, name=name), ensure_ascii=False)

    access_key = 'lbb'
    secret_key = 'lbbcs'
    req_time = get_millis()

    sign = ''.join([secret_key, req_time, payload])
    sign = get_md5hex(get_md5hex(sign))

    headers = {
        'accesskey': access_key,
        'reqtime': req_time,
        'sign': sign,
        'content-type': "application/json"
    }

    url = "http://47.98.155.93:8081/orapi/original/pull"
    response = requests.post(url, data=payload, headers=headers, timeout=5)
    text = response.text.split('data')
    # print(text[1])
    print(response.status_code)
    print(response.text)
    return response

def get_data2(category, mobile, label, timeoutDay, userName,state):
    # 返回：{"code": 1000000,"msg": "成功","data": null}
    category, mobile, label, timeoutDay, userName, state = map(unicode2str, [category, mobile, label, timeoutDay, userName,state])
    payload = json.dumps(
        dict(category=category, mobile=mobile, label=label, timeoutDay=timeoutDay, userName=userName,state=state), ensure_ascii=False)

    access_key = 'lbb'
    secret_key = 'lbbcs'
    req_time = get_millis()

    sign = ''.join([secret_key, req_time, payload])
    sign = get_md5hex(get_md5hex(sign))

    headers = {
        'accesskey': access_key,
        'reqtime': req_time,
        'sign': sign,
        'content-type': "application/json"
    }

    url = "http://47.98.155.93:8081/orapi/credit/blackList"
    response = requests.post(url, data=payload, headers=headers, timeout=5)
    text = response.text.split('data')
    # print(text[1])
    print(response.status_code)
    print(response.text)
    return response


if __name__ == "__main__":
    a = json.dumps("0")
    get_data1("李彬彬", "420922198912212834", "18626876673")

    # for i in range(300):
    #     get_data1("李彬彬", "420922198912212834", "18626876673")
    # get_data1("test", "360926197302164710", "15958049747")
    # get_data2("1","18626876673","2","7","李彬彬",a)