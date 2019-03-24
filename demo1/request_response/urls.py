from django.conf.urls import url

from . import views


# 注意: urlpatterns是[] 不是 {}
urlpatterns = [
    # url(r'^weather/$', views.weather)
    
    # url(r'weather/beijing/2018', views.weather)
    # 使用正则组提取 url路径参数 位置参数
    # url(r'^weather/([a-z]+)/(\d+)$', views.weather1)
    # 利用正则组起别名, 提取url路径参数  关键字参数
    # 如果给正则组起了别名, 那么对应的形参名必须和别名一致
    url(r'^weather/(?P<city>[a-z]+)/(?P<year>\d+)/$', views.weather2),
    
    # 获取查询字符串
    url(r'^get_query_params/$', views.get_query_params),
    
    # 获取请求体的表单数据
    url(r'^get_from_data/$', views.get_from_data),
    
    # 获取请求体中的非表单数据 json
    url(r'^get_json_data/$', views.get_json_data),
    
    # 获取当前请求对象
    url(r'^get_user/$', views.get_user),
    
    # 响应对象的基本操作
    url(r'^response_demo/$', views.response_demo),
    
    # 响应json 数据
    url(r'^response_json/$', views.response_json,  name="response_json"),
    # url(r'^response_json/$', views.response_json),
    
    # 反向解析 reverse, 传入的参数是
    url(r'^reverse_demo/$', views.reverse_demo),
    
    # 重定向
    url(r'^redirect_demo/$', views.redirect_demo),
    
    # cokice 的读写操作
    url(r'^cookice_demo/$', views.cookice_demo),
    
    # session 的读写操作
    url(r'^session_demo/$', views.session_demo),
]
