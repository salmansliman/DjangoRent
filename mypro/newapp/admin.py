from django.contrib import admin
from .models import Cars,Customer,Rent
# Register your models here.
class CarAdmin(admin.ModelAdmin):
    list_display="id","brand","model","price","rented"
admin.site.register(Cars,CarAdmin)
class CustomerAdmin(admin.ModelAdmin):
    list_display="id","first","last","phone"
admin.site.register(Customer,CustomerAdmin)
class RentAdmin(admin.ModelAdmin):
    list_display="id_car","id_cos","startDate","endDate"
admin.site.register(Rent,RentAdmin)
