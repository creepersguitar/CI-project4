from django.urls import path
from . import views

urlpatterns = [
    path('', views.BookListView.as_view(), name='home'),
    path('bookings/', views.BookingListView.as_view(), name='bookings'),
    path('create-booking/', views.create_booking, name='create_booking'),
    path('booking/<int:booking_id>/', views.booking_detail, name='booking_detail'),
]
