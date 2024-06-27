# backgroundcode/views.py

import logging
from django.shortcuts import render
from django.views import generic
from .forms import BookingForm
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
            return bookings
        except Exception as e:
            logger.error("Error fetching bookings: %s", e)
            return []

def bookings(request):
    try:
        all_bookings = Booking.objects.all()
        logger.debug(f"Found {all_bookings.count()} bookings")
    except Exception as e:
        logger.error("Error fetching all bookings: %s", e)
        all_bookings = []

    return render(request, 'bookings.html', {'bookings': all_bookings})

# create bookings view function
def create_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            logger.info("Booking created successfully")
            return redirect('bookings')  # Redirect to bookings list or another page after successful booking creation
        else:
            logger.error("Form data is invalid")
    else:
        form = BookingForm()

    return render(request, 'bookings/create_booking.html', {'form': form})
