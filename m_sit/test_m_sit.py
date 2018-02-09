# -*- coding:utf-8 -*-
author = 'chenshu2'
# ecoding=utf-8

import requests, urllib.request, json
from m_sit.cookies import Sit_cookie
import datetime


class TestMsit():
    cookie = Sit_cookie().sit_headers()

    headers = {
        'cookie': "tuniu_partner=MjAxLDAsLGQzN2UwNjg4ZDEyYzVmMmNmYzBlYjMyZGUyMzFkMDQ5; PageSwitch=2%2C1521018859; tuniuuser_citycode=MjUwMA%3D%3D; tuniuuser_id=71656166; rg_entrance=030000%2F010002%2F000015%2F000000; Hm_lvt_ae25642992035099e716fa9b0b1c5636=1511161946; Hm_lpvt_ae25642992035099e716fa9b0b1c5636=1513243276; departCityCode=2500; departCityName=%u4E0A%u6D77; honeydukesUname=6ZmI5pyvMg%3D%3D; honeydukesTelExt=; honeydukesUspelling=chenshu2; honeydukesUid=20243; honeydukesUNum=19464; tuniusub=1; ssoUser=8gi43hvmbue1f2lrhk4m8ktgg0; BSFIT_OkLJUJ=JFKIx49P5oW4WvTfoSPk_nQwvwkLK0cD; fp_ver=4.5.2; connect.sid=s%3AbNPxzHhsKdrFx3DVwo3Cxhsjr6_-H4ly.MQp8rwCIhoQcTnQ3tQqxlvJwFvQ%2FFogUHdjL6KGaaeI; isLogined=true; TRAIN_PHPSESSID=260c3622be0f98088e4535b34e005263; departStationId=1175074; departStationName=%u4E0A%u6D77%u5357%u7AD9; destCityCode=2104; destCityName=%u5305%u5934; destStationId=1175333; destStationName=%u5305%u5934%u4E1C%u7AD9; BSFIT_EXPIRATION=1513731328128; BSFIT_DEVICEID=Y4v9dbUIJBR8YKsPoVF6Xfw207v0KSWbgn3bRTwl90q-h0e1IVYNk64mQ6U9AuXzlCVobdW_SyUHWdZluEt6SFGeJgXi1-dhgDE5JVVBCeXtvi1h5F4tvfldjE5jsn0YJgzyoOrUXCY1GXbBaPUP63AWXcbEEFaD; honeydukesSessionID=ST-2689-oqATJmxndYdREVaWOe6O-cas; muser=f2ed4205de42b6b5ba76b85a669d96cf; TUNIUmuser=f2ed4205de42b6b5ba76b85a669d96cf; departDate=2017-12-20",
        'cache-control': "no-cache",
        'postman-token': "5c429414-01a0-071b-1c5a-6d1ed5ac9adc",
        'content-type': "application/json"}

    def g_index(self):
        headers = self.headers
        dict = {"status": "error"}
        try:
            url = "http://m-sit.tuniu.org/m2015/global/index"
            print("首页：", url)
            querystring = "data=%7B%22partner%22%3A%7B%22p%22%3A%22%22%2C%22referer%22%3A%22%22%7D%7D"
            que = urllib.request.unquote(json.dumps(querystring))
            starttime = datetime.datetime.now()
            response = requests.request("GET", url, headers=headers, params=querystring)
            endtime = datetime.datetime.now()
            speed = f"{endtime - starttime}"
            status = response.status_code
            print(status, "\n", json.dumps(response.json(), indent=4))
            if status == 200:
                print("请求成功！")
                print(que)
                dict["status"] = status
                dict["url"] = url
                dict["data"] = que
                dict["result"] = json.dumps(response.json(), indent=4)
                dict["speed"] = speed
            if status != 200:
                print("请求失败！")
                print(que)
            response.close()
        except Exception as a:
            print(a)
        response.close()
        return dict

    def testadListNew(self):
        headers = self.headers
        dict = {"status": "error"}
        try:
            url = "http://m.tuniu.com/api/train/product/adListNew"
            print("广告位：", url)
            querystring = {"d": "%7B%7D"}
            que = urllib.request.unquote(json.dumps(querystring))
            starttime = datetime.datetime.now()
            response = requests.request("GET", url, headers=headers, params=querystring)
            endtime = datetime.datetime.now()
            speed = f"{endtime - starttime}"
            status = response.status_code
            print(status, "\n", json.dumps(response.json(), indent=4))
            if status == 200:
                print("请求成功！")
                print(que)
                dict["status"] = status
                dict["url"] = url
                dict["data"] = que
                dict["result"] = json.dumps(response.json(), indent=4)
                dict["speed"] = speed
            if status != 200:
                print("请求失败！")
                print(que)
            response.close()
        except Exception as a:
            print(a)
        response.close()
        return dict

    def ticketList(self):
        headers = self.headers
        dict = {"status": "error"}
        try:
            url = "http://m-sit.tuniu.org/api/train/product/ticketList"
            print("车次预加载：", url)
            querystring = "d=%7B%22departureCityCode%22:%222500%22,%22arrivalCityCode%22:%222104%22,%22departureCityName%22:%22%E4%B8%8A%E6%B5%B7%22,%22arrivalCityName%22:%22%E5%8C%85%E5%A4%B4%E4%B8%9C%22,%22departureDate%22:%222017-12-19%22%7D"
            que = urllib.request.unquote(json.dumps(querystring))
            starttime = datetime.datetime.now()
            response = requests.request("GET", url, headers=headers, params=querystring)
            endtime = datetime.datetime.now()
            speed = f"{endtime - starttime}"
            status = response.status_code
            print(status, "\n", json.dumps(response.json(), indent=4))
            if status == 200:
                print("请求成功！")
                print(que)
                dict["status"] = status
                dict["url"] = url
                dict["data"] = que
                dict["result"] = json.dumps(response.json(), indent=4)
                dict["speed"] = speed
            if status != 200:
                print("请求失败！")
                print(que)
            response.close()
        except Exception as a:
            print(a)
        response.close()
        return dict

    def contacts(self):
        headers = self.headers
        dict = {"status": "error"}
        try:
            url = "http://m-sit.tuniu.org/api/train/order/contacts"
            print("填写默认保险：", url)
            querystring = "d=%7B%22departDate%22%3A%222017-12-19%22%2C%22adultPrice%22%3A236%2C%22trainTicketBusinessType%22%3A%22DIRECT%22%2C%22pValue%22%3A%22201%22%7D"
            que = urllib.request.unquote(json.dumps(querystring))
            starttime = datetime.datetime.now()
            response = requests.request("GET", url, headers=headers, params=querystring)
            endtime = datetime.datetime.now()
            speed = f"{endtime - starttime}"
            status = response.status_code
            print(status, "\n", json.dumps(response.json(), indent=4))
            if status == 200:
                print("请求成功！")
                print(que)
                dict["status"] = status
                dict["url"] = url
                dict["data"] = que
                dict["result"] = json.dumps(response.json(), indent=4)
                dict["speed"] = speed
            if status != 200:
                print("请求失败！")
                print(que)
            response.close()
        except Exception as a:
            print(a)
        response.close()
        return dict

    def getComboSwitch(self):
        headers = self.headers
        dict = {"status": "error"}
        try:
            url = "http://m-sit.tuniu.org/api/train/product/getComboSwitch"
            print("默认红包套餐：", url)
            querystring = "d=%7B%22cfgName%22%3A%22page_show_channel%22%7D"
            que = urllib.request.unquote(json.dumps(querystring))
            starttime = datetime.datetime.now()
            response = requests.request("GET", url, headers=headers, params=querystring)
            endtime = datetime.datetime.now()
            speed = f"{endtime - starttime}"
            status = response.status_code
            print(status, "\n", json.dumps(response.json(), indent=4))
            if status == 200:
                print("请求成功！")
                print(que)
                dict["status"] = status
                dict["url"] = url
                dict["data"] = que
                dict["result"] = json.dumps(response.json(), indent=4)
                dict["speed"] = speed
            if status != 200:
                print("请求失败！")
                print(que)
            response.close()
        except Exception as a:
            print(a)
        response.close()
        return dict

    def AddOrder(self):
        headers = self.headers
        dict = {"status": "error"}
        try:
            url = "http://m-sit.tuniu.org/api/train/order/AddOrder"
            print("php下单：", url)
            s = {
                "trainId": 35282,
                "trainNumber": "Z282",
                "departDate": "2017-12-20",
                "departureStationName": "上海南",
                "arrivalStationName": "包头东",
                "seatId": 8,
                "resourceId": 31388245,
                "adultCount": 1,
                "childCount": 0,
                "adultPrice": 236,
                "departureCityCode": 2500,
                "arrivalCityCode": 2104,
                "departureCityName": "上海",
                "arrivalCityName": "包头东",
                "acceptStandingTicket": False,
                "ministryRailwaysId": 1681,
                "contactList": {
                    "name": "",
                    "appellation": "",
                    "email": "",
                    "phone": "",
                    "tel": "13584089726"
                },
                "touristList": [
                    {
                        "name": "孙新建",
                        "psptType": "1",
                        "psptName": "身份证",
                        "psptId": "210282199008039117",
                        "birthday": "1990-08-03",
                        "sex": "",
                        "isAdult": 1,
                        "relatedTouristName": "",
                        "contacterId": "1935022"
                    }
                ],
                "insuranceResourceId": None,
                "insurancePrice": None,
                "receiverName": "",
                "address": "",
                "telNum": "",
                "zipCode": "",
                "isExcess": 0,
                "buyPromotionResources": [

                ],
                "isInsCashBack": 0,
                "extension": {
                    "voucherInfo": [

                    ]
                },
                "personalTailorInfo": {
                    "info": ""
                },
                "isCouponValuable": 0,
                "travelCouponUseValue": 0,
                "verificationCode": "",
                "travelCouponId": "",
                "promotionList": [

                ],
                "useTrainUniquePromotion": False,
                "isTransferToDispatchTicket": 0
            }
            data = json.dumps(s)
            d = data.encode("utf-8").decode("utf-8")
            dd = json.loads(d)
            # print(d)
            response = requests.post(url=url, data=data, headers=headers)
            status = response.status_code

            print(status, "\n", json.dumps(response.json(), indent=4, ensure_ascii=False))

            if status != 200:
                print("请求失败！")
            response.close()
        except Exception as a:
            print(a)
        response.close()
        return None

    def trainTicketOrderDetailAjax(self):
        headers = self.headers
        dict = {"status": "error"}
        try:
            url = "http://m-sit.tuniu.org/userOrder/trainTicketOrderDetailAjax"
            print("异步查询订单状态：", url)
            querystring = "data=%7B%22orderId%22%3A%221019620143%22%2C%22orderType%22%3A%2238%22%7D"
            que = urllib.request.unquote(json.dumps(querystring))
            starttime = datetime.datetime.now()
            response = requests.request("GET", url, headers=headers, params=querystring)
            endtime = datetime.datetime.now()
            speed = f"{endtime - starttime}"
            status = response.status_code
            print(status, "\n", json.dumps(response.json(), indent=4))
            if status == 200:
                print("请求成功！")
                print(que)
                dict["status"] = status
                dict["url"] = url
                dict["data"] = que
                dict["result"] = json.dumps(response.json(), indent=4)
                dict["speed"] = speed
            if status != 200:
                print("请求失败！")
                print(que)
            response.close()
        except Exception as a:
            print(a)
        response.close()
        return dict

    def run(self):

        aa = self.g_index()
        a = self.testadListNew()
        b = self.ticketList()
        c = self.contacts()
        d = self.getComboSwitch()
        # self.AddOrder()
        e = self.trainTicketOrderDetailAjax()
        print("\n", "***************运***************行***************结***************果***************：")
        print("首页：", aa["status"], aa["speed"],aa["data"])
        print("广告位：",a["status"], a["speed"])
        print("车次预加载：",b["status"], b["speed"])
        print("填写默认保险：",c["status"], c["speed"])
        print("默认红包套餐：",d["status"], d["speed"])
        print("异步查询订单状态：",e["status"], e["speed"])
        return None
