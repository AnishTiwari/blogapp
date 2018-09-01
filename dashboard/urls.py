from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'logout/$',views.logout_user,name="logout"),
    url(r'dashboard/$',views.dashboard,name="dashboard"),
    url(r'$',views.index,name="indexlogin"),
]
