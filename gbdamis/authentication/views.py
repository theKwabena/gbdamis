from django.shortcuts import render, redirect

from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.contrib.auth import authenticate, login, logout
import logging
log = logging.getLogger(__name__)

from .forms import (
    LoginForm, SignUpForm
)

# Create your views here.
def login_view(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            remember = form.cleaned_data['agree']
            # log.info(remember)
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if not remember:
                    request.session.set_expiry(0)  
                if user.is_admin:
                    return redirect('admin-dashboard')
                else:  
                    return redirect('member-dashboard')
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = LoginForm()

    return render(request, 'account/login.html', {'form': form})


def sign_up_view(request):
    form = SignUpForm(request.POST or None)
    if request.method == "POST":
            if form.is_valid():
                user = form.save()
                user.save()

                #Log in the user
                _user = authenticate(request, username=user.username, password = form.cleaned_data.get('password1'))
                login(request, _user)

                return redirect('member-dashboard')
            # else:
            #     fmsg = ('Check form details and try again')
    else:
        form = SignUpForm()
    return render(request, 'account/signup.html', {'form': form})


def verification_sent(request):
    
    return render(request, 'account/auth-email-verification.html')



# def sendVerificationEmail(request):
#     current_site = get_current_site(request)
#     email_subject = 'Activate Your Physics FYP Account'
#     email_body = render_to_string('notifications/supervisorConfirm.html', {
#         'user': request.user,
#         'domain': current_site,
#         'uid': urlsafe_base64_encode(force_bytes(request.user.id)),
#         'token' : generate_supervisor_token.make_token(request.user),
#         'email' : request.user.email 
#     })
#     send_verification_email.delay(subject = email_subject, body = email_body,  recipient = request.user.email)
    
#     return render(request, 'accounts/verificationEmailSent.html')