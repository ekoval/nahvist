from django.contrib import admin
from core.models import User, DriverTrip, PassengerTrip, JoinDriverRequest

admin.site.register(User)
admin.site.register(DriverTrip)
admin.site.register(PassengerTrip)
admin.site.register(JoinDriverRequest)
