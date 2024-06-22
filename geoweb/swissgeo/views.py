# views.py
from django.http import HttpResponse
from django.shortcuts import render
from django.core.serializers import serialize
from .models import Slope

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. It works!")

def slopes(request):
    return render(request, 'slopes.html')

def slopesjson(request):
    slopes_data = Slope.objects.all()
    serializer = serialize('geojson', slopes_data, geometry_field='geom', fields=('name', 'difficulty'))
    return HttpResponse(serializer, content_type='application/json')
