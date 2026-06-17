from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("mood/", views.mood, name="mood"),
    path("time/", views.time, name="time"),
    path("budget/", views.budget, name="budget"),
    path("result/", views.result, name="result"),
]
