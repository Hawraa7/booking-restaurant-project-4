from django.contrib import admin
from .models import Table, Booking, MenuItem
from django_summernote.admin import SummernoteModelAdmin
from django.core.mail import send_mail


# Registering the MenuItem model in the admin interface using Summernote
@admin.register(MenuItem)
class MenuItemAdmin(SummernoteModelAdmin):
    # Configuring which fields should use the Summernote editor
    summernote_fields = ('description',)


# Registering the Table model in the admin interface
@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    # Configuring the admin interface to display 'number' and 'capacity' fields
    list_display = ('number', 'capacity')


# Registering the Booking model in the admin interface
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    # Configuring the admin interface to display specific fields
    list_display = ('user', 'table', 'date', 'time', 'guests', 'status')
    # Adding filters for 'date' and 'time' fields to narrow down the bookings
    list_filter = ('date', 'time')

    # Custom method to handle email sending when a booking is updated
    def save_model(self, request, obj, form, change):
        # If the booking is updated and its status is 'rejected', send an email
        if change and obj.status == "rejected":
            # If a rejection reason is provided use it, otherwise use a message
            if obj.rejection_reason:
                rejection_message = obj.rejection_reason
            else:
                rejection_message = ("Unfortunately, "
                                     "your reservation at Laclook Restaurant"
                                     "has been rejected due to a scheduling "
                                     "conflict. We apologize for the "
                                     "inconvenience.")

            email_subject = "Booking Rejection - Laclook Restaurant"
            # Sending the rejection email to the user who made the booking
            send_mail(
                email_subject,
                rejection_message,
                'laclookrestaurant@gmail.com',  # Email from the restaurant
                [obj.user.email],  # Sending the email to the user
                fail_silently=False,  # Ensuring errors are not silenced
            )

        # If the booking is updated and its status is 'confirmed',
        # send a confirmation email to the user
        elif change and obj.status == "confirmed":
            email_subject = "Booking Confirmed - Laclook Restaurant"
            email_message = ("Your reservation at Laclook Restaurant has been "
                             "confirmed. We look forward to seeing you!")
            # Sending the confirmation email to the user
            send_mail(
                email_subject,
                email_message,
                'laclookrestaurant@gmail.com',  # Email from the restaurant
                [obj.user.email],  # Sending the email to the user
                fail_silently=False,  # Ensuring errors are not silenced
            )

        # Calling the parent method to save the booking object
        super().save_model(request, obj, form, change)
