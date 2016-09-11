from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.hello, name='hello'),
    url(r'^check$', views.check_children_status, name='check')
]