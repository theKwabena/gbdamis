import logging

from django.contrib.auth import get_user_model
from django.conf import settings
from django.core.mail import send_mail, EmailMessage

from celery import shared_task


from config.celery_app import app



# import logger
log = logging.getLogger(__name__)

# import logger
import logging
log = logging.getLogger(__name__)


@app.task   
def send_email(subject, body,  recipient):
    email = EmailMessage(
        subject = subject,
        body = body,
        from_email = settings.EMAIL_HOST_USER,
        to = [recipient]        
    )
    email.fail_silently = False 
    
    email.content_subtype = "html"  # Main content is now text/html
    log.info("Sending the email here")
    email.send()
    return str(recipient)

