from django.urls import path, include
from home.api_views.send_email_api import send_ex_email, send_form_email


urlpatterns = [
    path('api-send-ex-email/', send_ex_email, name='home-send-ex-email'),
    path('api-send-form-email/', send_form_email, name='home-send-form-email'),
]
