from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

from . import views as accounts_views
from boards import views

urlpatterns=[
    path('signup/',accounts_views.signup, name='signup'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),


]