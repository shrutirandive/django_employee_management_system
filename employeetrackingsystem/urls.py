from django.contrib import admin
from django.urls import path

from .views.register import Register
from .views.login import Login, logout
from .views.details import showg, showm
from .views.navbar import navbar
from .views.main import main

urlpatterns = [
    path('',main, name='main'),
    path('register', Register.as_view(), name='register'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout, name='logout'),
    path('showg', showg, name='showg'),
    path('showm', showm, name='showm'),
    path('navbar', navbar, name='navbar'),


]
