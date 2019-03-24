from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.

import json

"""Django中的视图函数不需要指定请求方法, 只要路由匹配成功都可以调用
    查询字符串无论是get请求还是post请求都可以, 但一般都是get请求带查询字符串"""


# GET /beijing/2018
def weather(request):
    """获取url路径参数数据"""
    return HttpResponse("weather")


# GET weather/beijing/2018
def weather1(request, city, year):
    """获取url路径参数数据"""
    print(city)
    print(year)
    return HttpResponse("weather1")


# GET /beijing/2018
def weather2(request, year, city):
    """获取url路径参数数据"""
    print(city)
    print(year)
    return HttpResponse("weather2")


# GET /get_query_params?name=zs&age=18&name=li
def get_query_params(request):
    """获取url查询字符串数据"""
    # request.GET 后面大写的GET是一个请求对象的属性而已, 与请求方式无关, Query_dict 类型对象
    query_dict = request.GET
    # 一个取一个值, 当有多个值时, 默认取最后一个
    print(query_dict.get('name'))
    print(query_dict.get('age'))
    # 一次取多个值, 返回列表
    print(query_dict.getlist('name'))
    return HttpResponse("get_query_params")


# POST /get_from_data
# request.POST 用来获取请求体中的表单数据, 大写的POST只是一个属性而已,和请求方法无关, QueryDict类型对象
def get_from_data(request):
    """获取请求体表单数据"""
    query_dict = request.POST
    print(query_dict.get('name'))
    print(query_dict.get('age'))
    print(query_dict.getlist('name'))
    return HttpResponse('get_from_data')


# POST /get_json_data
def get_json_data(request):
    """获取请求体中的非表单数据: json"""
    json_types = request.body
    json_str = json_types.decode()
    req_data = json.loads(json_str)  # 将json字符串转换成json字典或json列表
    print(req_data)
    return HttpResponse("get_json_data")


# GET /get_user/
def get_user(request):
    """获取当前请求对象"""
    # 当前如果没有登录获取 request.user 会是一个匿名用户AnonymousUser
    # 如果当前登录了,request.user 获取到当前登录的用户对象 zhangsan
    print(request.user)
    return HttpResponse('get_user')


# GET /response_demo/
def response_demo(request):
    """响应对象的基本操作"""
    # return HttpResponse("response_demo", content_type="text/html", status=200)
    # return HttpResponse("response_demo", content_type="text/plain", status=201)
    # 自定义响应头
    response = HttpResponse('hello')
    response['itcase'] = 'muye'
    return response


def response_json(request):
    """响应json数据"""
    json_data = [{"name": "zs", "age": 18}, "haha"]
    dict = {"dict": json_data}
    return JsonResponse(dict)

