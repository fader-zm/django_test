from django.conf.urls import url

from . import views


urlpatterns = [
    # url(正则, 视图函数名, 别名)
    # as_view()方法的作用将类中的方法转化成函数, 根据请求方式
    # 动态查找类中的方法
    url(r'^DemoView/$', views.DemoView.as_view(), name="DemoView"),
    # url(r'^DemoView/$', views.my_decorator(views.DemoView.as_view()), name='DemoView'),  # 此写法会将类视图中所有方法进行装饰
    url(r'^TemplateDemo/$', views.TemplateDemo.as_view(), name="TemplateDemo"),
]


