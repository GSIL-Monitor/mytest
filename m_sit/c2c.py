# -*- coding:utf-8 -*-
author = 'chenshu2'

import json
import requests

from testurl import func


class C2c():
    @property
    def c2c_book(self):
        url = "http://m-sit.tuniu.org/api/train/memberRights/memberRightsOrder"

        payload = {
            "resId": 199,
            "vipInfo": {
                "memberName": "diaobaole",
                "memberIdType": 1,
                "memberIdNo": "32118119911225353x"
            }
        }
        headers = {
            'content-type': "application/json",
            'cookie': "tuniu_partner=MjAxLDAsLGQzN2UwNjg4ZDEyYzVmMmNmYzBlYjMyZGUyMzFkMDQ5; PageSwitch=2%2C1521018859; tuniuuser_citycode=MjUwMA%3D%3D; tuniuuser_id=71656166; rg_entrance=030000%2F010002%2F000015%2F000000; Hm_lvt_ae25642992035099e716fa9b0b1c5636=1511161946; Hm_lpvt_ae25642992035099e716fa9b0b1c5636=1513243276; departCityCode=2500; departCityName=%u4E0A%u6D77; departStationId=1175075; departStationName=%u4E0A%u6D77%u7AD9; destCityCode=1631; destCityName=%u6606%u5C71; honeydukesUname=6ZmI5pyvMg%3D%3D; honeydukesTelExt=; honeydukesUspelling=chenshu2; honeydukesUid=20243; honeydukesUNum=19464; tuniusub=1; destStationId=1175980; destStationName=%u6606%u5C71%u7AD9; ssoUser=8gi43hvmbue1f2lrhk4m8ktgg0; BSFIT_OkLJUJ=JFKIx49P5oW4WvTfoSPk_nQwvwkLK0cD; fp_ver=4.5.2; BSFIT_EXPIRATION=1513492508347; BSFIT_DEVICEID=V1SN50A-rC7g8RJiCdDrcdNIk16JlfXXhrk_Wz2YtnPX2MJvRKBxI0eB2MIZBifGFnVRSgS4i8zQwUWxT79j41miNJya41q-s20waa3vkALvoJKk0Txe4igMRvddJR5Wm4x3j8CcMw8Izgd9plp1xKzJzOLYAtr4; TRAIN_PHPSESSID=ebe2f42ac5ed1430a6e4a766dfab5434; connect.sid=s%3AbNPxzHhsKdrFx3DVwo3Cxhsjr6_-H4ly.MQp8rwCIhoQcTnQ3tQqxlvJwFvQ%2FFogUHdjL6KGaaeI; isLogined=true; honeydukesSessionID=ST-2689-oqATJmxndYdREVaWOe6O-cas; muser=e20029d299e1900ac986e0ccda8d3468; TUNIUmuser=e20029d299e1900ac986e0ccda8d3468",
            'cache-control': "no-cache",
            'postman-token': "d0fb437d-354f-d37f-7793-48b5ffb05998"
        }
        try:
            response = requests.request("POST", url, data=payload, headers=headers)
            result = (response.json())["success"]
            print(json.dumps(response.json(), indent=4))
            if result:
                try:
                    orderid = (response.json())["data"]["orderId"]
                    purl = "http://10.10.32.203:18280/train/c2c/pay/notice"
                    pdata = {
                        "orderId": orderid,
                        "payCardNum": "00380000824347616220120060000500",
                        "pay": 300,
                        "payTotal": 300,
                        "lastPayTime": "2016-12-02 17:09:33"
                    }
                    f = func.Func().b64(pdata)
                    response_pay = requests.post(url=purl, data=f)
                    response_pay.close()
                except Exception as a:
                    print(a)
            response.close()
        except Exception as w:
            print(w)
        return None


t = C2c().c2c_book
