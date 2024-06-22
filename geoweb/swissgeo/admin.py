from django.contrib.gis import admin
from .models import Slope

admin.site.register(Slope, admin.OSMGeoAdmin)

