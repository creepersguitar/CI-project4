from django.contrib import admin
from .models import Booking, Profile, CustomUser
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Booking)
class BookingAdmin(SummernoteModelAdmin):

    list_display = ('name', 'date', 'time', 'guests', 'email', 'created_on')
    search_fields = ('name', 'email')
    #list_filter = ('created_on')
    summernote_fields = ('content',)

admin.site.register(Profile)
admin.site.register(CustomUser)
