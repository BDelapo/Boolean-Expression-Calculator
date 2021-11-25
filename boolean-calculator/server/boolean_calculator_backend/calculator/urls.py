from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('set-session/', views.Session_Auth.as_view() ),
    path('set-session/calculate/', views.Row_Obtainer.as_view() ),
    # path('calculate-terms/', views.getRows )

]