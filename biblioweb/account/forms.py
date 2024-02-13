from django import forms


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegistrationForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput)
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
