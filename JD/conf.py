# -*- coding:utf-8 -*-
#10.40.187.32
author = 'chenshu2'

import json, requests, base64


def confirm_ticket():
    url = "http://10.40.189.123:13532/train/confirm"
    data = {
        "apiKey": "CilH5aOmlnN9XTHD1l",
        "sign": "testsign",
        "timestamp": "2016-06-28 09:44:36",
        "data": {
            "retailOrderId": "JD154174873269",
            "orderId": "1067822252"
        }
    }
    try:
        response = requests.post(url=url, data=json.dumps(data))
        print(response.text, )
        response.close()
    except Exception as a:
        print(a)
    pass


def return_ticket():
    url = "http://10.40.189.123:13532/train/return"
    data = {
        "retailOrderId": "JD154174873269",
        "orderId": "1067822252",
        "orderNumber": "EC70341109",
        "callBackUrl": "http://10.10.31.92:18280/train/returnTicketFeedback",
        "tickets": [
            {
                "ticketNo": "EC703411091030051",
                "passengerName": "陈术",
                "passportTypeId": "1",
                "passportNo": "32118119911225353X"
            }
        ]
    }
    p = base64.b64encode(json.dumps(data, ensure_ascii=False).encode("utf-8"))
    url_ = "http://10.40.189.123:13532/test/testEncrypt/CilH5aOmlnN9XTHD1l"
    try:
        re = requests.get(url=url_, params=p)
        re.close()
    except Exception as e:
        print(e)
    data_ = {
        "apiKey": "CilH5aOmlnN9XTHD1l",
        "sign": "testsign",
        "timestamp": "2016-06-28 09:44:36",
        "data": re.text}
    try:
        response = requests.post(url=url, data=data_)
        print(response.text, )
        response.close()
    except Exception as a:
        print(a)
    pass


def cancel_ticket():
    url = "http://10.10.32.203:13532/train/cancelGrabTicket"
    data = {
        "orderId": "1008307778",
        "retailOrderId": "JD2553853206185",
        "userName": None,
        "userPassword": None
    }

    p = base64.b64encode(json.dumps(data, ensure_ascii=False).encode("utf-8"))
    url_ = "http://10.10.32.203:13532/test/testEncrypt/QT5VF0NWBKpWaocYGw"
    try:
        re = requests.get(url=url_, params=p)
        re.close()
    except Exception as e:
        print(e)
    data_ = {
        "apiKey": "QT5VF0NWBKpWaocYGw",
        "sign": "testsign",
        "timestamp": "2016-06-28 09:44:36",
        "data": re.text}
    try:
        response = requests.post(url=url, data=data_)
        print(response.text, )
        response.close()
    except Exception as a:
        print(a)
    pass


def occupy_ticket():
    url = "http://10.40.189.123:13532/train/changeApi/occupy"
    data = {
        "callBackUrl": "http://public-api.ord-train.tuniu.org/train/manage/main/change/occupy/feedback",
        "changeMethod": 0,
        "changeTickets": [
            {
                "passengerId": 1,
                "passengerName": "陈术",
                "passportNo": "32118119911225353X",
                "passportTypeId": "1",
                "passportTypeName": "二代身份证",
                "piaoType": "1",
                "ticketNo": "EB203441781030053"
            }
        ],
        "changeTrainDate": "2018-02-06",
        "changeTrainNo": "K7906",
        "fromStationCode": "BTC",
        "fromStationName": "包头",
        "hasSeat": True,
        "orderId": "1067819912",
        "orderNumber": "EB20344178",
        "retailOrderId": "JD8593628759670",
        "toStationCode": "BDC",
        "toStationName": "包头东",
        "zwCode": "1",
        "zwName": "硬座"
    }
    p = base64.b64encode(json.dumps(data, ensure_ascii=False).encode("utf-8"))
    url_ = "http://10.40.189.123:13532/test/testEncrypt/CilH5aOmlnN9XTHD1l"
    try:
        re = requests.get(url=url_, params=p)
        re.close()
    except Exception as e:
        print(e)
    data_ = {
        "apiKey": "CilH5aOmlnN9XTHD1l",
        "sign": "testsign",
        "timestamp": "2016-06-28 09:44:36",
        "data": re.text}
    try:
        response = requests.post(url=url, data=data_)
        print(response.text, )
        response.close()
    except Exception as a:
        print(a)
    pass


def changeconf_ticket():
    url = "http://10.40.189.123:13532/train/changeApi/confirm"
    data = {
        "retailOrderId": "JD8593628759670",
        "userPassword": "",
        "userName": "",
        "changeId": "18012908526327",
        "orderId": "1067819912",
        "callBackUrl": "http://public-api.ord-train.tuniu.org/train/manage/main/change/confirm/feedback"
    }
    p = base64.b64encode(json.dumps(data, ensure_ascii=False).encode("utf-8"))
    url_ = "http://10.40.189.123:13532/test/testEncrypt/CilH5aOmlnN9XTHD1l"
    try:
        re = requests.get(url=url_, params=p)
        re.close()
    except Exception as e:
        print(e)
    data_ = {
        "apiKey": "CilH5aOmlnN9XTHD1l",
        "sign": "testsign",
        "timestamp": "2016-06-28 09:44:36",
        "data": re.text}
    try:
        response = requests.post(url=url, data=data_)
        print(response.text, )
        response.close()
    except Exception as a:
        print(a)
    pass


if __name__ == '__main__':
    return_ticket()

