from django.shortcuts import render
from django.views import generic
from .models import Booking

class booklist(generic.ListView):
    model = Booking
    template_name = 'booking_list.html'