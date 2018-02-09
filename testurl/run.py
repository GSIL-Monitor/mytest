# -*- coding:utf-8 -*-
author = 'chenshu2'
import base64
import datetime
import json

import requests

from testurl import case, func, ip, url


class run():
    def postTest(self,ip,url,data):
        ff = func.Func()  # 实例化
        parm = ff.b64(data)  # 加密
        host =ip + url
        headers = {"Content-Type": "application/json,charset=UTF-8"}
        starttime = datetime.datetime.now()
        print(host)
        #exit()
        try:
            req = requests.post(url=host, data=parm, headers=headers)
            endtime = datetime.datetime.now()
            print("请求时间：", f"{endtime - starttime}")
            re = bytes.decode(base64.b64decode(req.text))
            print(json.dumps((json.loads(re)),indent=4))
            req.close()
        except Exception as e:
            print(e)

        return None
    def getTest(self,ip,url,data):
        ff = func.Func()  # 实例化
        parm = ff.b64(data)  # 加密
        host =ip + url
        headers = {"Content-Type": "application/json,charset=UTF-8"}
        print(host)
        starttime = datetime.datetime.now()
        try:
            req = requests.get(url=host,params=parm, headers=headers)
            endtime = datetime.datetime.now()
            print("请求时间：", f"{endtime - starttime}")
            re = bytes.decode(base64.b64decode(req.text))
            print(json.dumps((json.loads(re)), indent=4))
            req.close()
        except Exception as e:
            print(e)
        return None
t = run().postTest(ip=ip.ord_sit, url=url.pay, data=case.data3)

