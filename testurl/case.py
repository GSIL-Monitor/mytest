# -*- coding:utf-8 -*-
author = 'chenshu2'
import json
import base64, requests

# 余位查询
data1 = {
    "trainDate": "2017-12-13",
    "fromStation": "上海",
    "toStation": "南京",
    "isReal": True
}
# 火车票BOSS下单  1435981056   上海南到南京sst  1435977552   sit 31070000
data2 = {
    "mainOrderId": None,
    "memberId": 71656166,
    "userType": None,
    "source": 3,
    "productClassId": 18,
    "bookCityCode": 2500,
    "resources": [
        {
            "resourceId": 31070000,
            "resourceType": 8,
            "departsDate": "2018-01-19",
            "adultPrice": 46.5
        }
    ],
    "insuranceResources": [

    ],
    "buyPromotionResources": [

    ],
    "adultTourists": [
        {
            "name": "car",
            "psptType": 1,
            "psptId": "32118119911225353X",
            "birthday": "1991-12-25",
            "childTourists": None,
            "isStuDisabledArmyPolice": 0,
            "stu": None
        },
        {
            "name": "陈术",
            "psptType": 1,
            "psptId": "430522199610291412",
            "birthday": "1996-10-29",
            "childTourists": None,
            "isStuDisabledArmyPolice": 0,
            "stu": None
        }
    ],
    "adultTicketNum": 2,
    "childTicketNum": 0,
    "contact": {
        "name": "",
        "appellation": 0,
        "email": "",
        "phone": "",
        "tel": "13062527078"
    },
    "acceptStandingTicket": False,
    "travelVoucherCouponValue": 0,
    "travelCouponId": 0,
    "promotionIds": None,
    "deviceId": "",
    "versionId": "0.0.0",
    "delivery": {
        "receiverName": "",
        "telNum": "",
        "phoneNum": "",
        "mailAddress": "",
        "deliveryEndAddress": "",
        "deliveryTime": None,
        "zipCode": "",
        "fabDeliveryId": 0,
        "deliveryPrice": 0.0,
        "memberId": 0,
        "deliveryType": -1,
        "provinceCode": 0,
        "provinceName": "",
        "cityCode": 0,
        "cityName": "",
        "remark": "",
        "invoiceTitle": None,
        "isDispatchTicket": 0
    },
    "channelData": {
        "pValue": 27223,
        "pExt": "__",
        "pSource": 1,
        "clientType": 40000,
        "clientTypeExpand": 0,
        "innerNum": "0",
        "callPhone": "",
        "fromUrl": "",
        "clientId": None,
        "deviceId": "",
        "clientIp": None,
        "version": "",
        "channelCode": "10",
        "terminalCode": "32",
        "operatingSystemCode": None,
        "appCode": "100",
        "wechatCode": "0",
        "partnerCode": "100000",
        "channelRelationId": "010100000032"
    },
    "isChildBuyInsurance": 1,
    "isTransferToDispatchTicket": 0,
    "isDispatchTicket": 0,
    "dispatch": {
        "receiverName": "",
        "telNum": "",
        "phoneNum": "",
        "mailAddress": "",
        "deliveryEndAddress": "",
        "deliveryTime": None,
        "zipCode": "",
        "fabDeliveryId": 0,
        "deliveryPrice": 0.0,
        "memberId": 0,
        "deliveryType": 1,
        "provinceCode": 0,
        "provinceName": "",
        "cityCode": 0,
        "cityName": "",
        "remark": "",
        "invoiceTitle": None,
        "isDispatchTicket": 0
    },
    "personalTailor": {
        "orderId": None,
        "isConnecting": None,
        "connectingNum": None,
        "info": None,
        "isSameRoom": None,
        "topNum": None,
        "middleNum": None,
        "lowerNum": None,
        "acceptOthers": None,
        "nextWindowNum": None,
        "otherRequirement": None
    },
    "ministryRailwaysId": 0,
    "useTrainUniquePromotion": None,
    "grab": None,
    "isExcess": 0,
    "alternateTrainResources": None,
    "isInsCashBack": 0,
    "storeInfo": None,
    "extension": {
        "memberRightsInfo": [{
            "hasBuyMemberRights": False,
            "type": 1,
            "resId": 199,
            "beneficiaryVos": [{
                "memberName": "张美娟",
                "memberIdType": "B",
                "memberIdNo": "h15656165"
            },{
                "memberName": "陈术",
                "memberIdType": "B",
                "memberIdNo": "h15656165"
            }]
        }]
    }
}
# 支付订单
data3 = {
    "orderId": 1019621079,
    "payCardNum": "123546",
    "pay": 1000,
    "payTotal": 1000,
    "lastPayTime": "2016-07-06 16:27:20"
}

# 更新会员信息
data4 = {
    "id": 56,
    "memberName": "陈术",
    "memberIdType": "1",
    "memberIdNo": "32118119911225353x",
    "activeFlag": 0
}

# 查询是否会员
data5 = {
    "memberId": 667573
}

# 退票接口 tour不传就是全部退票
data6 = {
    "orderId": 1019620293,
    "touristIds": []
}

