from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('nearest-park/', views.nearest_park, name='nearest_park'),
    path('weather/', views.weather, name='weather'), 
]