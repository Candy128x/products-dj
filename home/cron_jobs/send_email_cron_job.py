from django.conf import settings
from django.template.loader import render_to_string
from utils.helper.datetime_util import DateTimeUtil
from utils.services.email_service import EmailService
import json, logging

logger = logging.getLogger(__name__)


def send_email():
    try:
        logger.info(f'---START---')
        # logger.debug(f'---request.header: {request.headers}')
        datetime_util_obj = DateTimeUtil()
        email_subject = f'Daily eMail from products-dj - {datetime_util_obj.get_current_datetime()}'
        email_body = {
            "subject": "Daily Test eMail from products-dj",
            "form_data": [
                {"field": "Quote", "value": "Simple Living High Thinking :], Will give you Success in Life <3"}
            ]
        }
        to_email = settings.EMAIL_BCC

        datetime_util_obj = DateTimeUtil()
        email_subject = f'{email_subject} - {datetime_util_obj.get_current_datetime()}'
        email_body = render_to_string('send_emails/contact_us_email.html', email_body)

        email_service_obj = EmailService()
        email_service_obj.send_email_v2(email_subject, email_body, to_email)

    except Exception as ex:
        logger.critical('---send_form_email---funn---EXCEPTION---', exc_info=True)
        logger.critical(f'---send_form_email---funn---EXCEPTION--msg: {ex}')

    finally:
        return 1


if __name__ == '__main__':
    send_email()
