# -*- coding:utf-8 -*-
author = 'chenshu2'
import base64
import datetime
import json

import requests

from testurl import case, func, ip, url


def bookPay(en, data):
    api = en
    p = data
    if api == 1:
        api = ip.ord_sst
    if api == 2:
        api = ip.ord_sit
    if api == 3:
        api = ip.ord_pre
    if api == 4:
        api = ip.ord_pre
    try:
        ff = func.Func()  # 实例化
        parm = ff.b64(p)  # 加密
        host1 = api + url.book
        host2 = api + url.pay
        headers = {"Content-Type": "application/json,charset=UTF-8"}
        starttime = datetime.datetime.now()
        req = requests.post(url=host1, data=parm, headers=headers)
        re = bytes.decode(base64.b64decode(req.text))
        print(re)
        s = json.loads(re)["success"]
        i = json.loads(re)["data"]["orderId"]
        print(i)
    except Exception as a:
        print(a)
    try:
        # 支付订单
        datapay = {
            "orderId": i,
            "payCardNum": "123546",
            "pay": 1500,
            "payTotal": 1500,
            "lastPayTime": "2016-07-06 16:27:20"
        }
        dpay = ff.b64(datapay)
        reqpay = requests.post(url=host2, data=dpay, headers=headers)
        rpay = bytes.decode(base64.b64decode(reqpay.text))
        print("支付:", json.loads(rpay)["success"])
        endtime = datetime.datetime.now()
        print("请求时间：", f"{endtime - starttime}")
        req.close()
        reqpay.close()
    except Exception as e:
        print(e)
    return None
if __name__ == '__main__':
    bookPay(2,case.datagrab)
