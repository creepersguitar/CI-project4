from . import views
from django.urls import path

urlpatterns = [
    path('', views.booklist.as_view(), name='home'),
    path('bookings/', views.bookings, name='bookings'),
    path('create/', views.create_booking, name='bookings:create'),
]
