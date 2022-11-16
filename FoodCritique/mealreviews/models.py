from django.db import models

# Create your models here.
class Restaurant(models.Model) :
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    score = models.DecimalField(max_digits=1, decimal_places=1)
    cuisineType = models.CharField(max_length=30)

    def __str__(self) :
        return (self.name)

    class Meta :
        db_table = 'Restaurants'

class Dish(models.Model) :
    restuarant = models.ForeignKey(Restaurant, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=30)
    score =  models.DecimalField(max_digits=1, decimal_places=1)
    description = models.CharField(max_length=100)
    
    def __str__(self) :
        return (self.name)
    class Meta :
        db_table = 'Dish'