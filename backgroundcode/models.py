from django.db import models
from django.contrib.auth.models import User

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
    email = models.TextField()
    phone = models.CharField(max_length=15)
    website = models.URLField()

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"Profile of {self.user.username}"

class Booking(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookings")
    content = models.TextField()
    excerpt = models.TextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    
    # New fields added
    name = models.CharField(max_length=100)
    time = models.TimeField()
    guests = models.IntegerField()
    date = models.DateField()
    email = models.EmailField()

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"Booking: {self.title} by {self.author}"
