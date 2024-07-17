from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from .forms import BookingForm
from .models import Booking
from django.http import JsonResponse
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

                # Assuming you want to return a JSON response indicating success
                return JsonResponse({'success': True})

            # Handle form errors if not valid
            errors = form.errors.as_json()
            return JsonResponse({'success': False, 'errors': errors})

        else:
            form = BookingForm()
        return render(request, 'create_booking.html', {'form': form})

    @login_required
    def booking_detail(request, booking_id):
        booking = get_object_or_404(Booking, id=booking_id)
        heroLink = 'booking_detail'
        return render(request, 'booking_detail.html', {'booking': booking})
