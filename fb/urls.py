from django.conf.urls import url

from fb import views

urlpatterns = [
    #url(r'', views.home, name='home'),
    url(r'^about/$', views.about, name='about'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.login, name='login'),
    url(r'^sucess/$', views.sucess, name='sucess'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^profile/$', views.user_profile, name='user_profile'),
    #url(r'^loggedin/$', views.loggedin, name='loggedin'),


  
]