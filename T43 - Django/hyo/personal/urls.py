from django.urls import path, include
from . import views

urlpatterns = [
    path('online_shopping/', views.online_shop),
    path('index/', views.index),
    path('about me/', views.about_me)
]