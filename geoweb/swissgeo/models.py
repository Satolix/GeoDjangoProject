from django.db import models
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
    @property
    def length(self):
        return self.geom.length

class Lift(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()
    geom = models.LineStringField()

    class Meta:
        db_table = 'lifts'
        verbose_name_plural = "lifts"

    def __str__(self):
        return self.name