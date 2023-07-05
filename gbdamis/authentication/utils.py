import six
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes

from django.template.loader import render_to_string
from django.contrib.auth.tokens import PasswordResetTokenGenerator


class UserVerificationEmailTokenGenerator(PasswordResetTokenGenerator):
    
    def _make_harsh_value(self,user, timestamp):
        return (six.text_type (user.id) + six.text_type(timestamp) + six.text_type(user.verified))
    
    
generate_verification_token = UserVerificationEmailTokenGenerator()




