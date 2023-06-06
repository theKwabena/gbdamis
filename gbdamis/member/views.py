from django.shortcuts import render

# Create your views here.
def member_dashboard(request):
    return render(request, 'member/member-dashboard.html')


def nomination(request):
    return render(request, 'nominations.html')


def forum(request):
    return render(request, 'forum/members-forum.html')