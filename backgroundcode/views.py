from django.shortcuts import render
from django.views import generic
from .models import Booking

class booklist(generic.ListView):
    queryset = Booking.objects.filter(status=1)
    template_name = 'backgroundcode/index.html'
    paginate_by = 6