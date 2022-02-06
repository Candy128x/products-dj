from django.conf import settings
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import email, smtplib, ssl, logging
import threading
from threading import Thread
from django.core.mail import EmailMessage

logger = logging.getLogger(__name__)


class EmailThread(threading.Thread):
    def __init__(self, subject, html_content, recipient_list):
        self.subject = subject
        self.recipient_list = recipient_list
        self.html_content = html_content
        threading.Thread.__init__(self)

    def run (self):
        EMAIL_HOST_USER = settings.EMAIL_HOST_USER
        msg = EmailMessage(self.subject, self.html_content, EMAIL_HOST_USER, self.recipient_list, settings.EMAIL_BCC)
        msg.content_subtype = "html"
        msg.send()


class EmailService:

    def send_email(self):
        try:
            logger.info(f'---START---')
            subject = "Test eMail from products-dj"
            body = "This is an email with attachment sent from Python"
            sender_email = settings.EMAIL_HOST_USER
            receiver_email = ",".join(settings.EMAIL_BCC)
            password = settings.EMAIL_HOST_PASSWORD

            # -> Create a multipart message and set headers
            message = MIMEMultipart()
            message["From"] = sender_email
            message["To"] = receiver_email
            message["Subject"] = subject
            message["Bcc"] = receiver_email  # Recommended for mass emails

            # -> Add body to email
            message.attach(MIMEText(body, "plain"))

            # filename = "document.pdf"  # In same directory as script
            #
            # # -> Open PDF file in binary mode
            # with open(filename, "rb") as attachment:
            #     # Add file as application/octet-stream
            #     # Email client can usually download this automatically as attachment
            #     part = MIMEBase("application", "octet-stream")
            #     part.set_payload(attachment.read())
            #
            # # -> Encode file in ASCII characters to send by email
            # encoders.encode_base64(part)
            #
            # # -> Add header as key/value pair to attachment part
            # part.add_header(
            #     "Content-Disposition",
            #     f"attachment; filename= {filename}",
            # )
            #
            # # -> Add attachment to message and convert message to string
            # message.attach(part)
            text = message.as_string()

            # -> Log in to server using secure context and send email
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, text)

        except Exception as ex:
            logger.critical('---send_email---funn---EXCEPTION---', exc_info=True)
            logger.critical(f'---send_email---funn---EXCEPTION--msg: {ex}')
        finally:
            logger.info(f'---api_response: {0}')
            return 0


    def send_email_v2(self, subject, body, to_email):
        try:
            logger.info(f'---START---')
            EmailThread(subject, body, to_email).start()

        except Exception as ex:
            logger.critical('---send_email---funn---EXCEPTION---', exc_info=True)
            logger.critical(f'---send_email---funn---EXCEPTION--msg: {ex}')
        finally:
            logger.info(f'---api_response: {0}')
            return 0

