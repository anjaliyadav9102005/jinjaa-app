from django.db import models

# Create your models here.
class Payment(models.Model):
    Name = models.CharField(max_length=100)
    ProductName = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10 , decimal_places=2)

    def __str__(self):
        return self.Name