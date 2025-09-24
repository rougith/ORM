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
