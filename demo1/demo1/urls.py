"""demo1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from users import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),  # 后台管理路由
    
    # 注册子应用的路由
    url(r'^users/', include('users.urls')),
    
    # 注册路由的三种方式
    # 1. 把子应用中的所有路由都注册在总路由/根路由中
    # url(r'^', include('users.urls')),
    # 2. 只在总路由中定义路由
    # url(r'^users/index/$', views.index)
]
