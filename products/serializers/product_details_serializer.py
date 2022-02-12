from products.models.product_details import ProductDetails
from rest_framework import serializers


# # -> Serializers define the API representation.
# class ProductDetailsSerializer(serializers.HyperlinkedModelSerializer):
class ProductDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductDetails
        fields = ['id', 'name', 'price', 'quantity']
