from django.db import models
from datetime import datetime
from decimal import Decimal

# Create your models here.


class Customer(models.Model):
	# customer_id=models.AutoField()
	first_name=models.CharField(max_length=25)
	last_name=models.CharField(max_length=25)
	contact_no=models.IntegerField()
	pincode=models.IntegerField()
	
class Product(models.Model):
	# product_id=models.AutoField()
	name=models.CharField(max_length=50)
	# unit_price=models.DecimalField(max_digits=6,decimal_places=2)

	

class Order(models.Model):
	customer_id=models.ForeignKey(Customer,on_delete=models.CASCADE)
	product_id=models.ForeignKey(Product,on_delete=models.CASCADE)
	# unit_price=DecimalField(max_digits=6,decimal_places=2)
	qnt=models.IntegerField()
	# # total_price=DecimalField(max_digits=10,decimal_places=2)
	# created_date=DateTimeField(default=datetime.now, blank=True)



