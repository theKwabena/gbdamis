import json
import logging

from django.core import serializers
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
# Create your views here.
from django.shortcuts import render



from elections.models import Nomination, Position
from elections.forms import PositionForm, NominationForm
from authentication.forms import SignUpForm
from .forms import AnnouncementForm, AddMemberForm, NewsForm
from.models import News, Announcement
from .utils import is_ajax

log = logging.getLogger(__name__)
User = get_user_model()

def admin_dashboard(request):
    return render(request, 'dashboard/index2.html')


#Events
def events(request):
    return render(request, 'dashboard/events.html')


#Nominations
def nominations(request):
    positions =Position.objects.all()
    nominations = Nomination.objects.all()
    log.info(positions)
    position_form = PositionForm(None)
    nomination_form = NominationForm(None)
    if is_ajax(request) and request.method == 'POST':
        log.info(request.POST)
        form_type = request.POST.get('form_id')
        if form_type== 'position-form':
            position_form = PositionForm(request.POST or None)
            if position_form.is_valid():
                position_form.save()
                return JsonResponse({
                    'success': True, 
                    'title': 'Position added successfully', 
                    'text': 'New position added successfully'
                })
            else:
                log.warning(position_form.errors.as_json())
                return JsonResponse({'success': False, 'errors' : position_form.errors.as_json()})
        elif form_type == 'nomination-form':
            nomination_form = NominationForm(request.POST or None)
            if nomination_form.is_valid():
                nomination_form.save()
                return JsonResponse({
                    'success': True, 
                    'title': 'Nomination added successfully', 
                    'text': 'New nomination added successfully'
                })
            else:
                log.info(nomination_form.errors.as_json())
                return JsonResponse({
                    'sucess': False, 
                    'errors': nomination_form.errors.as_json()
                })
    context = {
        'position_form': position_form,
        'nomination_form' : nomination_form,
        'positions': positions,
        'nominations' : nominations
    }
    return render(request, 'dashboard/nominations.html', context)

def delete_position(request, pk):
    position = get_object_or_404(Position, pk=pk)
    position.delete()
    messages.success(request, 'Position deleted successfully')
    return redirect('nomination')
# def update_delete_positons(request):


#News
def news(request, id=None):
    news = News.objects.all()
    form = NewsForm(request.POST or None)
    if is_ajax(request) and request.method == 'POST':
        action = request.POST.get('action')
        news_id =request.POST.get('news_id')
        news_obj = News.objects.get(id=news_id)
        if action  == 'update':
            news_obj.title = request.POST.get('new_title')
            news_obj.description = request.POST.get('new_description')
            news_obj.save()
            return JsonResponse({'success' : True, 'message': 'News updated successfully' })
        if action == 'delete':
            news_obj.delete()
            return JsonResponse({'message': 'News deleted successfully'})
        
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'News added successfully')
            return redirect('news')
        else:
            return JsonResponse({'success': False})
    else:
        form = NewsForm()

    context = {
        'form' : form,
        'news' : news
    }
    return render(request, 'dashboard/news.html', context)

def add_news(request):
    if is_ajax(request) and request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success' : True})
        else:
            return JsonResponse({'success': False})
    else:
        return JsonResponse({'error' : 'Invalid request'})

def news_item(request, id):
    if is_ajax(request):
        news_obj = News.objects.get(id=id)
        data = {
            'title' : news_obj.title,
            'description' : news_obj.description
        }
        return JsonResponse({'data': data })
    else:
        context = {
            'announcement': news_obj
        }
        return render(request, 'announcement.html', context)
    


#Announcement
def announcements(request):
    announcements = Announcement.objects.all()
    form = AnnouncementForm(request.POST or None)
    if is_ajax(request) and request.method == 'POST':
        action = request.POST.get('action')
        announcement_id =request.POST.get('announcement_id')
        announcement_obj = Announcement.objects.get(id=announcement_id)
        if action  == 'update':
            announcement_obj.title = request.POST.get('new_title')
            announcement_obj.description = request.POST.get('new_description')
            announcement_obj.save()
            return JsonResponse({'message': 'Announcement updated successfully' })
        if action == 'delete':
            announcement_obj.delete()
            return JsonResponse({'message': 'Annoncement deleted successfully'})
        else:
            log.warning('error')

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Announcement added successfully')
            return redirect('announcements')
        else:
            return JsonResponse({'success': False})
    else:
        form = AnnouncementForm()

    context = {
        'form' : form,
        'announcements' : announcements
    }
    return render(request, 'dashboard/announcements.html', context)


def announcement(request, id):
    announcement_obj = Announcement.objects.get(id=id)
    if is_ajax(request):
       
        data = {
            'title' : announcement_obj.title,
            'description': announcement_obj.description
        }
        return JsonResponse({'data': data })
    else:
        context = {
            'announcement': announcement_obj
        }
        return render(request, 'announcement.html', context)


def add_announcements(request):
    form = AnnouncementForm

    context = {
        'form': AnnouncementForm
    }
    return render(request, 'dashboard/addAnnouncement.html', context)

def edit_announcement(request, id):
    if is_ajax(request):
        announcement_obj = Announcement.objects.get(id=id)
        announcement_obj.title =  request.POST.get('title')
        announcement_obj.description = request.POST.get('description')
        announcement_obj.save()
        return JsonResponse({'data' : 'Announcement deleted successfully'})
    else:
        return None
        
#Members
def members(request):
    members = User.objects.all()
    context = {
        'members' : members,
    }
    return render(request, 'dashboard/members.html', context)

def add_member(request):
    form = AddMemberForm(request.POST or None)
    if request.method == 'POST':
        username = request.POST.get('username')
        if form.is_valid():
            user= form.save()
            user.set_password(username)
            messages.success(request, str(user.first_name) + ' ' + str(user.other_names) + 'added successfully')
            return redirect('members')
    else:
        form = SignUpForm()
    return render(request, 'dashboard/add_member.html', {'form':form})

def edit_member(request, id):
    user = User.objects.get(id=id)
    form = AddMemberForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, str('changes on user ' + str(user.first_name) + str(user.other_names) + ' saved successfully'))
        return redirect('members')
    else:
        form=SignUpForm(instance=user)
    return render(request, 'dashboard/add_member.html', {'form' :form})

def remove_member(request, id):
    member = get_object_or_404(User, pk=id)
    if is_ajax(request) and request.method=='GET':
        try:
            member.delete()
            return JsonResponse({'deleted' : True})
        except:
            return JsonResponse({'delete': False})
    else:
        return JsonResponse({'deleted' : False}, status=402)

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
    
def make_admin(request, id):
    user = get_object_or_404(User, pk=id)
    user.admin = True
    user.save()
    if is_ajax(request) and request.method=='GET':
        return JsonResponse({'success': True})
    else:
        messages.success(request, 'User is now an admin')
        return redirect('members')

def remove_admin(request, id):
    user = get_object_or_404(User,pk=id)
    if user.admin:
        user.admin = False
        user.save()
    if is_ajax(request) and request.method == 'GET':
        return JsonResponse({'success':True})
    else:
        messages.success(request,'User is now an admin')
        return redirect('members')
#Add and Edit User Validationns and Authorizations
def check_password(request):
    user = request.user
    if is_ajax(request) and request.method=='POST':
        password = request.POST.get('password')
        log.info(password)
        if user.check_password(password):
            return JsonResponse({'has_permission' : True})
        else:
            return JsonResponse({'has_permission' : False}, status=200) 
    else:
        return JsonResponse({'deleted' : 'false'}, status=400)
    
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
        

