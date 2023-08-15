from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('topstories/', views.results, name='topstories'),
    path('popular/', views.results, name='popular'),
    path('feed/', views.results, name='feed'),
]
