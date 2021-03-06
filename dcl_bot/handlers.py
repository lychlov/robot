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
from .mysql_base import SQLExecutor
from .utils import parse_tuple
from werobot.replies import TextReply

dcl_robot = WeRoBot(token='zhdd', app_id='wx373d0151a80c6b6b', )


# app_id='wx242d734cd4057dc5', app_secret='a1ffde51020438f076e43e3b19973648',
#                   encoding_aes_key='S24igTjZOhFawPXnUbLslXjs4LMwsEEyp7lJ4fUn1xI'

@dcl_robot.subscribe
def hello(message):
    return '欢迎您使用“网络维护一点通”！\n' + '您的ID为：' + message.source + '\n请联系管理员添加为内部用户。'


@dcl_robot.filter(re.compile('^yw.*'))
def yw_handler(message):
    sql_executor = SQLExecutor()
    para = message.content[2:]
    result = parse_tuple(sql_executor.executor('yw', para))
    return result


@dcl_robot.filter(re.compile('^jz.*'))
def yw_handler(message):
    sql_executor = SQLExecutor()
    para = message.content[2:]
    result = parse_tuple(sql_executor.executor('jz', para))
    return result


@dcl_robot.filter(re.compile('^jf.*'))
def yw_handler(message):
    sql_executor = SQLExecutor()
    para = message.content[2:]
    result = parse_tuple(sql_executor.executor('jf', para))
    return result


@dcl_robot.filter(re.compile('^wx.*'))
def yw_handler(message):
    sql_executor = SQLExecutor()
    para = message.content[2:]
    result = parse_tuple(sql_executor.executor('wx', para))
    return result

@dcl_robot.filter(re.compile('^lh.*'))
def yw_handler(message):
    sql_executor = SQLExecutor()
    para = message.content[2:]
    result = parse_tuple(sql_executor.executor('lh', para))
    return result

@dcl_robot.image
@dcl_robot.voice
def unknown(message):
    return '暂不支持的消息类型，敬请期待。'


@dcl_robot.filter(re.compile('帮助'))
def help(message):
    return '''
    '''


@dcl_robot.text
def test(message):
    return "get message"
