from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    """
    index: 视图函数, 至少有一个参数
    :param request: 接收请求对象, 类型HttpRequest
    :return: 响应请求对象
    """
    return HttpResponse("hello world")


def say(request):
    return HttpResponse('say')


def say_hello(request):
    return HttpResponse('say_hello')


