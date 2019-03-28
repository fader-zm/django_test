from django.conf.urls import url

from . import views
urlpatterns = [
    url(r'^books/$', views.BookListView.as_view()),  # as_view() 方法动态地将函数转换成方法
    # 详细视图的路由
    url(r'^books/(?P<pk>\d+)/$', views.BookDetailView.as_view()),
    
]