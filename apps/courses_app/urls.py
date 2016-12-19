from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^courses$', views.courses, name='courses'),
    url(r'^course/(?P<id>\d+)/delete$', views.delete, name='delete'),
    url(r'^course/(?P<id>\d+)/final_delete$', views.final_delete, name='final_delete'),
    url(r'^cancel$', views.cancel, name='cancel'),
]