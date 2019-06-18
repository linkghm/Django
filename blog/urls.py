# -*- coding: utf-8 -*-
# @Time    : 2019/6/18 20:51
# @Author  : GUO Huimin
# @Email   : guohuimin2619@foxmail.com
# @FileName: urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_title),
]
