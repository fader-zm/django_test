from django.conf.urls import url
from rest_framework.routers import DefaultRouter

# from . import serializers
from . import views
urlpatterns = [
    # url(r'^books/$', views.BookListView.as_view()),  # as_view() 方法动态地将函数转换成方法
    # 详细视图的路由
    # url(r'^books/(?P<pk>\d+)/$', views.BookDetailView.as_view()),
]

router = DefaultRouter()  # 创建路由器
router.register(r'books', views.BookInfoViewSet)  # 注册路由
urlpatterns += router.urls  # 把生成好的路由拼接到urlpatterns中
