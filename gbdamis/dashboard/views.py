from django.shortcuts import render

# Create your views here.
from django.shortcuts import render





from .forms import AnnouncementForm

# Create your views here.


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