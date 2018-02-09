# -*- coding:utf-8 -*-
author = 'chenshu2'
import json,base64,requests,pymysql,time
import JD.book
'''
测试京东普通下单出票退票
只支持一个乘客退票
'''
#api分销商京东data加密
jd_key="QT5VF0NWBKpWaocYGw"
#QT5VF0NWBKpWaocYGw
#iytSyCkNGkkKzyTFB4
def test_encode(data):
    if type(data) != dict:
        print("类型错误")
        exit()
    parm = json.dumps(data,ensure_ascii=False)
    p = base64.b64encode(parm.encode(encoding='utf-8'))
    try:
        re = requests.get(url="http://10.10.32.203:13532/test/testEncrypt/"+jd_key,params=p)
        re_result = re.text
        re.close()
    except Exception as a :
        print("加密错误！！")
    return re_result

#京东分销商下普通单占位
def test_book(ob):
    data = {
        "apiKey": "QT5VF0NWBKpWaocYGw",
        "sign": "testsign",
        "timestamp": "2016-06-28 09:44:36",
        "data": test_encode(ob)}
    try:
        re = requests.post(url="http://10.10.32.203:13532/train/book",data=data)
        result = re.text
        print(result)
    except Exception as a :
        print("下单占位报错！！")
        exit()
    time.sleep(15)
    return result

#京东确认出票
def test_conf(ob):
    orderinfo = []
    retailid = json.loads(test_book(ob))["data"]["retailOrderId"]
    if type(retailid) != str:
        print("确认出票失败！")
        exit()
    try:
        sit_connect = pymysql.Connect(host="open_roc-master.db.tuniu-sit.org", port=3306, user="open_rw",
                                      passwd="tuniu520",
                                      db="open_roc", charset='utf8')
        cursor = sit_connect.cursor()
        sql = f"SELECT * FROM order_info where retail_order_id = '{retailid}'"
        cursor.execute(sql)
        orderid = str(cursor.fetchone()[1])
        cursor.close()
    except Exception as a :
        print("sql错误！！")
        exit()
    data = {
            "apiKey": jd_key,
            "sign": "testsign",
            "timestamp": "2016-06-28 09:44:36",
            "data": {
            "retailOrderId": retailid,
            "orderId": orderid
        }
    }
    orderinfo.append(retailid)
    orderinfo.append(orderid)
    try:
        re = requests.post(url="http://10.10.32.203:13532/train/confirm",data=json.dumps(data))
        re.text
        print(re.text)
        re.close()
        time.sleep(10)
    except Exception as a :
        print("确认出票报错！！")
        exit()
    exit()
    if orderinfo[1] != None:
        return orderinfo
    else:
        return None

#京东分销退票
def test_return(ob):
    get_orderinfo = test_conf(ob)
    if get_orderinfo == None:
        print("退票失败！！")
        exit()
    try:
        sit_connect = pymysql.Connect(host="open_roc-master.db.tuniu-sit.org", port=3306, user="open_rw",
                                      passwd="tuniu520",
                                      db="open_roc", charset='utf8')
        cursor = sit_connect.cursor()
        sql = f"SELECT * FROM `ticket_info` WHERE order_id = {get_orderinfo[1]}"
        cursor.execute(sql)
        ticket_number = str(cursor.fetchone()[6])
        cursor.close()
    except Exception as a:
        print("sql错误！！")
        exit()
    return_data = {
        "retailOrderId": get_orderinfo[0],
        "orderId": get_orderinfo[1],
        "orderNumber": "EC73089332",
        "callBackUrl": "http://10.10.31.92:18280/train/returnTicketFeedback",
        "tickets": [
            {
                "ticketNo": ticket_number,
                "passengerName": "陈术",
                "passportTypeId": "1",
                "passportNo": "32118119911225353X"
            }
        ]
    }
    data = {
        "apiKey": "QT5VF0NWBKpWaocYGw",
        "sign": "testsign",
        "timestamp": "2016-06-28 09:44:36",
        "data": test_encode(return_data)}
    try:
        re = requests.post(url="http://10.10.32.203:13532/train/return",data=data)
        print(re.text)
    except Exception as a :
        print("退票失败！！")
    time.sleep(10)
    select_rfb_collection(get_orderinfo[1])
    pass

#pop查询收退款订单是否生成
def select_rfb_collection(order_id):
    if order_id == None:
        print("获取订单失败！！")
        exit()
    try:
        connect = pymysql.Connect(host="open_rdp-master.db.tuniu-sit.org", port=3306, user="open_rw",
                                      passwd="tuniu520",
                                      db="open_rfb", charset='utf8')
        cursor = connect.cursor()
        sql = f"SELECT a.pop_collection_id,a.collection_record_id,b.pop_refund_id,b.refund_record_id FROM rfb_collection AS a LEFT JOIN `rfb_refund` AS b ON a.order_id = b.order_id WHERE a.order_id ={order_id}"
        print(sql)
        cursor.execute(sql)
        print(cursor.fetchone())
        connect.close()
    except Exception as a :
        print("sql执行失败！！")
    pass


if __name__ == '__main__':
    test_return(JD.book.data_1)