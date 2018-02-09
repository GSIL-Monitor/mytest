# -*- coding:utf-8 -*-
author = 'chenshu2'
import pymysql
#port   int
connect = pymysql.Connect(host="roc-master.db.tuniu-sst.org", port=3306, user="roc_rw", passwd="tuniu520",
                                  db="roc", charset='utf8')
cur = connect.cursor()

