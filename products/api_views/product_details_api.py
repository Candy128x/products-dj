from django.conf import settings
from django.http import HttpResponse
from products.models.product_detail import ProductDetail
from products.serializers.product_details_serializer import ProductDetailsSerializer
from rest_framework import routers, serializers, viewsets, status
from rest_framework.decorators import api_view
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.views import APIView
import json, logging

logger = logging.getLogger(__name__)


# -> ViewSets define the view behavior.
class ProductDetailsApiViewSet(viewsets.ModelViewSet):
    queryset = ProductDetail.objects.all()
    serializer_class = ProductDetailsSerializer

