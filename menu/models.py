from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    
class Meal(models.Model):
    name = models.CharField(max_length=100)
    #image = models.ImageField(upload_to='uploads/meals/')
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    






