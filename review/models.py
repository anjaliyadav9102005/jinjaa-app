from django.db import models

# Create your models here.
class Review(models.Model):
    ProductName = models.CharField(max_length=100)
    ProductImage = models.ImageField(upload_to='products/' , blank=True)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.ProductName
