from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core.serializers import serialize
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.views.decorators.http import require_POST

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


@csrf_protect
@require_POST
def update_status(request):
    name = request.POST.get('name')
    status = request.POST.get('status')
    type = request.POST.get('type')

    if status not in ['open', 'closed']:
        return JsonResponse({'error': 'Invalid status'}, status=400)

    try:
        if type == 'lift':
            lift = Lift.objects.get(name=name)
            lift.status = status
            lift.save()
            return JsonResponse({'success': True})
        elif type == 'slope':
            slope = Slope.objects.get(name=name)
            slope.status = status
            slope.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'error': 'Invalid type'}, status=400)
    except (Lift.DoesNotExist, Slope.DoesNotExist):
        return JsonResponse({'error': 'Invalid name'}, status=400)

