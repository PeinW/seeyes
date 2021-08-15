from django.forms import model_to_dict
from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout
from user.models import User
import pprint
from django.core.paginator import Paginator


class Login(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'login.html')

    def post(self, request, *args, **kwargs):
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        user = authenticate(phone=phone, password=password)
        if user:
            login(request, user)
            next_url = request.GET.get('next')
            if next_url:
                return redirect(next_url)
            else:
                return redirect('/index/')
        else:
            return render(request, 'login.html', {'errmsg': 'phone or password error'})


def logout_custom(request):
    logout(request)
    return render(request, 'login.html')
