from django.db import models


class Streets(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)

    class Meta:
        db_table = 'streets'


class Houses(models.Model):
    id = models.IntegerField(primary_key=True)
    number = models.IntegerField()
    floor = models.IntegerField()
    street_id = models.ForeignKey(Streets, on_delete=models.PROTECT)

    class Meta:
        db_table = 'houses'
