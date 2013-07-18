from django.db import models
from django.contrib.auth.models import User
from core.constants import TRIP_STATES, REQUEST_STATES, ROLES


class Car(models.Model):
    """Describes car."""
    user = models.ForeignKey(User)
    description = models.CharField(max_length=50)
    passenger_seats = models.IntegerField()


class Trip(models.Model):
    """Describes trip."""
    host = models.ForeignKey(User)
    host_role = models.CharField(max_length=10, choices=ROLES)
    destination = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    state = models.CharField(max_length=10, choices=TRIP_STATES)
    vacant_seats_number = models.IntegerField()
    passengers_number = models.IntegerField()


class JoinRequest(models.Model):
    """Request is created when somebody wants to join some trip."""
    user = models.ForeignKey(User)
    trip = models.ForeignKey(Trip)
    role = models.CharField(max_length=10, choices=ROLES)
    state = models.CharField(max_length=10, choices=REQUEST_STATES)
    created = models.DateTimeField()
    state_changed = models.DateTimeField()
    number_of_people = models.IntegerField()
