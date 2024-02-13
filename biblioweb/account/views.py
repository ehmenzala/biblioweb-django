from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import LoginForm, RegistrationForm


def login(request: HttpRequest) -> HttpResponse:

    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            # TODO: Start session here
            return HttpResponseRedirect(reverse('main:index'))
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
