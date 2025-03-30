from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from datetime import date
# Create your models here.


class Table(models.Model):
    number = models.IntegerField(unique=True)
    capacity = models.IntegerField()
    
    def __str__(self):
        return f"Table {self.number} - {self.capacity} seats"
    
class Booking(models.Model):
    STATUS_Dic = [
        ('waiting', 'Waiting for Confirmation'),
        ('confirmed', 'Confirmed'),
        ('rejected', 'Rejected')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    guests = models.IntegerField(default=1)
    status = models.CharField(max_length=10, choices=STATUS_Dic, default='waiting')
    rejection_reason = models.TextField(blank=True, null=True)  # Custom message from admin


    # Prevent double bookings
    class Meta:
        unique_together = ('table', 'date', 'time')  
    
    def __str__(self):
        return f"{self.user.username} - {self.date} {self.time}"
    
        # Custom validation to ensure guests are within a valid range and the booking is in the future
    def clean(self):
        if self.guests < 1:
            raise ValidationError("The number of guests shall be at least one.")
        elif self.guests > self.table.capacity:
            raise ValidationError(f"Number of guests ({self.guests}) cannot exceed the capacity of the table ({self.table.capacity}).")
        elif self.time == None:
            raise ValidationError("The time field is required.")
        elif self.date <= date.today():
            raise ValidationError("The booking date must be in the future.")
        
    
    # Save method overridden to call clean before saving
    def save(self, *args, **kwargs):
        self.clean()  # Call the custom validation method
        super().save(*args, **kwargs)
    
class MenuItem(models.Model):
    CATEGORY_CHOICES = [
        ('appetizer', 'Appetizer & Salads'),
        ('main_course', 'Main Course'),
        ('dessert', 'Dessert'),
        ('beverage', 'Beverage'),
    ]
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='menu_images/', blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)  # Category of the dish
    available = models.BooleanField(default=True)  # Availability of the dish
    
    def __str__(self):
        return self.name