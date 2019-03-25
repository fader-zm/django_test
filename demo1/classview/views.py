from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.utils.decorators import method_decorator

# Create your views here.


def my_decorator(view_fun):
    """自定义装饰器"""
    def wrapper(request, *args, **kwargs):
        print("装饰器被调用了")
        return view_fun(request, *args, **kwargs)
    return wrapper


# 类视图
# @my_decorator 装饰器不能直接装饰类

# 将普通装饰器进行转换成 方法/类 装饰器
# @method_decorator(要进行转换的装饰器, name='要装饰类中的那个方法)
# @method_decorator(my_decorator, name='get')
class DemoView(View):
    """定义类视图"""
    # @my_decorator
    @method_decorator(my_decorator)
    def get(self, request):
        return HttpResponse("classView_get get请求业务逻辑处理")
    
    def post(self, request):
        return HttpResponse("classView_host host请求业务逻辑处理")
# 映射机制 动态查找
# hasattr()  判断类中是否有某个成员(属性和方法) bool
# getattr()  获取类中的属性或方法
# __import__()  # 动态导包





