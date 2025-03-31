from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages  # Importing messages framework
from django.contrib.auth.decorators import login_required
from .models import Booking, MenuItem  # Importing models
from .account_forms import BookingForm  # Importing the BookingForm
from datetime import date  # Importing date to handle today's date
from django.core.mail import send_mail  # Importing send_mail to send emails

# Create your views here.


# Home view: Render the home page
def home_view(request):
    return render(request, 'blog/index.html')


# Menu view: Display the menu items categorized by their type
def menu_view(request):
    # Fetch menu items categorized by their category
    menu_items = {
        'appetizer': MenuItem.objects.filter(category='appetizer'),
        'main_course': MenuItem.objects.filter(category='main_course'),
        'dessert': MenuItem.objects.filter(category='dessert'),
        'beverage': MenuItem.objects.filter(category='beverage'),
    }
    return render(request, 'blog/menu.html', {'menu_items': menu_items})


# Booking view: Handle booking creation
@login_required  # Ensure that the user is logged in to make a booking
def booking_view(request):
    if request.method == 'POST':  # If the form is submitted via POST
        form = BookingForm(request.POST)
        if form.is_valid():  # If the form is valid
            booking = form.save(commit=False)  # Save the form data
            booking.user = request.user  # Assign the current logged-in user
            booking.status = 'waiting'  # Set the status of the booking
            booking.save()  # Save the booking to the database
            # Send a confirmation email to the user
            send_mail(
                "Booking Request Received - Laclook Restaurant",
                "Thanks for booking at Laclook Restaurant. "
                "We will send you an email and reply whether "
                "or not your reservation is confirmed.",  # Email body
                'laclookrestaurant@gmail.com',  # From address
                [booking.user.email],  # Send email to the authenticated user
                fail_silently=False,  # Raise errors if the email fails to send
            )
            return redirect('booking_list')  # Redirect to the list of bookings
    else:  # If the request method is GET, create a blank booking form
        form = BookingForm()
    return render(request, 'blog/booking.html', {'form': form})


# Booking list view: Display the list of bookings for the authenticated user
@login_required  # Ensure that the user is logged in to see their bookings
def booking_list_view(request):
    today = date.today()  # Get today's date to compare with booking dates
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'blog/booking_list.html',
                  {'bookings': bookings, 'today': today})


# Cancel booking view: Allow users to cancel their booking
@login_required  # Ensure that the user is logged in to cancel a booking
def cancel_booking_view(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)  # Retrieve the booking
    if booking.user != request.user:  # Check the booking
        messages.error(request,
                       "You do not have permission to cancel this booking.")
        return redirect('booking_list')  # Redirect to the booking list
    booking.delete()  # Delete the booking from the database
    return redirect('booking_list')  # Redirect to the booking list page


# Edit booking view: Allow users to edit their booking details
@login_required  # Ensure that the user is logged in to edit a booking
def edit_booking_view(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    if request.method == 'POST':  # If the form is submitted via POST
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():  # If the form is valid
            booking.status = 'waiting'  # Set the status to 'waiting'
            form.save()  # Save the edited booking to the database
            return redirect('booking_list')  # Redirect to the booking list
    else:  # If the request method is GET, show the current booking data
        form = BookingForm(instance=booking)
    return render(request, 'blog/edit_booking.html',
                  {'form': form, 'booking': booking})  # Render the edit form
