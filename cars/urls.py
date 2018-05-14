from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^owners/add/$', views.OwnersView().as_view()),
    url(r'^owners/list/$', views.OwnersView().as_view()),
    url(r'^add/$', views.CarsView().as_view()),
    url(r'^list/$', views.CarsView().as_view()),
    url(r'^get/(?P<uuid>[0-9A-Za-z\-]+)/$', views.CarsView().as_view()),
]