from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.http import JsonResponse
import logging
log = logging.getLogger(__name__)
# Create your views here.
from django.shortcuts import render




from authentication.forms import SignUpForm
from .forms import AnnouncementForm
from .utils import is_ajax

User = get_user_model()

def admin_dashboard(request):
    return render(request, 'dashboard/index2.html')

def events(request):
    return render(request, 'dashboard/events.html')

def members(request):
    return render(request, 'dashboard/members.html')

def nominations(request):
    positions = Position.objects.all()

    context = {
        'positions': positions
    }
    return render(request, 'dashboard/nominations.html', context)

def news(request):
    return render(request, 'dashboard/news.html')


def announcements(request):
    return render(request, 'dashboard/announcements.html')

def add_announcements(request):
    form = AnnouncementForm

    context = {
        'form': AnnouncementForm
    }
    return render(request, 'dashboard/addAnnouncement.html', context)


def add_member(request):
    form = SignUpForm(request.POST or None)
    if form.is_valid():
        pass
    else:
        form = SignUpForm()


    return render(request, 'dashboard/add_member.html', {'form':form})

def generate_username(request):
    if is_ajax(request) and request.method == 'POST':
        first_name = request.POST.get('first_name')
        other_names = request.POST.get('other_names')
        log.info(first_name)
        log.info(other_names)
        user = User(first_name = first_name, other_names = other_names)
        username = user.generate_username()
        log.info(username)
        return JsonResponse({'username' : username})
    else:
        return JsonResponse({'error': 'invalid request'})