from django.shortcuts import render, redirect

from django.http import JsonResponse
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.template.loader import render_to_string
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
import logging
log = logging.getLogger(__name__)

from .forms import (
    LoginForm, SignUpForm
)

from dashboard.utils import is_ajax
from .tasks import send_all_admin_email, send_email
from .utils import generate_verification_token

User = get_user_model()

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
                
                #Send admins new sign up mail
                current_site = get_current_site(request)
                email_subject = 'New Sign Up Alert'
                email_body = render_to_string('emails/new_signup.html', {
                'member': request.user,
                'domain': current_site,
                })

                send_all_admin_email.delay(subject = email_subject, body = email_body)

                return redirect('send-verification-email')
            # else:
            #     fmsg = ('Check form details and try again')
    else:
        form = SignUpForm()
    return render(request, 'account/signup.html', {'form': form})


def verification_sent(request):
    return render(request, 'account/account_verification_submitted.html')

def verified(request):
    return (request, 'account/account-verified-submitted')

def send_verification_email(request):
   

    if is_ajax(request) and request.POST.get('new_email'):
        email = request.POST.get('email')
        request.user.email = email
        request.user.save()
    else:
        email = request.user.email

    current_site = get_current_site(request)
    email_subject = 'Activate Your Physics FYP Account'
    email_body = render_to_string('emails/confirm_verification_email.html', {
        'user': request.user,
        'domain': current_site,
        'uid': urlsafe_base64_encode(force_bytes(request.user.id)),
        'token' : generate_verification_token.make_token(request.user),
        'email' : email 
    })
    send_email.delay(subject = email_subject, body = email_body,  recipient = email)
    
    if is_ajax(request) and request.POST.get('new_email'):
        return JsonResponse({'success' : True})
    elif is_ajax(request) and request.POST.get('resend'):
        return JsonResponse({'success' : True})
    return render(request, 'account/auth-email-verification.html')




def verify_user(request, email, uid64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uid64))
        user = User.objects.get(id=uid)
    except Exception as e:
        user = None
        
    if user and generate_verification_token.check_token(user, token):
        user.email = email
        user.verified = True
        user.save()
        return render(request, 'account/account_verification_submitted.html')
    return render(request, 'home/activation_failed.html', {'user': user,})


def pending_verification(request):
    return render(request, 'account/pending-verification.html')