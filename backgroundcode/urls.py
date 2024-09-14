from django.urls import path
from . import views

urlpatterns = [
    path('', views.BookListView.as_view(), name='home'),
    path('bookings/', views.BookListView.as_view(), name='booking_list'),
    path('create-booking/', views.create_booking, name='create_booking'),
    path('booking/<int:booking_id>/', views.booking_detail, name='booking_detail'),
    path('booking-success/', views.booking_successful, name='booking_success'),
    path('view_booking/', views.view_booking, name='view_booking'),
    path('update_booking/<int:booking_id>/', views.update_booking, name='update_booking'),
    path('delete_booking/<int:booking_id>/', views.delete_booking, name='delete_booking'),
]
