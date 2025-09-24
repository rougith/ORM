# Ex02 Django ORM Web Application
# Date:24/09/25
# AIM
To develop a Django application to store and retrieve data from a bank loan database using Object Relational Mapping(ORM).

# ENTITY RELATIONSHIP DIAGRAM
## DESIGN STEPS
## STEP 1:
Clone the problem from GitHub

## STEP 2:
Create a new app in Django project

## STEP 3:
Enter the code for admin.py and models.py

## STEP 4:
Execute Django admin and create details for 10 books

# PROGRAM

'''
admin.py
from django.contrib import admin
from .models import Loan

# Customize how Loan model appears in Admin
class LoanAdmin(admin.ModelAdmin):
    list_display = ('customer_id', 'name', 'amount', 'interest_rate', 'duration')
    search_fields = ('name', 'customer_id')
    list_filter = ('interest_rate', 'duration')
    ordering = ('customer_id',)

# Register the model with custom admin options
admin.site.register(Loan, LoanAdmin)
models.py


from django.db import models

class Loan(models.Model):
    customer_id = models.AutoField(primary_key=True)   
    name = models.CharField(max_length=100)  
    age  = models.IntegerField()     
    amount = models.DecimalField(max_digits=10, decimal_places=2)  
    interest_rate = models.FloatField()               
    duration = models.IntegerField()                  
    address = models.TextField()
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    income = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return f"{self.name} - {self.amount}"


'''


# OUTPUT

![alt text](<Screenshot 2025-09-24 200133.png>)



# RESULT
Thus the program for creating a database using ORM hass been executed successfully
