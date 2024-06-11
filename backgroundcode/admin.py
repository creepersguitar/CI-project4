from django.contrib import admin
from .models import Booking, Profile, CustomUser

admin.site.register(Booking)
admin.site.register(Profile)
admin.site.register(CustomUser)