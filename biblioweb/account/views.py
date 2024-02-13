from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.urls import reverse
from .forms import LoginForm, RegistrationForm


def user_login(request: HttpRequest) -> HttpResponse:

    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(
                username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                print('User succesuffly logged in!')
                return HttpResponseRedirect(reverse('main:index'))
            else:
                print('Username or password is incorrect.')
                return HttpResponse('Username or password is incorrect.')
        else:
            login_form = LoginForm(request.POST)
            return render(request, 'account/login.html', {'form': login_form})

    if request.method == 'GET':
        login_form = LoginForm()
        return render(request, 'account/login.html', {'form': login_form})


def registration(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        registration_form = RegistrationForm(request.POST)
        if registration_form.is_valid():
            # TODO: Start session here
            return HttpResponseRedirect(reverse('main:index'))
        else:
            registration_form = RegistrationForm(request.POST)
            return render(request, 'account/registration.html', {'form': registration_form})

    if request.method == 'GET':
        registration_form = RegistrationForm()
        return render(request, 'account/registration.html', {'form': registration_form})
