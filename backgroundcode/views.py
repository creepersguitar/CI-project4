import logging
from django.shortcuts import render
from django.views import generic
from .models import Booking

logger = logging.getLogger(__name__)

class booklist(generic.ListView):
    template_name = 'index.html'
    paginate_by = 6

    def get_queryset(self):
        try:
            return Booking.objects.filter(status=1)
        except Exception as e:
            logger.error("Error fetching bookings: %s", e)
            return []