# 抢票下单
datagrab = {
  "mainOrderId": 0,
  "memberId": 21648666,
  "source": 0,
  "productClassId": 18,
  "bookCityCode": 2104,
  "resources": [
    {
      "resourceId": 31070000,
      "resourceType": 8,
      "departsDate": "2018-02-20",
      "adultPrice": 553
    }
  ],
  "insuranceResources": None,
  "buyPromotionResources": None,
  "adultTourists": [
    {
      "name": "陈术",
      "psptType": 1,
      "psptId": "32118119911225353X",
      "birthday": "1991-12-25",
      "childTourists": [
        
      ],
      "isStuDisabledArmyPolice": 0,
      "stu": {
        "stuProvince": None,
        "stuSchoolName": None,
        "stuCollege": None,
        "stuClass": None,
        "stuNumber": None,
        "stuSchoolSystem": None,
        "stuSchoolYear": None,
        "stuTrainNumber": None,
        "stuTrainCity1": None,
        "stuTrainCity2": None
      }
    }
  ],
  "adultTicketNum": 1,
  "childTicketNum": 0,
  "contact": {
    "name": "",
    "appellation": 0,
    "email": "",
    "phone": "",
    "tel": "15295115732"
  },
  "acceptStandingTicket": True,
  "travelVoucherCouponValue": None,
  "travelCouponId": None,
  "promotionIds": None,
  "deviceId": None,
  "versionId": None,
  "delivery": None,
  "channelData": {
    "pValue": 0,
    "pExt": "",
    "pSource": 0,
    "clientType": 10000,
    "clientTypeExpand": None,
    "innerNum": "",
    "callPhone": "",
    "fromUrl": "",
    "clientId": None,
    "deviceId": None,
    "clientIp": None,
    "version": ""
  },
  "isChildBuyInsurance": 0,
  "isTransferToDispatchTicket": 0,
  "isDispatchTicket": 0,
  "dispatch": {
    "receiverName": "",
    "telNum": "",
    "phoneNum": "",
    "mailAddress": "",
    "deliveryEndAddress": "",
    "deliveryTime": None,
    "zipCode": "",
    "fabDeliveryId": 0,
    "deliveryPrice": 0.0,
    "memberId": 0,
    "deliveryType": 0,
    "provinceCode": 0,
    "provinceName": "",
    "cityCode": 0,
    "cityName": "",
    "remark": "",
    "invoiceTitle": None,
    "isDispatchTicket": 0
  },
  "personalTailor": None,
  "ministryRailwaysId": 0,
  "useTrainUniquePromotion": None,
  "grab": {
    "deadline": "2018-01-17 23:00:00",
    "rate": 0,
    "grabSourceType": 1
  },
  "isExcess": 0
}

# 出票成功有退款
datamanage1 = {
    "template_id": 11,
    "content": "购票成功，[departDate][departTime] [departStationName] - [destStationName][trainNum]次列车，取票号[takeOutTicketNo]，[seatTypeName]，[seatInfo]，开车前凭购票证件原件在火车站或代售点取票[checkInPortMess]。退还差额[totalRefundAmount]元，1~7个工作日退回原支付账号。租车接送特惠：http://tuniu.cc/t/GPtO23"
}

# 出票成功无退款
datamanage2 = {
    "template_id": 10,
    "content": "购票成功，[departDate][departTime] [departStationName] - [destStationName][trainNum]次列车，取票号[takeOutTicketNo]，[seatTypeName]，[seatInfo]，开车前凭购票证件原件在火车站或代售点取票[checkInPortMess]。租车接送特惠：http://tuniu.cc/t/GPtO23"
}

# 权益次数减少1次的接口
datadecrease = {
    "basicId": 7,
    "memberId": 6675783,
    "detailType": 1
}

# 权益成本支出入库的接口
datasavecostinfo = {
    "basicId": 55,
    "memberId": 6648,
    "detailType": 1,
    "cost": 100
}

# 修改黄金权益特权新会员入11项特权+老会员增加3项特权
dataxinzeng11 = {
    "cfgName": "train_member_rights_config",
    "cfgKey": "member_rights_times_1",
    "cfgValue": "1#3,2#3,3#3,4#3,5#3,6#3,7#3,8#3,9#3,10#3,11#3",
    "delFlag": 0,
    "memo": "199/年，会员权益使用次数，权益类型#剩余次数"
}

# 修改钻石权益特权入11项特权+老会员增加3项特权
dataxinzengzuanshi11 = {
    "cfgName": "train_member_rights_config",
    "cfgKey": "member_rights_times_9",
    "cfgValue": "1#999,2#24,3#999,4#999,5#999,6#999,7#999,8#999,9#12,10#999,11#999",
    "delFlag": 0,
    "memo": "999/年，会员权益使用次数，权益类型#剩余次数"
}

# 更新doi配置
datadoiconfig = {
    "cfgName": "seat_selection_config",
    "cfgKey": "changeChooseSwitch",
    "cfgValue": "1 注：1代表开， 0代表关",
    "delFlag": 0,
    "memo": "改签选座开关#控制M站和APP端，改签是否漏出选座"
}
'''
数据中心反刷接口开关
{
    "cfgName": "crawl_12306_data_switch",
    "cfgKey": "0",
    "cfgValue": "1",
    "delFlag": 0,
    "memo": "APP反刷火车票数据开关"
}
'''
