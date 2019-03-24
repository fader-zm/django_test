from django.conf.urls import url
from . import views

urlpatterns = {
    url(r'^users/index/$', views.index),
    url(r'^say/$', views.say),
    url(r'^sayhello/$', views.say_hello),
    
}
