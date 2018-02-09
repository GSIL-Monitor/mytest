# -*- coding:utf-8 -*-
author = 'chenshu2'
import base64
import json


class Func():
    def testPrint(self,re):
        print("请求结果：", json.loads(re)["success"], "\n" )
        for i in re:
            j = re.index(i)
            if i == "," or i == "{" or i == "}" or i == "[" or i == "]":
                print(i)
            else:
                print(i, end="")

    def b64(self, data: object) -> object:
        data = data
        d = json.dumps(data)
        bd = d.encode()
        dd = base64.b64encode(bd)
        return  dd