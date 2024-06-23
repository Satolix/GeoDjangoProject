# views.py
from django.http import HttpResponse
from django.shortcuts import render
from django.core.serializers import serialize
from .models import  Lift, Slope

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. It works!")

def map(request):
    return render(request, 'map.html')

def slopesjson(request):
    slopes_data = Slope.objects.all()
    serializer = serialize('geojson', slopes_data, geometry_field='geom')
    return HttpResponse(serializer, content_type='application/json')

def liftsjson(request):
    lifts_data = Lift.objects.all()
    serializer = serialize('geojson', lifts_data, geometry_field='geom', fields=('name', 'capacity'))
    return HttpResponse(serializer, content_type='application/json')
'''
def buildingsjson(request):
    buildings_data = Building.objects.all()
    serializer = serialize('geojson', buildings_data, geometry_field='geom', fields=('name', 'type'))
    return HttpResponse(serializer, content_type='application/json')

def loadSlopes():
    '''
