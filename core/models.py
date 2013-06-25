from django.db.models import Model, ForeignKey, CharField, DateTimeField
from django.contrib.auth.models import User
from core.constants import EVENT_STATES, REQUEST_STATES, ROLES


class Event(Model):
    host = ForeignKey(User)
    name = CharField(max_length=100)
    description = CharField(max_length=500)
    created = DateTimeField()
    state = CharField(max_length=10, choices=EVENT_STATES)


class JoinRequest(Model):
    user = ForeignKey(User)
    event = ForeignKey(Event)
    role = CharField(max_length=10, choices=ROLES)
    state = CharField(max_length=10, choices=REQUEST_STATES)
    created = DateTimeField()
    state_changed = DateTimeField()
