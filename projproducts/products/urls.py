from django.urls import path, include
from products.api_views.product_details_api import ProductDetailsApiViewSet
from products.api_views.product_details_api import send_ex_email, send_form_email
from rest_framework import routers


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'api', ProductDetailsApiViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-send-ex-email/', send_ex_email, name='products-send-ex-email'),
    path('api-send-form-email/', send_form_email, name='products-send-form-email'),
]
