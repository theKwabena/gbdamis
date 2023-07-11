from django.shortcuts import render
from django.contrib.auth.decorators import login_required 


from .forms import MemberUpdateForm
from .decorator import unapproved_user

from gbdamis.elections.models import Position, Nomination


# Create your views here.
@login_required
@unapproved_user
def member_dashboard(request):
    return render(request, 'member/member-dashboard.html')


def nomination(request):
    return render(request, 'nominations.html')


def member_profile(request):
    form = MemberUpdateForm(request.POST or None, instance=request.user)
    if form.is_valid():
        form.save();
    

    context = {
        'form': form
    }

    return render(request, 'member/member-profile.html', context)


def executives(request):
    executives = Position.objects.all()
    context = {
        "executives" : executives
    }
    return render(request, 'member/member-executives.html', context)


def nominate(request):
    nominees = Nomination.objects.all()
    context = {
        "nominees" : nominees
    }
    return render(request, 'member/member-nominees.html', context)


def dues(request):
    dues =request.user.get_all_dues
    return render(request, 'member/member-dues.html', {'dues': dues})
# def payment_history(request):
