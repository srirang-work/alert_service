# models.py

from django.db import models
from django.conf import settings

from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    jwt_token = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.username

    class Meta:
        # Add related names to avoid clashes with default user model
        # Adjust these names as per your preference
        db_table = 'custom_user'
        managed = True
        default_related_name = 'custom_users'
        app_label = 'alert'
        swappable = 'AUTH_USER_MODEL'

class Alert(models.Model):
    STATUS_CHOICES = (
        ('created', 'Created'),
        ('triggered', 'Triggered'),
        ('deleted', 'Deleted'),
    )

    # Update the user field to reference the custom user model using settings.AUTH_USER_MODEL
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    cryptocurrency = models.CharField(max_length=10)
    target_price = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='created')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s alert for {self.cryptocurrency} at {self.target_price}"
