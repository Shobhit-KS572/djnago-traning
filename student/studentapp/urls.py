from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('display', views.displaydata, name='displaydata'),
    path('registration', views.registration, name='registration'),
    path('homepage', views.homepage, name='homepage'),
    path('teacher', views.teacher, name='teacher')
]
