from django.conf.urls import url

from fb import views

urlpatterns = [
    #url(r'', views.home, name='home'),
    #url(r'^detail/$', views.detail, name='detail'),
    url(r'^login/$', views.login, name='login'),

  
]