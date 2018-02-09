# -*- coding:utf-8 -*-
import traceback

author = 'chenshu2'

import threading
from time import ctime,sleep
import datetime


def music(func):
    for i in range(10):
        print (f"I was listening to{func}{ctime()}" )
        sleep(1)
    pass

def move(func):
    for i in range(10):
        print (f"I was listening to{func}{ctime()}" )
        sleep(5)
    pass

threads = []
t1 = threading.Thread(target=music,args=(u'爱情买卖',))
threads.append(t1)
t2 = threading.Thread(target=move,args=(u'阿凡达',))
threads.append(t2)

if __name__ == '__main__':
    start_time = datetime.datetime.now()
    for t in threads:
        t.setDaemon(True)
        t.start()
    end_time = datetime.datetime.now()
    print (f"all over {ctime()}")
    print(f"{end_time - start_time}")
