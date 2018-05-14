from django.db import models
from uuid import uuid4


class Car(models.Model):
    uuid = models.UUIDField(default=uuid4)
    manufacturer = models.CharField(max_length=150)
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=15, decimal_places=3)

    class Meta:
        default_related_name = 'cars_car'

    def __str__(self):
        return '{} {} {}'.format(self.manufacturer, self.make, self.model)


class Owner(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    identification = models.CharField(max_length=100)
    regno = models.CharField(unique=True, max_length=30)
    car = models.ForeignKey('Car', null=True)

    def __str__(self):
        return '{} {} - {}'.format(self.first_name, self.last_name, self.regno)
