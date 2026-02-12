from django.db import models
from django.utils import timezone

# Create your models here.

class Supplier(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=timezone.now)

    def getName(self):
        return self.name
    
    def __str__(self):
        return "{} - {}, {} created at: {}".format(self.name, self.city, self.country, self.created_at)