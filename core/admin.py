from django.contrib import admin
from core.models import Event, JoinRequest

class TripAdmin(admin.ModelAdmin):
    pass

admin.site.register(Trip, TripAdmin)


class JoinRequestAdmin(admin.ModelAdmin):
    pass

admin.site.register(JoinRequest, JoinRequestAdmin)
