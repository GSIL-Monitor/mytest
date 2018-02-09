# -*- coding:utf-8 -*-
author = 'chenshu2'

import requests, json, threading,datetime
from JD.encode import Encode


def get_promotioninfos():
    url = "http://10.10.30.172:13532/train/promotionInfos"
    data = {
        "apiKey": "QT5VF0NWBKpWaocYGw",
        "sign": "testsign",
        "timestamp": "2017-08-03 11:11:11",
        "data": {
            "type": "1"
        }
    }
    data_ = json.dumps(data)
    req = requests.post(url=url, data=data_)
    print(req.status_code, req.elapsed.microseconds / 1000, "ms")
    req.close()
    pass
def book_grab():
    s_time = datetime.datetime.now()
    t = Encode().grabTicketBook()
    e_time = datetime.datetime.now()
    load_time = (e_time-s_time)
    return load_time

if __name__ == '__main__':
    threads = []
    start_time = datetime.datetime.now()
    for i in range(100):
        t = threading.Thread(target=book_grab())
        t.start()
    end_time = datetime.datetime.now()
    print(end_time - start_time)
    print(threads)






