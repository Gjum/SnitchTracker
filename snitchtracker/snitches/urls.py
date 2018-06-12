from django.conf.urls import url
from django.urls import path
from . import views

app_name='snitches'

urlpatterns = [
    #/$
    url(r'^profile', views.update_profile),
    path(r'groups', views.handle_group),
    path(r'groups/<str:name>', views.handle_group),
    url(r'^logout', views.logout_view),
    path(r'api/webhook/<str:key>', views.webhook),
    url(r'^', views.Home),
]