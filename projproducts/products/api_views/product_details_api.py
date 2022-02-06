from django.http import HttpResponse
from products.models.product_details import ProductDetails
from products.serializers.product_details_serializer import ProductDetailsSerializer
from rest_framework import routers, serializers, viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.views import APIView
import abc


# -> ViewSets define the view behavior.
class ProductDetailsApiViewSet(viewsets.ModelViewSet):
    queryset = ProductDetails.objects.all()
    serializer_class = ProductDetailsSerializer
