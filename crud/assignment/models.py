from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    amount = models.PositiveIntegerField()
    productDetails = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name