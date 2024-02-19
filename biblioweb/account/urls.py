from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('registration/', views.registration, name='registration'),
    path('logout/', views.logout_user, name='logout'),
]
