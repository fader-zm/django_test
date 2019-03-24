from django.shortcuts import render, reverse, redirect
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

    # 如果响应的json数据不是字典面是列表 要么 多指定safe=False 或者把列表包装成字典格式
    json_data = [{"name": "zs", "age": 18}, "haha"]
    dict = {"dict": json_data}
    return JsonResponse(dict)


# GET /redirect_demo/
def reverse_demo(request):
    """反向解析"""
    # if 判断当前是不是登录用户,如果是 返回用户中心界面数据
    #     else:

    # print(reverse('index')) # /json_response_demo_xxxx/  没有设置命名空间时,可以用路由别名进行反向解析,它是全局查找
    # 如果设置了命名空间后,那么这个子应用中进行反向解析时 写法 (命名空间:路由别名)
    # reverse : 反向解析, 传入的参数必须是视图的别名
    print(reverse('request_response:response_json'))
    return HttpResponse("reverse_demo")


# GET /redirect_demo/
def redirect_demo(request):
    """重定向"""
    # /redirect_demo/reverse_demo/ 在路由最前面加/ 代表从根路由进行重定向,如果没有加/ 那么就是从当前路由拼接后面的路由再进行定向
    # return redirect('reverse_demo/')
    # return redirect('/reverse_demo/')
    return redirect(reverse('request_response:response_json'))
    

# GET /cookice_demo/
def cookice_demo(request):
    """cookice读写操作"""
    # cookice 在response对象上设置, request对象读取
    response = HttpResponse("ok")
    response.set_cookie("name", "zs", max_age=3600)  # 设置 cookice
    # response.delete_cookie("name")  # 删除 cookice
    print(request.COOKIES.get("name"))  # None ... zs
    return response


# GET /session_demo/
def session_demo(request):
    """session 读写操作"""
    # session依赖于cookice
    # 当代码执行到这行时, 会将session设置到redis数据库中
    # 同时, redis数据库会生成一个session_id, 把session_id 通过后期的响应对象设置到浏览器的cookice中
    # session通过 request请求对象来设置
    request.session['name'] = 'zhangsan'  # 设置session
    
    # 先通过请求对象读取到cookice中的session_id, 然后在通过session_id读取到redis数据库中的session记录
    # 在通过name key获取value
    print(request.session.get('name'))  # 读取session
    return HttpResponse("session_demo")
    

