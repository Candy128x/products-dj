from django.urls import path, include
from home.api_views.send_email_api import send_test_email, send_form_email, send_ex_email


urlpatterns = [
    path('send-test-email/', send_test_email, name='home-send-test-email'),
    path('api-send-form-email/', send_form_email, name='home-send-form-email'),
    path('api-send-ex-email/', send_ex_email, name='home-send-ex-email'),
]
