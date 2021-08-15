# -*- coding: utf-8 -*-
# Time       : 2021/3/10 22:40
# Author     : pein
# Email      : lihuazhang@live.com
# File       : middleware.py
# Project    : seeyes
# Functional :
from django.shortcuts import render, HttpResponse, redirect
from django.utils.deprecation import MiddlewareMixin
from django.conf import settings
import re


class VerifyPermissions(MiddlewareMixin):
    # white list
    whitelist = ['login/']

    def process_view(self, request, view_func, view_args, view_kwargs):
        """
        根据中间中process_*方法执行的顺序，process_view方法是在请求到达urls.py之后在执行view.py视图函数之前执行的
        使用process_view方法不使用process_request是因为如果用户输入了找不到的路径，可以先提示404，不会先提示权限问题
        """
        current_url = request.path
        for url in self.whitelist:
            if not current_url.startswith(url):
                token = request.META.get("HTTP_TOKEN")
                if not token:
                    return HttpResponse('404')
                user = request.session.get("user", None)
                if not user:
                    return redirect('/login/?next={}'.format(current_url))

        # 从session中获取权限列表
        permissions_list = request.session.get('permissions_list', [])
        # 校验是否是权限内的内容,如果不是提示权限不够
        for url in permissions_list:
            ret = re.fullmatch(url['url'], current_url)
            if ret:
                return
        else:
            return HttpResponse('Permission denied !')

