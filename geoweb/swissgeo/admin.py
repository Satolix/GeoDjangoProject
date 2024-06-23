from django.contrib.gis import admin
from .models import *

admin.site.register(Slope, admin.OSMGeoAdmin)
admin.site.register(Lift, admin.OSMGeoAdmin)
#admin.site.register(Building, admin.OSMGeoAdmin)

