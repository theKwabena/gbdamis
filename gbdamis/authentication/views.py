from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from .forms import LoginForm

# Create your views here.
def login_view(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            remember = form.cleaned_data['agree']
            print(remember)
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if not remember:
                    request.session.set_expiry(0)   
                return redirect('home')
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = LoginForm()

    return render(request, 'account/login.html', {'form': form})
