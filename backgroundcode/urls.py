from . import views
from django.urls import path

urlpatterns = [
    path('', views.BookListView.as_view(), name='home'),
    path('bookings/', views.Booking, name='bookings'),
]
