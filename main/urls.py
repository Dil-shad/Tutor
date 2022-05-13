from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [


    path('', Home, name='Home_page'),
    path('signup', signup, name='signup'),
    path('login', login, name='login'),
    path('dash', dash, name='dash'),
    path('profile', profile, name='profile'),
    path('about', about, name='about'),
    path('logout', logout, name='logout'),
    path('edit/<int:pk>', edit, name='edit'),
    path('delete/<int:pk>', delete, name='delete')


]
