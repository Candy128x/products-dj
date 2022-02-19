from django.conf import settings
from django.template.loader import render_to_string
from utils.helper.datetime_util import DateTimeUtil
from utils.services.email_service import EmailService
import json, logging

logger = logging.getLogger(__name__)


def send_email():
    try:
        datetime_util_obj = DateTimeUtil()
        _current_dt = datetime_util_obj.get_current_datetime()
        print(f'---START---current_dt: {_current_dt}')
        # logger.debug(f'---request.header: {request.headers}')
        email_subject = f'Daily eMail from products-dj - {datetime_util_obj.get_current_datetime()}'
        email_body = {
            "subject": "Daily Test eMail from products-dj",
            "form_data": [
                {"field": "Quote", "value": "Simple Living High Thinking :], Will give you Success in Life <3"}
            ]
        }
        to_email = settings.EMAIL_BCC

        email_subject = f'{email_subject} - {_current_dt}'
        email_body = render_to_string('send_emails/contact_us_email.html', email_body)

        email_service_obj = EmailService()
        email_service_obj.send_email_v2(email_subject, email_body, to_email)

    except Exception as ex:
        print('---send_form_email---funn---EXCEPTION---', exc_info=True)
        print(f'---send_form_email---funn---EXCEPTION--msg: {ex}')

    finally:
        return 1


if __name__ == '__main__':
    send_email()
