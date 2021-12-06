from django.db import models


class Customer(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)

    class Meta:
        db_table = 'customer'


class Cars(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    speed = models.IntegerField()
    colour = models.CharField(max_length=10)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)

    class Meta:
        db_table = 'cars'
