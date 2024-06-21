from django.contrib import admin

from .models import (
    Customer,
    Cart,
    OrderPlaced,
    Product
)

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','name','locality','city','zipcode','state']

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','selling_price','discounted_price','description','brand','category','product_image']   


@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','Product','quantity']

@admin.register(OrderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','Customer','Product','quantity','ordered_date','status']
