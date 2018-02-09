# -*- coding:utf-8 -*-
author = 'chenshu2'
import requests
from testurl import ip,url
class Query():
    def query_distri_list(self):
        try:
            result = requests.get(url=ip.ord_sit+ "/doi-main/train/distri/queryDistriList")
            result.text
            print(result.text)
            result.close()
        except Exception as  a :
            print(a)
        pass
