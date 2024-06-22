from django.http import HttpResponse
from django.shortcuts import render
from django.http import Http404
from django.core.serializers import serialize
from .models import Slope
from django.template import loader

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. It works!")

def slopes(request):
    slopes_data = Slope.objects.all()
    serializer = serialize('geojson', slopes_data, geometry_field='geom', fields=('name', 'geom'))
    context = {'slopes_data': serializer}
    return render(request, 'slopes.html', context)