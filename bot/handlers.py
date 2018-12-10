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
import re
from werobot import WeRoBot
from .django_api import check_auth
from .commando_query import call_fx_api
from .alarm_query import old_alarm_query

myrobot = WeRoBot(token='loyowanwancc')


# app_id='wx242d734cd4057dc5', app_secret='a1ffde51020438f076e43e3b19973648',
#                   encoding_aes_key='S24igTjZOhFawPXnUbLslXjs4LMwsEEyp7lJ4fUn1xI'

@myrobot.subscribe
def hello(message):
    return '欢迎您使用“网络维护一点通”！\n' + '您的ID为：' + message.source + '\n请联系管理员添加为内部用户。'


@myrobot.image
@myrobot.voice
def unknown(message):
    return '暂不支持的消息类型，敬请期待。'


@myrobot.filter(re.compile('我的ID'))
def id_check(message):
    return '您的ID是：%s\n请联系管理员注册内部用户' % message.source


@myrobot.filter(re.compile('^10[1-9].*'))
def old_alarm_handler(message):
    source = message.source
    if not check_auth(source):
        return '您不是授权用户，无法使用该功能。'
    content = message.content
    return old_alarm_query(content)


@myrobot.filter(re.compile('^[3-6]0[1-9].*'))
def old_commando_handler(message):
    source = message.source
    content = message.content
    if not check_auth(source):
        return '您不是授权用户，无法使用该功能。'
    result = call_fx_api('chengzhikun', content)
    return result
