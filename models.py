from django.db import models


# Create your models here.
# Puneet 

class Product(models.Model):
    fields_name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    added_on_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fields_name


class Product_Purchase(models.Model):
    product = models.ForeignKey(Product, null=False, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(null=False)
    price = models.PositiveIntegerField(null=False)
    purchase_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.PositiveIntegerField(null=False)


class Vendor(models.Model):
    vendor_name = models.CharField(max_length=100)
    vendor_description = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.vendor_name


class Vendor_Sale(models.Model):
    vendor = models.ForeignKey(Vendor, null=False, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, null=False, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(null=False)
    price = models.PositiveIntegerField(null=False)
    total_amount = models.PositiveIntegerField(null=False)
    purchase_date = models.DateTimeField(auto_now_add=True)
