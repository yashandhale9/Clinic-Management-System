from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator


class User(AbstractUser):
    """Custom User model extending AbstractUser"""
    USER_TYPE_CHOICES = [
        ('patient', 'Patient'),
        ('doctor', 'Doctor'),
    ]
    
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'users'
    
    def __str__(self):
        return f"{self.username} ({self.user_type})"


class Address(models.Model):
    """Address model for users"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='address')
    line1 = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(
        max_length=10,
        validators=[RegexValidator(regex=r'^\d{5,10}$', message='Pincode must be 5-10 digits')]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'addresses'
    
    def __str__(self):
        return f"{self.line1}, {self.city}, {self.state} - {self.pincode}"


class Patient(models.Model):
    """Patient model"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='patient_profile')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'patients'
    
    def __str__(self):
        return f"Patient: {self.user.username}"


class Doctor(models.Model):
    """Doctor model"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='doctor_profile')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'doctors'
    
    def __str__(self):
        return f"Doctor: {self.user.username}"

