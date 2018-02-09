# -*- coding:utf-8 -*-
author = 'chenshu2'


class Sit_cookie():
    def sit_headers(self):
        cookie = "tuniu_partner=MjAxLDAsLGQzN2UwNjg4ZDEyYzVmMmNmYzBlYjMyZGUyMzFkMDQ5; PageSwitch=2%2C1521018859; tuniuuser_citycode=MjUwMA%3D%3D; tuniuuser_id=71656166; rg_entrance=030000%2F010002%2F000015%2F000000; Hm_lvt_ae25642992035099e716fa9b0b1c5636=1511161946; Hm_lpvt_ae25642992035099e716fa9b0b1c5636=1513243276; departCityCode=2500; departCityName=%u4E0A%u6D77; honeydukesUname=6ZmI5pyvMg%3D%3D; honeydukesTelExt=; honeydukesUspelling=chenshu2; honeydukesUid=20243; honeydukesUNum=19464; tuniusub=1; ssoUser=8gi43hvmbue1f2lrhk4m8ktgg0; BSFIT_OkLJUJ=JFKIx49P5oW4WvTfoSPk_nQwvwkLK0cD; fp_ver=4.5.2; BSFIT_EXPIRATION=1513492508347; BSFIT_DEVICEID=V1SN50A-rC7g8RJiCdDrcdNIk16JlfXXhrk_Wz2YtnPX2MJvRKBxI0eB2MIZBifGFnVRSgS4i8zQwUWxT79j41miNJya41q-s20waa3vkALvoJKk0Txe4igMRvddJR5Wm4x3j8CcMw8Izgd9plp1xKzJzOLYAtr4; connect.sid=s%3AbNPxzHhsKdrFx3DVwo3Cxhsjr6_-H4ly.MQp8rwCIhoQcTnQ3tQqxlvJwFvQ%2FFogUHdjL6KGaaeI; isLogined=true; muser=909ee4aaacd17910a8b2ad434263e7cb; TUNIUmuser=909ee4aaacd17910a8b2ad434263e7cb; TRAIN_PHPSESSID=260c3622be0f98088e4535b34e005263; departStationId=1175074; departStationName=%u4E0A%u6D77%u5357%u7AD9; destCityCode=2104; destCityName=%u5305%u5934; destStationId=1175333; destStationName=%u5305%u5934%u4E1C%u7AD9; honeydukesSessionID=ST-2689-oqATJmxndYdREVaWOe6O-cas; departDate=2017-12-20"
        cookies = {}
        for line in cookie.split(';'):
            name, value = line.strip().split('=', 1)
            cookies[name] = value  # 为字典cookies添加内容
        #print(cookies)
        return cookies



