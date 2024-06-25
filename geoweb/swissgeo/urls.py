from django.urls import path
from . import views
from .views import update_status

urlpatterns = [
    path('', views.index, name='index'),
    path('map/', views.map, name='map'),
    path('weather/', views.weather, name='weather'),
    path('manage/', views.manage, name='manage'),
    path('slopes.json', views.slopesjson, name='slopesjson'),
    path('lifts.json', views.liftsjson, name='liftsjson'),
    path('buildings.json', views.buildingsjson, name='buildingsjson'),
    path('update_status/', update_status, name='update_status'),
]
