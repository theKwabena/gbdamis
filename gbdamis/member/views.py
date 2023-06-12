from django.shortcuts import render

from .forms import MemberUpdateForm

# Create your views here.
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