from django.contrib import admin
from .models import Customer,Order,OrderItem,Products,ShippingAddress
# Register your models here.
admin.site.register(Customer)
admin.site.register(Products)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)