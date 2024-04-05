
from django.contrib import admin
from .models import FuelTypeModel,CarModel
# Register your models here.

# admin.site.register(FuelTypeModel)
# admin.site.register(CarModel)

class Fuel(admin.ModelAdmin):
    list_display = ('id', 'fuel_name')
admin.site.register(FuelTypeModel,Fuel)

class Car(admin.ModelAdmin):
    list_display = ('id','car_name')
admin.site.register(CarModel,Car)