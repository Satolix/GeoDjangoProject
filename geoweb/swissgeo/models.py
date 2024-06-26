
from django.contrib.gis.db import models


# Create your models here.
class Slope(models.Model):
    name = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=100, choices=[('green', 'green'), ('blue', 'blue'), ('red', 'red'), ('black', 'black')], default='green')
    status = models.CharField(max_length=100, choices=[('open', 'open'), ('closed', 'closed')], default='closed')
    geom = models.LineStringField()

    class Meta:
        db_table = 'slopes'
        verbose_name_plural = "slopes"

    def __str__(self):
        return self.name

class Lift(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.IntegerField(default=2)
    geom = models.LineStringField()
    type = models.CharField(max_length=100, choices=[('chairlift', 'chairlift'), ('gondola', 'gondola'), ('teleski', 'teleski')], default='chairlift')
    status = models.CharField(max_length=100, choices=[('open', 'open'), ('closed', 'closed')], default='closed')

    class Meta:
        db_table = 'lifts'
        verbose_name_plural = "lifts"

    def __str__(self):
        return self.name


class Building(models.Model):
    name = models.CharField(max_length=100)
    geom = models.PolygonField()
    type = models.CharField(max_length=100, choices=[('restaurant', 'restaurant'), ('hotel', 'hotel'), ('liftstation', 'liftstation')], default='restaurant')

    class Meta:
        db_table = 'buildings'
        verbose_name_plural = "buildings"

    def __str__(self):
        return self.name
