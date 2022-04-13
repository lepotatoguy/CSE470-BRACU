from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def index(request):
    user_list = User.objects.all()
    paramters = {'user_list': user_list, }
    return render(request, 'index.html', paramters)
    # return HttpResponse(output)
