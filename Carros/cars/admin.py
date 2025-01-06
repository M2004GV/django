from django.contrib import admin
from .models import Car
from .models import Brand

class BrandAdmin(admin.ModelAdmin):
    list_display = ('id','name',)
    search_fields = ('name',)

class CarAdmin(admin.ModelAdmin):
    list_display = ('model','brand', 'factory_year', 'model_year', 'value', 'photo')
    search_fields = ('model','brand__name')

    
admin.site.register(Brand, BrandAdmin)
admin.site.register(Car, CarAdmin)