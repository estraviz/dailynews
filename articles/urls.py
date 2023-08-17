from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('topstories/', views.results, name='topstories'),
    path('popular/', views.results, name='popular'),
    path('feed/', views.results, name='feed'),
]
