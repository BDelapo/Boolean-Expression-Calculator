from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('set-session/', views.post_session ),
    path('set-session/calculate/post', views.post ),
    path('set-session/calculate/get', views.get ),
]