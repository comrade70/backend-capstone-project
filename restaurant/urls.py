#define url routes for index()
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index')
]