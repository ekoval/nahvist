from django.forms import ModelForm
from core.models import Trip
from registration.forms import RegistrationFormUniqueEmail
from django import forms


class UserRegistrationForm(RegistrationFormUniqueEmail):
    first_name = forms.CharField(max_length=40)
    last_name = forms.CharField(max_length=40)


class TripForm(ModelForm):
    class Meta:
        model = Trip
        fields = ['host_role', 'destination', 'description', 'vacant_seats_number', 'passengers_number']

    def __init__(self, *args, **kwargs):
        self._user = kwargs.pop('user')
        super(TripForm, self).__init__(*args, **kwargs)
