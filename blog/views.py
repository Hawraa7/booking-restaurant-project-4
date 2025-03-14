from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Booking, MenuItem
from .forms import BookingForm

# Create your views here.

def menu_view(request):
    menu_items = MenuItem.objects.all()
    return render(request, 'menu.html', {'menu_items': menu_items})

@login_required
def booking_view(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            return redirect('booking_list')
    else:
        form = BookingForm()
    return render(request, 'booking.html', {'form': form})

@login_required
def booking_list_view(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'blog/booking_list.html', {'bookings': bookings})
