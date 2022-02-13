from django.conf import settings
from django.http import HttpResponse
from django.template.loader import render_to_string
from home.cron_jobs.send_email_cron_job import send_email
from rest_framework import routers, serializers, viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from utils.helper.datetime_util import DateTimeUtil
from utils.services.email_service import EmailService
import json, logging

logger = logging.getLogger(__name__)


@api_view(['GET'])
def send_test_email(request):
    api_response = {'status_code': status.HTTP_500_INTERNAL_SERVER_ERROR, 'status': 'failed', 'messages': [], 'data': []}
    try:
        logger.info(f'---START---')
        res1 = send_email()
        if res1:
            api_response['status_code'] = status.HTTP_200_OK
            api_response['status'] = 'success'
            api_response['messages'].append('email send successfully.')
            api_response['data'].append(res1)

    except Exception as ex:
        logger.critical('---send_test_email---funn---EXCEPTION---', exc_info=True)
        logger.critical(f'---send_test_email---funn---EXCEPTION--msg: {ex}')
        api_response.update({'exception_message': [str(ex)]})
    finally:
        logger.info(f'---api_response: {api_response}')
        return Response(api_response)


@api_view(['POST'])
def send_form_email(request):
    api_response = {'status_code': status.HTTP_500_INTERNAL_SERVER_ERROR, 'status': 'failed', 'messages': [], 'data': []}
    try:
        logger.info(f'---START---')
        logger.debug(f'---request.data: {request.data}')
        # logger.debug(f'---request.header: {request.headers}')
        api_salt_key_is_valid = request.headers.get('Api-Salt-Key') in settings.SEND_EMAIL_API_SALT_KEY
        if api_salt_key_is_valid:
            email_subject = request.data['email']['subject']
            email_body = request.data['email']['body']
            to_email = request.data['email']['to_email']

            datetime_util_obj = DateTimeUtil()
            email_subject = f'{email_subject} - {datetime_util_obj.get_current_datetime()}'
            email_body = render_to_string('send_emails/contact_us_email.html', email_body)

            email_service_obj = EmailService()
            # email_service_obj.send_email()
            email_service_obj.send_email_v2(email_subject, email_body, to_email)
            api_response['status_code'] = status.HTTP_200_OK
            api_response['status'] = 'success'
            api_response['messages'].append('email send successfully.')
            api_response['data'].append(request.data)
        else:
            api_response['messages'].append('missing/invalid Api-Salt-Key!')

    except Exception as ex:
        logger.critical('---send_form_email---funn---EXCEPTION---', exc_info=True)
        logger.critical(f'---send_form_email---funn---EXCEPTION--msg: {ex}')
        api_response.update({'exception_message': [str(ex)]})
    finally:
        logger.info(f'---api_response: {api_response}')
        return Response(api_response)


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

            datetime_util_obj = DateTimeUtil()
            email_subject = f'{email_subject} - {datetime_util_obj.get_current_datetime()}'
            # email_body = render_to_string('send_emails/ex_email.html', email_body)
            email_body = render_to_string('send_emails/ex_detail_email.html', email_body)

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