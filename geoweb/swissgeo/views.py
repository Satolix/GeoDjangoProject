from django.shortcuts import render
from django.http import HttpResponse
from django.core.serializers import serialize
from .models import Lift, Slope, Building

def index(request):
    return render(request, 'index.html')

def map(request):
    return render(request, 'map.html')

def weather(request):
    return render(request, 'weather.html')

def manage(request):
    return render(request, 'manage.html')

def slopesjson(request):
    slopes_data = Slope.objects.all()
    serializer = serialize('geojson', slopes_data, geometry_field='geom')
    return HttpResponse(serializer, content_type='application/json')

def liftsjson(request):
    lifts_data = Lift.objects.all()
    serializer = serialize('geojson', lifts_data, geometry_field='geom', fields=('name', 'capacity', 'type', 'status'))
    return HttpResponse(serializer, content_type='application/json')

def buildingsjson(request):
    buildings_data = Building.objects.all()
    serializer = serialize('geojson', buildings_data, geometry_field='geom', fields=('name', 'type', 'status'))
    return HttpResponse(serializer, content_type='application/json')
