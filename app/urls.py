from django.contrib import admin
from django.urls import path, include
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.SearchResultsView, name='search'),
    path('prac/', views.prac, name='prac'),
    path('<int:id>/delete/', views.city_delete, name='city_delete'),
]