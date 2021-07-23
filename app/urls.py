from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.SearchResultsView, name='search'),
    path('prac/', views.prac, name='prac'),
    path(r'^delete/(?P<id>\d+)/$', views.city_delete, name='city_delete'),
]