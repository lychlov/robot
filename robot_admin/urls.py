# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     urls
   Description :
   Author :       Lychlov
   date：          2018/12/6
-------------------------------------------------
   Change Activity:
                   2018/12/6:
-------------------------------------------------
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('alarms',views.alarms,name='alarms'),
]
