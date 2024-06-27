from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from .forms import BookingForm
from .models import Booking, CustomUser
import logging

logger = logging.getLogger(__name__)

# View to display all bookings
class BookListView(ListView):
    model = Booking
    template_name = 'index.html'
    context_object_name = 'bookings'
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

# View to create a new booking
def create_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            logger.info("Booking created successfully")
            return redirect('bookings')  # Redirect to bookings list after successful creation
        else:
            logger.error("Form data is invalid")
    else:
        form = BookingForm()

    return render(request, 'bookings/create_booking.html', {'form': form})

def booking_detail(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    return render(request, 'bookings/booking_detail.html', {'booking': booking})