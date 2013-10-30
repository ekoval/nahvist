from django.forms import ModelForm
from core.models import DriverTrip
from registration.forms import RegistrationFormUniqueEmail
from django import forms
from core.constants import ROLES


class UserRegistrationForm(RegistrationFormUniqueEmail):
    first_name = forms.CharField(max_length=40)
    last_name = forms.CharField(max_length=40)


class TripForm(ModelForm):
    class Meta:
        model = DriverTrip
        fields = ['move_to', 'start_date', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'cols': 20, 'rows': 2}),
        }

    def __init__(self, *args, **kwargs):
        self._user = kwargs.pop('user')
        super(TripForm, self).__init__(*args, **kwargs)
