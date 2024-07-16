# forms.py
from django import forms
from .models import Booking, Profile

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['title', 'slug', 'content', 'excerpt', 'status', 'name', 'time', 'guests', 'date', 'email']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'email', 'phone']