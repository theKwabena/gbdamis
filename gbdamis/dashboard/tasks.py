import logging

from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail, EmailMessage


from django.contrib.auth import get_user_model
from config.celery_app import app

# import logger
User = get_user_model()
log = logging.getLogger(__name__)


@app.task   
def send_all_admin_mails(subject, body):
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



@app.task()
def make():
    return "Make"
    

    
    
    
    