# backgroundcode/views.py

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
            logger.debug("Attempting to fetch bookings with status=1")
            bookings = Booking.objects.filter(status=1)
            logger.debug(f"Found {bookings.count()} bookings")
            print('bookings:', bookings)
            return bookings
        except Exception as e:
            logger.error("Error fetching bookings: %s", e)
            return []
