from django.db import models

# Create your models here.

class Restaurant(models.Model):
    restaurant_id = models.IntegerField()
    restaurant_name = models.CharField(max_length=255)
    country_code = models.IntegerField()
    address = models.CharField(max_length=255)
    cuisines = models.CharField(max_length=255)
    has_table_booking = models.BooleanField(default=False)
    has_online_delivery = models.BooleanField(default=False)
    aggregate_rating = models.FloatField()

def __str__(self):
    return self.name

