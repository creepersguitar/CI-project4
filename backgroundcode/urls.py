from . import views
from django.urls import path

urlpatterns = [
    path('', views.booklist.as_view(), name='home'),
    path('<slug:slug>/', views.booking_detail, name='booking_detail'),
]
