from django.contrib.gis import admin
from .models import City, Slope

admin.site.register(City)
admin.site.register(Slope, admin.OSMGeoAdmin)

