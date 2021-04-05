from django.db import models

# Create your models here.

class Name(models.Model):
    FirstName = models.CharField(max_length = 64)
    LastName = models.CharField(max_length = 64)
    class Meta:
        verbose_name_plural = "Name"

class EmpID(models.Model):
    EmployeeID =models.IntegerField()
    
    class Meta:
        verbose_name_plural = "EmployeeID"

class Contact(models.Model):
    PhoneNo = models.IntegerField()

    class Meta:
        verbose_name_plural = "PhoneNo"

   

class Address(models.Model):
    Line1 = models.CharField(max_length = 64)
    Line2 = models.CharField(max_length = 64)
    Street = models.CharField(max_length = 64)
    City = models.CharField(max_length = 64)
    State = models.CharField(max_length = 64)
    Country = models.CharField(max_length = 64)

    class Meta:
        verbose_name_plural = "Address"
