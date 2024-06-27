from django.shortcuts import render, redirect, get_object_or_404
from .forms import BookingForm
from .models import Booking, CustomUser
import logging

logger = logging.getLogger(__name__)

# View to display all bookings
def bookings(request):
    try:
        all_bookings = Booking.objects.all()
        logger.debug(f"Found {all_bookings.count()} bookings")
    except Exception as e:
        logger.error("Error fetching all bookings: %s", e)
        all_bookings = []

    return render(request, 'bookings.html', {'bookings': all_bookings})

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

    return render(request, 'create_booking.html', {'form': form})

# View to display details of a specific booking
def booking_detail(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    return render(request, 'booking_detail.html', {'booking': booking})