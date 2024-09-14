from django.db import models

# Create your models here.


class Tour(models.Model):
    country_origin = models.CharField(max_length=64)
    destination_country = models.CharField(max_length=64)
    number_of_nights = models.IntegerField()
    price = models.IntegerField()

    # This is a string representation of the tours 
    def __str__(self):
        return (f'ID: {self.id}, From: {self.country_origin} to {self.destination_country}, {self.number_of_nights} nights for ${self.price}')