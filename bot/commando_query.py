# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     commando_query
   Description :
   Author :       Lychlov
   date：          2018/12/6
-------------------------------------------------
   Change Activity:
                   2018/12/6:
-------------------------------------------------
"""
from suds.client import Client

BASE_URL = 'http://10.217.8.189:8081/fmaster-henan-web/MessageProcess?wsdl'

client = Client(url=BASE_URL)


def call_fx_api(open_id, commando):
    try:
        result = client.service.process(open_id, commando, False)
        return result.replace('<result><text>', '').replace('</text></result>', '')
    except:
        return '指令输入错误！'
