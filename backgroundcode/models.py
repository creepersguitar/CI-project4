from django.db import models
from django.contrib.auth.models import User
from datetime import date, time, datetime

STATUS = ((0, "Draft"), (1, "Published"))

class CustomUser(models.Model):
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        ordering = ['email']

    def __str__(self):
        return self.email
    
class Profile(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    email = models.TextField(default='example@example.com')
    phone = models.CharField(max_length=15, default=274560901928406)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"Profile of {self.user.username}"

class Booking(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)    
    # New fields added
    name = models.CharField(max_length=100, default='default_name')
    time = models.TimeField(default=time(12,0))
    guests = models.IntegerField(default=1)
    date = models.DateField(default=date.today)
    email = models.EmailField(default='example@example.com')

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"Booking: {self.created_on} by {self.name}"
