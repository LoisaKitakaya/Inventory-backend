from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout as django_logout, login as django_login
from django.contrib import messages

# Create your views here.

def login(request):

    if request.method == 'POST':

        form = AuthenticationForm(data=request.POST)

        if form.is_valid():

            user = form.get_user()

            django_login(request, user)

            messages.success(request, 'Successfully logged in.')

            return redirect('home')

    else:

        form = AuthenticationForm()

    page_title = 'Login to your account'

    context = {
        'form' : form,
        'page_title': page_title,
    }

    return render(request, 'accounts/login.html', context)

def logout(request):

    django_logout(request)

    messages.error(request, 'You have been logged out.')

    return redirect('home')