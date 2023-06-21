import logging

from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.mail import send_mail, EmailMessage

from celery import shared_task


from config.celery_app import app


User = settings.AUTH_USER_MODEL
# import logger
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


@app.task   
def send_all_admin_email(subject, body):
    recipients = list(User.objects.filter(admin=True).values_list('email', flat=True))
    email = EmailMessage(
        subject = subject,
        body = body,
        from_email = settings.EMAIL_HOST_USER,
        to = recipients      
    )
    email.fail_silently = False 
    email.content_subtype = "html"  # Main content is now text/html
    log.info("Sending the email here")
    email.send()
    return str(recipients)

    
    
    
    