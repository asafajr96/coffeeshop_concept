from django.db import models


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to="products", blank=True, null=True)
    stock = models.IntegerField()
    def __str__(self):
        return self.product_name

