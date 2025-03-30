from django.test import TestCase
from blog.account_forms import BookingForm
from blog.models import Table, Booking
from django.contrib.auth.models import User

class TestBookingForm(TestCase):
    def test_form_is_valid(self):
        # Create a user for the booking
        user = User.objects.create_user(username='testuser', password='password123')

        # Create a valid table instance in the test database
        table = Table.objects.create(number=1, capacity=4)  # Use 'number' instead of 'name'

        # Create form data
        form_data = {
            'user': user.id,  # Ensure a user is associated
            'table': table.id,  # Use the created table's ID
            'date': '2026-03-28',  # Valid future date
            'time': '18:30',  # Valid time format
            'guests': 2,  # Ensure guests are between 1 and the table's capacity
        }

        # Create the form with the data
        booking_form = BookingForm(data=form_data)

        print("Form Errors:", booking_form.errors)  # Print errors to debug
        self.assertTrue(booking_form.is_valid(), msg='Form is not valid')  # Ensure form is valid
