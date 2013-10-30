from django.db import models
from django.contrib.auth.models import AbstractUser
from core.constants import TRIP_STATES, REQUEST_STATES, ROLES


class User(AbstractUser):
    fb_profile = models.URLField()


class Car(models.Model):
    """Describes car."""
    user = models.ForeignKey(User)
    description = models.CharField(max_length=50)
    passenger_seats = models.IntegerField()


class DriverTrip(models.Model):
    """Describes trip."""
    user = models.ForeignKey(User)
    move_from = models.CharField(max_length=100)
    move_to = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    state = models.CharField(max_length=10, choices=TRIP_STATES)
    start_date = models.DateField()
    start_time = models.TimeField()
    seats_number = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()


class PassengerTrip(models.Model):
    """Describes trip."""
    user = models.ForeignKey(User)
    move_from = models.CharField(max_length=100)
    move_to = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    state = models.CharField(max_length=10, choices=TRIP_STATES)
    start_date = models.DateField()
    start_time = models.TimeField()
    number_of_people = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()


class JoinDriverRequest(models.Model):
    """Request is created when somebody wants to join some trip."""
    user = models.ForeignKey(User)
    trip = models.ForeignKey(DriverTrip)
    state = models.CharField(max_length=10, choices=REQUEST_STATES)
    message = models.TextField()
    number_of_people = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()


class TakePassengerRequest(models.Model):
    """Request is created when somebody wants to join some trip."""
    user = models.ForeignKey(User)
    trip = models.ForeignKey(DriverTrip)
    state = models.CharField(max_length=10, choices=REQUEST_STATES)
    message = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
