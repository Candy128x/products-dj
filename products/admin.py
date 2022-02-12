from django.contrib import admin
from products.models.product_details import ProductDetails


# Register your models here.
class ProductDetailsAdmin(admin.ModelAdmin):
    pass


admin.site.register(ProductDetails, ProductDetailsAdmin)