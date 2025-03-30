from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Booking, MenuItem
from .account_forms import BookingForm
from datetime import date
from django.core.mail import send_mail

# Create your views here.

def home_view(request):
    return render(request, 'blog/index.html')

def menu_view(request):
    # Fetch menu items categorized by their category
    menu_items = {
        'appetizer': MenuItem.objects.filter(category='appetizer'),
        'main_course': MenuItem.objects.filter(category='main_course'),
        'dessert': MenuItem.objects.filter(category='dessert'),
        'beverage': MenuItem.objects.filter(category='beverage'),
    }
    return render(request, 'blog/menu.html', {'menu_items': menu_items})

@login_required
def booking_view(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.status = 'waiting'
            booking.save()
            # Send confirmation email
            send_mail(
                "Booking Request Received - Laclook Restaurant",
                "Thanks for booking at Laclook Restaurant. We will send you an email and reply whether or not your reservation is confirmed.",
                'laclookrestaurant@gmail.com',
                [booking.user.email],  # Retrieve email from authenticated user
                fail_silently=False,
            )
            return redirect('booking_list')
    else:
        form = BookingForm()
    return render(request, 'blog/booking.html', {'form': form})

@login_required
def booking_list_view(request):
    today = date.today()
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'blog/booking_list.html', {'bookings': bookings, 'today': today})

@login_required
def cancel_booking_view(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if booking.user != request.user:
        messages.error(request, "You do not have permission to cancel this booking.")
        return redirect('booking_list')
    booking.delete()
    return redirect('booking_list')

@login_required
def edit_booking_view(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            booking.status = 'waiting'
            form.save()
            return redirect('booking_list')
    else:
        form = BookingForm(instance=booking)
    return render(request, 'blog/edit_booking.html', {'form': form, 'booking': booking})
