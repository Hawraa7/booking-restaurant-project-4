from django.db import models  # Importing the models module
from django.contrib.auth.models import User  # Importing the User model
from django.core.exceptions import ValidationError  # Importing ValidationError
from datetime import date  # Importing date

# Create your models here.


# Defining the Table model to represent restaurant tables
class Table(models.Model):
    # Table number should be unique to avoid duplicates
    number = models.IntegerField(unique=True)
    # Capacity of the table (number of seats it can hold)
    capacity = models.IntegerField()

    # String representation of the Table object
    def __str__(self):
        return f"Table {self.number} - {self.capacity} seats"


# Defining the Booking model to represent a customer's booking
class Booking(models.Model):
    # Defining possible status choices for the booking
    STATUS_Dic = [
        ('waiting', 'Waiting for Confirmation'),
        ('confirmed', 'Confirmed'),
        ('rejected', 'Rejected')
    ]
    # Foreign key linking the booking to a user
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Foreign key linking the booking to a table
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    # Date of the booking
    date = models.DateField()
    # Time of the booking
    time = models.TimeField()
    # Number of guests for the booking (default is 1)
    guests = models.IntegerField(default=1)
    # Status of the booking (waiting by default)
    status = models.CharField(max_length=10, choices=STATUS_Dic,
                              default='waiting')
    # Optional rejection reason (used if booking is rejected)
    rejection_reason = models.TextField(blank=True, null=True)

    class Meta:
        unique_together = ('table', 'date', 'time')

    # String representation of the Booking object
    def __str__(self):
        return f"{self.user.username} - {self.date} {self.time}"

    # Custom validation method for the booking model
    def clean(self):
        # Validation to ensure there is at least one guest
        if self.guests < 1:
            raise ValidationError("Number of guests shall be at least one.")
        # Ensure the number of guests does not exceed the table capacity
        elif self.guests > self.table.capacity:
            raise ValidationError(f("Number of guests ({self.guests}) cannot "
                  "exceed the capacity of the table ({self.table.capacity})."))
        # Validation to ensure a time is specified
        elif self.time is None:
            raise ValidationError("The time field is required.")
        # Validation to ensure the booking date is in the future
        elif self.date <= date.today():
            raise ValidationError("The booking date must be in the future.")

    # Overriding the save method to call the custom clean method before saving
    def save(self, *args, **kwargs):
        self.clean()  # Calling the custom validation method
        super().save(*args, **kwargs)  # Calling the parent save method


# Defining the MenuItem model to represent items on the restaurant's menu
class MenuItem(models.Model):
    # Choices for the category of the menu item
    CATEGORY_CHOICES = [
        ('appetizer', 'Appetizer & Salads'),
        ('main_course', 'Main Course'),
        ('dessert', 'Dessert'),
        ('beverage', 'Beverage'),
    ]
    # Name of the menu item
    name = models.CharField(max_length=100)
    # Description of the menu item
    description = models.TextField()
    # Price of the menu item
    price = models.DecimalField(max_digits=6, decimal_places=2)
    # Optional image for the menu item (uploaded to 'menu_images/' directory)
    image = models.ImageField(upload_to='menu_images/', blank=True, null=True)
    # Category of the menu item (appetizer, main course, dessert, or beverage)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    # Whether the item is available or not
    available = models.BooleanField(default=True)  # Availability of the dish

    # String representation of the MenuItem object
    def __str__(self):
        return self.name
