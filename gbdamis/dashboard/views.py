from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.http import JsonResponse
import logging
log = logging.getLogger(__name__)
# Create your views here.
from django.shortcuts import render




from authentication.forms import SignUpForm
from .forms import AnnouncementForm, AddMemberForm
from .utils import is_ajax

User = get_user_model()

def admin_dashboard(request):
    return render(request, 'dashboard/index2.html')

def events(request):
    return render(request, 'dashboard/events.html')



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

def members(request):
    members = User.objects.filter(admin=False)

    context = {
        'members' : members
    }
    return render(request, 'dashboard/members.html', context)

def remove_member(request, id):
    member = get_object_or_404(User, pk=id)
    if is_ajax(request) and request.method=='DELETE':
        member.delete()
        return JsonResponse({'deleted' : 'True'})
    else:
        return JsonResponse({'deleted' : 'false'}, status=400)






def add_member(request):
    form = AddMemberForm(request.POST or None)
    if request.method == 'POST':
        username = request.POST.get('username')
        if form.is_valid():
            email = form.cleaned_data.get('email')
            phone_number = form.cleaned_data.get('phone_number')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('other_names')
            user = User(
                username = username,
                first_name = first_name,
                other_names = last_name,
                phone_number = phone_number,
                email = email
            )
            user.set_password(username)
            user.save()
            return redirect('members')
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
        return JsonResponse({'error': 'invalid request'}, status=400)
    
def check_email(request):
    if is_ajax(request) and request.method == 'POST':
        email = request.POST.get('email')
        if User.objects.filter(email=email).exists():
            return JsonResponse({'exists' : True})
        else:
            return JsonResponse({'exists': False})
    else:
        return JsonResponse({'error': 'invalid request'}, status=400)
    
def check_phone_number(request):
    if is_ajax(request) and request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        if User.objects.filter(phone_number=phone_number).exists():
            return JsonResponse({'exists': True})
        else:
            return JsonResponse({'exists': False})
    else:
        return JsonResponse({'error': 'invalidd request'}, status=400)
        
        