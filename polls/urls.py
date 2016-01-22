from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^vote/$', views.voting, name='vote'),
    url(r'^authen/$', views.authen_token, name='authen-token'),
    url(r'^authen/inspect$', views.authen_inspect, name='authen-inspect'),
    url(r'^authen/logout$', views.authen_logout, name='authen-logout'),
]
