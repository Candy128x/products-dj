from products.models.product_detail import ProductDetail
from rest_framework import serializers


# # -> Serializers define the API representation.
# class ProductDetailsSerializer(serializers.HyperlinkedModelSerializer):
class ProductDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductDetail
        fields = ['id', 'name', 'description', 'price', 'category', 'available_quantity']
