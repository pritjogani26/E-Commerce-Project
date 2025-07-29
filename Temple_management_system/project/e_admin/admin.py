from django.contrib import admin
from e_admin.models import Product,feedback,donation,room_booking,rooms, Order
# Register your models here.

class Product_table(admin.ModelAdmin):
    list_display = ('title','price','name','category','description','img_source','stock')

admin.site.register(Product,Product_table)

class Feedback_table(admin.ModelAdmin):
    list_display = ('username','date','state','feedback')

admin.site.register(feedback,Feedback_table)

class Donation_table(admin.ModelAdmin):
    list_display = ('username','date','amountc','reason')

admin.site.register(donation,Donation_table)

class Room_Booking(admin.ModelAdmin):
    list_display = ('username','place','purpose','booking_date','check_in_time','check_out_time','male','female','children','total_guests','total_rooms','total_amount')
admin.site.register(room_booking,Room_Booking)

class Room(admin.ModelAdmin):
    list_display = ('total_rooms','available_rooms')
    
admin.site.register(rooms,Room)

class Order_table(admin.ModelAdmin):
    list_display = ('username','date','items','price','quantity','total_amount','address','state','pincode')
    
admin.site.register(Order,Order_table)
