from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from .forms import BookingForm
from .models import Booking
import logging

logger = logging.getLogger(__name__)


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


@login_required
def create_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.author = request.user  # Set the author to the current user
            booking.save()
            
            # Redirect to a success page or another relevant page after successful booking
            return redirect('booking_successful')
        # If the form is invalid, re-render the form with the errors
        return render(request, 'create_booking.html', {'form': form})

    # For GET requests, render the booking form
    form = BookingForm()
    return render(request, 'create_booking.html', {'form': form})

@login_required
def booking_detail(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    heroLink = 'booking_detail'
    return render(request, 'booking_detail.html', {'booking': booking})

def booking_successful(request):
    return render(request, 'booking_success.html')