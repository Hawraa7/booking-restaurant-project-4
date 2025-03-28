from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .models import MenuItem, Table, Booking
from datetime import date, time

class TestMenuViews(TestCase):

    def setUp(self):
        # Creating a superuser for accessing the menu
        self.user = User.objects.create_superuser(
            username="myUsername",
            password="myPassword",
            email="test@test.com"
        )

        # Creating a sample MenuItem with correct price format (Decimal)
        self.menu_item = MenuItem.objects.create(
            name="apple juice", 
            description="refreshing juice",
            price=13.00,  # Correctly using decimal value
            category="appetizer", 
            available=True
        )

        # Create a table for booking purposes
        self.table = Table.objects.create(number=1, capacity=4)

    def test_render_menu_page(self):
        # Login the superuser for accessing the menu page
        self.client.login(username="myUsername", password="myPassword")
        
        # Request the menu page (no arguments needed here)
        response = self.client.get(reverse('menu'))

        # Check if the response status is 200 OK
        self.assertEqual(response.status_code, 200)
        
        # Check if the menu items are in the response content
        self.assertIn(b"apple juice", response.content)  # Check the name of the MenuItem
        self.assertIn(b"refreshing juice", response.content)  # Check the description
        self.assertIn(b"13.00", response.content)  # Check the price

    def test_successful_booking_submission(self):
        """Test for posting a booking"""
        # Ensure user is logged in
        self.client.login(username="myUsername", password="myPassword")

        # Prepare booking data with valid future date
        booking_data = {
            'table': self.table.id,  # Reference the table by its ID
            'date': '2026-03-28',  # Valid future date
            'time': '18:30',  # Valid time format
            'guests': 2
        }

        # Make POST request to booking page
        response = self.client.post(reverse('booking'), booking_data)

        # Follow the redirect to the final destination (e.g., booking list page)
        self.assertRedirects(response, reverse('booking_list'))

        # Now test if booking was successfully created and user is redirected to booking list
        booking = Booking.objects.first()  # Fetch the first booking

        # Assert that booking data is saved correctly
        self.assertEqual(booking.table.id, self.table.id)
        self.assertEqual(booking.date, date(2026, 3, 28))
        self.assertEqual(booking.time, time(18, 30))  
        self.assertEqual(booking.guests, 2)
        self.assertEqual(booking.status, 'waiting')
