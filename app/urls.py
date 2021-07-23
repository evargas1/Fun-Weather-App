from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.SearchResultsView, name='search'),
    path('prac/', views.prac, name='prac'),
    url(r'^delete/(?P<pk>[0-9]+)/$', views.city_delete, name='city_delete'),
]