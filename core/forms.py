from django.forms import ModelForm
from core.models import Trip
from registration.forms import RegistrationFormUniqueEmail
from django import forms


class UserRegistrationForm(RegistrationFormUniqueEmail):
    first_name = forms.CharField(max_length=40)
    last_name = forms.CharField(max_length=40)

