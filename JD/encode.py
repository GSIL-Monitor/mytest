# -*- coding:utf-8 -*-
author = 'chenshu2'
import requests, json, base64, pymysql, random,JD.mm,JD.book,JD.grab_book


class Encode():
    # 分销商    table"rdp"."retail"
    fx_apikey = "QT5VF0NWBKpWaocYGw"
    #京东   QT5VF0NWBKpWaocYGw       online :  iytSyCkNGkkKzyTFB4     test:CilH5aOmlnN9XTHD1l
    #翼支付  Q2A07N1IOG6hmdaNfO                KYyCsR58kR7cFmvIBP
    r_order = str(round(random.random() * 10000000000000))
    r_code = str(round(random.random() * 4))
    r_realprice = str(round(random.random() * 30))
    r_price = str(round(random.random() * 100))
    r_num = str(round(random.random() * 3))
    order_jd = "jdchenshu" + r_order
    data = {
        "contact": "137225723",
        "phone": "15000332654",
        "orderNumber": None,
        "passengers": [
            {
                "passengerId": 137225722,
                "ticketNo": "",
                "passengerName": "测试单出不了票的",
                "passportNo": "32118119911253533",
                "passportTypeId": "1",
                "passportTypeName": "二代身份证",
                "piaoType": "1",
                "piaoTypeName": "成人票",
                "zwCode": "1",
                "zwName": "硬座",
                "cxin": None,
                "price": "1.00",
                "procedureFee": None,
                "reason": None,
                "provinceCode": None,
                "schoolCode": None,
                "schoolName": None,
                "studentNo": None,
                "schoolSystem": None,
                "enterYear": None,
                "preferenceFromStationName": None,
                "preferenceFromStationCode": None,
                "preferenceToStationName": None,
                "preferenceToStationCode": None,
                "memo": None,
                "orderNumber": None,
                "code": "231000",
                "msg": None
            }, {
                "passengerId": 1372258722,
                "ticketNo": "",
                "passengerName": "测试单出不了票的",
                "passportNo": "32118119911253539",
                "passportTypeId": "1",
                "passportTypeName": "二代身份证",
                "piaoType": "1",
                "piaoTypeName": "成人票",
                "zwCode": "1",
                "zwName": "硬座",
                "cxin": None,
                "price": "1.00",
                "procedureFee": None,
                "reason": None,
                "provinceCode": None,
                "schoolCode": None,
                "schoolName": None,
                "studentNo": None,
                "schoolSystem": None,
                "enterYear": None,
                "preferenceFromStationName": None,
                "preferenceFromStationCode": None,
                "preferenceToStationName": None,
                "preferenceToStationCode": None,
                "memo": None,
                "orderNumber": None,
                "code": "231000",
                "msg": None
            }
        ],
        "retailOrderId": order_jd,
        "cheCi": "6044",
        "fromStationCode": "CBF",
        "fromStationName": "长治北",
        "toStationCode": "UTP",
        "toStationName": "潞城",
        "trainDate": "2018-01-10",
        "deadLine": "2018-01-09 18:00:00",
        "hasSeat": False,
        "userName": "",
        "userPassword": "",
        "grabType": "1",
        "grabFrequency": "1",
        "grabQueue": "1",
        "grabEntryway": "1",
        "insureCode": None,
        "reservedTrainList": None,
        "callBackUrl": "http://10.10.31.92:18280/train/manage/main/grab/monitor/occupy/feedback",
        "deliveryInfo": {
            "deliveryAddress": "江苏南京玄武区玄武大道途牛大厦",
            "deliveryZipCode": "210000",
            "deliveryName": "高鑫",
            "deliveryPhone": "15895905973"
        },
        "departDepartTime": "08:10",
        "destArriveTime": "08:29",
        "isTicketMonitor": 1,
        "paymentAccount": None,
        "promotionInfo": [{
            "code": r_code,
            "type": "1",
            "price": r_price,
            "realPrice": r_realprice,
            "num": r_num
        }]
    }

    def testEncrypt(self):
        parm = JD.book.data_1
        print(self.r_code, self.r_price, self.r_realprice, self.r_num)
        p = base64.b64encode(json.dumps(parm, ensure_ascii=False).encode("utf-8"))
        url = "http://10.40.189.123:13532/test/testEncrypt/" + self.fx_apikey
        #10.10.30.172:13532
        #10.40.189.123:13521
        #10.40.189.123:13532
        try:
            re = requests.get(url=url, params=p)
            return re.text
        except Exception as e:
            print(e)

    def grabTicketBook(self):
        parm = self.testEncrypt()
        p = {
            "apiKey": self.fx_apikey,
            "sign": "testsign",
            "timestamp": "2016-06-28 09:44:36",
            "data": parm}
        url = "http://10.10.32.203:13532/train/book"
        #book
        #grabTicketBook
        #10.10.32.203:13532
        #10.40.187.32:13521
        #10.40.189.123:13532
        try:
            pp = json.dumps(p, indent=4)
            re = requests.post(url=url, data=pp)
            result = json.dumps(json.loads(re.text), indent=4, ensure_ascii=False)
            #print(url)
            print(result)
        except Exception as e:
            print(e)
        return result

    def getOrder(self):
        try:
            order = json.loads(self.grabTicketBook())["data"]["orderId"]
            # print("订单号：", order)
            return order
        except Exception as e:
            print(e)
        pass

    def selectPromotion_info(self):
        order = self.getOrder()
        # 86_roc
        connect = pymysql.Connect(host="open_roa-master.train.db.tuniu-sst.org", port=3306, user="open_rw",
                                  passwd="tuniu520",
                                  db="open_roc", charset='utf8')
        # 86_roa
        connect_roa = pymysql.Connect(host="open_roa-master.train.db.tuniu-sst.org", port=3306, user="open_rw",
                                      passwd="tuniu520",
                                      db="open_roa", charset='utf8')
        # sit_roc
        sit_connect = pymysql.Connect(host="open_roc-master.db.tuniu-sit.org", port=3306, user="open_rw",
                                      passwd="tuniu520",
                                      db="open_roc", charset='utf8')
        # sit_roa
        sit_connect_roa = pymysql.Connect(host="roa-master.db.tuniu-sit.org", port=3306, user="open_roa_rw",
                                          passwd="tuniu520",
                                          db="open_roa", charset='utf8')
        # sst_roc
        sst_roc_connect = pymysql.Connect(host="roc-master.db.tuniu-sst.org", port=3306, user="roc_rw",
                                          passwd="tuniu520",
                                          db="roc", charset='utf8')
        #链接数据库
        cursor = sst_roc_connect.cursor()
        sql = f"SELECT a.code,a.order_id ,a.price,a.real_price,a.num,b.grab_frequency,b.grab_queue,b.grab_entryway FROM `promotion_info` AS a LEFT JOIN grab_info  AS b ON a.order_id = b.order_id WHERE a.order_id = {order}"
        print("roc新增表数据：")
        try:
            cursor.execute(sql)
            resulte = cursor.fetchall()

            for i in resulte:
                print("id:", i[0], "order_id:", i[1], "price:", i[2], "real_price:", i[3], "num:", i[4],
                      "grab_frequency:", i[5], "grab_quqe:", i[6], "grab_entrway:", i[7])
        except Exception as e:
            print(e)
        finally:
            connect.close()
        pass

if __name__ == '__main__':
    Encode().selectPromotion_info()



