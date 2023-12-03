from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Cars(models.Model):
    id = models.AutoField(primary_key=True)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rented = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.brand} {self.model}"


class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    first = models.CharField(max_length=100)
    last = models.CharField(max_length=100)
    phone = PhoneNumberField()
    def __str__(self):
        return f"{self.last} {self.first}"
    

class Rent(models.Model):
    id_rent=models.AutoField(primary_key=True)
    id_car=models.ForeignKey(Cars, on_delete=models.CASCADE)
    id_cos=models.ForeignKey(Customer, on_delete=models.CASCADE)
    startDate = models.DateField()
    endDate= models.DateField()
    
