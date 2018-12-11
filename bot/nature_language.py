# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     nature_language
   Description :
   Author :       Lychlov
   date：          2018/12/11
-------------------------------------------------
   Change Activity:
                   2018/12/11:
-------------------------------------------------
"""
from aip import AipNlp

APP_ID = '15124604'
API_KEY = 'qAgtzsYGbEGiND0brA1dABGD'
SECRET_KEY = 'hZhwHkQipjBnsKYrid7VBE9pNxrNZR71'

client = AipNlp(APP_ID, API_KEY, SECRET_KEY)

result = client.lexer('查询南阳市火车西站告警')
print(result)
