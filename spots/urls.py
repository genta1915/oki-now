from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("time/", views.time, name="time"),
    path("result/", views.result, name="result"),
]
