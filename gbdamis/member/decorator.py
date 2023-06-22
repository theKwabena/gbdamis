from django.http import HttpResponse


from django.shortcuts import redirect



def unapproved_user(view_func):
    def wrapper_func(request, *args, **kwargs ):
        if request.user.approved:
            return view_func(request, *args, **kwargs)
        else:
            return redirect('pending-approval')
    return wrapper_func