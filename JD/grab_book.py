# -*- coding:utf-8 -*-
author = 'chenshu2'
import random

aa = str(round(random.random() * 10000000000000))
a = "JD" + aa
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
        }
    ],
    "retailOrderId": a,
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
        "code": "1",
        "type": "1",
        "price": "10",
        "realPrice": "10",
        "num": 2
    }]
}

#抢票有座
data_grab = {
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
            "zwCode": "4",
            "zwName": "软卧",
            "cxin": None,
            "price": "78.00",
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
    "retailOrderId": a,
    "cheCi": "K7906",
    "fromStationCode": "BTC",
    "fromStationName": "包头",
    "toStationCode": "BDC",
    "toStationName": "包头东",
    "trainDate": "2018-02-18",
    "deadLine": "2018-01-24 18:00:00",
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
        "code": "1",
        "type": "1",
        "price": "10",
        "realPrice": "10",
        "num": 2
    }]
}