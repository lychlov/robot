# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     handlers
   Description :
   Author :       Lychlov
   date：          2018/12/3
-------------------------------------------------
   Change Activity:
                   2018/12/3:
-------------------------------------------------
"""
from werobot import WeRoBot

myrobot = WeRoBot(token='loyowanwancc')


# app_id='wx242d734cd4057dc5', app_secret='a1ffde51020438f076e43e3b19973648',
#                   encoding_aes_key='S24igTjZOhFawPXnUbLslXjs4LMwsEEyp7lJ4fUn1xI'

@myrobot.handler
def hello(message):
    print(message)
    return 'Hello World!'
