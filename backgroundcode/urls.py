from . import views
from django.urls import path

urlpatterns = [
    path('', views.booklist.as_view(), name='home'),
    ]