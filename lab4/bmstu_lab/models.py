from django.db import models


class Car(models.Model):
    name = models.CharField(max_length=30)
    speed = models.IntegerField()
    cost = models.FloatField()
