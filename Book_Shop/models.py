from django.db import models


class book(models.Model):
    name = models.CharField(max_length=200)
    Author = models.CharField(null= True, blank=True, max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.name

