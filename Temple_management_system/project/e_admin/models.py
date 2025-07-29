from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=50,default=0)
    price = models.CharField(max_length=50,default=0)
    name = models.CharField(max_length=50,default=0)
    category = models.CharField(max_length=50,default=0)
    description = models.CharField(max_length=200,default=0)
    img_source = models.CharField(max_length=50,default=0)
    stock = models.IntegerField(default=0)
   

   
# # Payment-Table     
# class Payment(models.Model):
#     Transaction_id = models.AutoField(primary_key=True)
#     user_id = models.ForeignKey(User,on_delete=models.CASCADE)
#     Date = models.DateField()
#     amount = models.DecimalField(max_digits=6,decimal_places=2)
#     payment_method = models.CharField(max_length=20)
#     status = models.CharField(max_length=15)

        

class room_booking(models.Model):
    username= models.CharField(max_length=50,default=0)
    place = models.CharField(max_length=50,default=0)
    purpose = models.CharField(max_length=100,default=0)
    booking_date = models.DateField()
    check_in_time = models.DateTimeField()
    check_out_time = models.DateTimeField()
    male = models.IntegerField(default=0)
    female = models.IntegerField(default=0)
    children = models.IntegerField(default=0)
    total_guests = models.IntegerField(default=0)
    total_rooms = models.IntegerField(default=0)
    total_amount = models.IntegerField(default=0)
    
    
class rooms(models.Model):
    total_rooms = models.IntegerField(default=0)
    available_rooms = models.IntegerField(default=0)    


# Order Table
class Order(models.Model):
    username = models.CharField(max_length=30)
    date = models.DateTimeField()
    items = models.TextField(default=0)
    price = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    total_amount = models.DecimalField(max_digits=8,decimal_places=2)
    address = models.TextField(default=0)
    state = models.CharField(max_length=50,default=0)
    pincode = models.IntegerField(default=0)
    



# Donation Table
class donation(models.Model):
    username = models.TextField()
    date = models.DateTimeField()
    amountc = models.IntegerField(default=0)
    reason = models.CharField(max_length=100)

# #Cart Table
# class Cart(models.Model):
#     cart_id = models.AutoField(primary_key=True)
#     product_id = models.ForeignKey(Product,on_delete=models.CASCADE)
#     total_amount = models.DecimalField(max_digits=6,decimal_places=2)
    

# Feedback Table
class feedback(models.Model):
    username = models.TextField(primary_key=True)
    date = models.DateField()
    state =models.CharField(max_length=100,default=0)
    feedback = models.CharField(max_length=100)