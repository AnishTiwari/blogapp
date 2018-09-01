from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.add, name="add"),
    url(r'^blogged/$', views.blogged, name="blogged"),
    url(r'^viewblog/$', views.viewblog, name="viewblog"),

]