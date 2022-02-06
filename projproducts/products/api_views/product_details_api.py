from django.http import HttpResponse
from products.models.product_details import ProductDetails
from products.serializers.product_details_serializer import ProductDetailsSerializer
from rest_framework import routers, serializers, viewsets, status
from rest_framework.decorators import api_view
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from utils.services.email_service import EmailService
import json, logging

logger = logging.getLogger(__name__)


# -> ViewSets define the view behavior.
class ProductDetailsApiViewSet(viewsets.ModelViewSet):
    queryset = ProductDetails.objects.all()
    serializer_class = ProductDetailsSerializer


def send_ex_msg(subject, ex_msg, ex_msg_details):
    email_service_obj = EmailService()
    email_service_obj.send_email_v2(email_subject, email_body, to_email)
    return 1


@api_view(['POST'])
def send_ex_email(request):
    api_response = {'status_code': status.HTTP_500_INTERNAL_SERVER_ERROR, 'status': 'failed', 'messages': [], 'data': []}
    try:
        logger.info(f'---START---')
        logger.debug(f'---request.data: {request.data}')
        if 1:
            email_subject = request.data.get('email', {}).get('subject', '')
            email_body = request.data.get('email', {}).get('body', '')
            to_email = request.data.get('email', {}).get('to_email', [])
            email_service_obj = EmailService()
            # email_service_obj.send_email()
            email_service_obj.send_email_v2(email_subject, email_body, to_email)
            api_response['status_code'] = status.HTTP_200_OK
            api_response['status'] = 'success'
            api_response['messages'].append('email send successfully.')
            api_response['data'].append(request.data)
    except Exception as ex:
        logger.critical('---send_ex_email---funn---EXCEPTION---', exc_info=True)
        logger.critical(f'---send_ex_email---funn---EXCEPTION--msg: {ex}')
        api_response.update({'exception_message': [str(ex)]})
    finally:
        logger.info(f'---api_response: {api_response}')
        return Response(api_response)