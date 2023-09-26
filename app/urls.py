from django.contrib import admin
from django.urls import path

from . import views


urlpatterns = [
    path('', views.home),
    path('s/', views.s),
    path('st/', views.stu),
]
