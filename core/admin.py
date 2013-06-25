from django.contrib import admin
from core.models import Event, JoinRequest

class EventAdmin(admin.ModelAdmin):
    pass

admin.site.register(Event, EventAdmin)


class JoinRequestAdmin(admin.ModelAdmin):
    pass

admin.site.register(JoinRequest, JoinRequestAdmin)
