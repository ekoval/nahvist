from django.db.models
from django.contrib.auth.models import User
from core.constants import EVENT_STATES, REQUEST_STATES, ROLES


class Car(models.Model):
    """Describes car."""
    user = models.ForeignKey(User)
    description = CharField(max_length=50)
    passenger_seats = models.IntegerField()


class Trip(models.Model):
    """Describes trip."""
    host = models.ForeignKey(User)
    host_role = models.CharField(choices=ROLES)
    destination = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    car = models.ForeignKey(Car)
    created = models.DateTimeField()
    state = models.CharField(max_length=10, choices=TRIP_STATES)
    vacant_seats_number = models.IntegerField()
    passengers_number = models.IntegerField()


class JoinRequest(Model):
    """Request is created when somebody wants to join some trip."""
    user = ForeignKey(User)
    trip = ForeignKey(Trip)
    role = CharField(max_length=10, choices=ROLES)
    state = CharField(max_length=10, choices=REQUEST_STATES)
    created = DateTimeField()
    state_changed = DateTimeField()
    number_of_people = IntegerField()
