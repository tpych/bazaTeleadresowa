from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    BirthDate = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name + ' ' + self.surname 
    
    def __eq__(self, other):
        return self.phone == other.phone or self.email == other.email