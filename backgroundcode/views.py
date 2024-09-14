from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from .forms import BookingForm
from .models import Booking
import logging

logger = logging.getLogger(__name__)

# ListView to display bookings
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

# View to create a booking
@login_required
def create_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.author = request.user  # Set the author to the current user
            booking.save()
            
            # Redirect to the 'booking_success' page after successful booking
            return redirect('booking_success')  # Ensure URL pattern matches this name
        
        # If the form is invalid, re-render the form with the errors
        return render(request, 'create_booking.html', {'form': form})

    # For GET requests, render the booking form
    form = BookingForm()
    return render(request, 'create_booking.html', {'form': form})

# View to display a booking's details
@login_required
def booking_detail(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    return render(request, 'booking_detail.html', {'booking': booking})

# View for successful booking
def booking_successful(request):
    return render(request, 'booking_success.html')

@login_required
def view_booking(request):
    # Get all bookings for the logged-in user (author)
    bookings = Booking.objects.filter(author=request.user)
    
    # Log the number of bookings retrieved
    logger.debug(f"Number of bookings found: {bookings.count()}")

    # Render the bookings in the template
    return render(request, 'view_booking.html', {'bookings': bookings})

@login_required
def update_booking(request, booking_id):
    # Get the booking instance based on the booking ID
    booking = get_object_or_404(Booking, id=booking_id)

    # Ensure that the user updating the booking is the author of the booking
    if booking.author != request.user:
        return redirect('view_booking')  # Redirect if user is not the author
    
    # Handle the POST request to update the booking
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)  # Pass the existing booking to the form
        if form.is_valid():
            form.save()  # Save the updated booking
            return redirect('view_booking')  # Redirect to the bookings list after updating
    
    # Handle the GET request by pre-filling the form with the current booking details
    else:
        form = BookingForm(instance=booking)  # Pre-fill the form with current booking details

    # Render the form for updating the booking
    return render(request, 'update_booking.html', {'form': form, 'booking': booking})

@login_required
def delete_booking(request, booking_id):
    # Get the booking instance
    booking = get_object_or_404(Booking, id=booking_id)

    # Ensure that the user deleting the booking is the author of the booking
    if booking.author != request.user:
        return redirect('view_booking')  # Redirect if user is not the author
    
    # Handle POST request to delete the booking
    if request.method == 'POST':
        booking.delete()  # Delete the booking
        return redirect('view_booking')  # Redirect to the bookings list after deletion

    # Render a confirmation page before deleting (optional)
    return render(request, 'confirm_delete.html', {'booking': booking})