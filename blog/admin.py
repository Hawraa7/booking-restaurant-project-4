from django.contrib import admin
from .models import Table, Booking, MenuItem
from django_summernote.admin import SummernoteModelAdmin
from django.core.mail import send_mail


@admin.register(MenuItem)
class MenuItemAdmin(SummernoteModelAdmin):
    summernote_fields = ('description',) 


# Register your models here.
@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('number', 'capacity')


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'table', 'date', 'time', 'guests', 'status')
    list_filter = ('date', 'time')
    def save_model(self, request, obj, form, change):
        if change and obj.status == "rejected":  # Only send email if booking is rejected
            rejection_message = obj.rejection_reason if obj.rejection_reason else "Unfortunately, your reservation at Laclook Restaurant has been rejected due to a scheduling conflict. We apologize for the inconvenience."

            email_subject = "Booking Rejection - Laclook Restaurant"
            send_mail(
                email_subject,
                rejection_message,
                'laclookrestaurant@gmail.com',
                [obj.user.email],  # Send email to the logged-in user
                fail_silently=False,
            )

        elif change and obj.status == "confirmed":  # Send confirmation email
            email_subject = "Booking Confirmed - Laclook Restaurant"
            email_message = "Your reservation at Laclook Restaurant has been confirmed. We look forward to seeing you!"
            
            send_mail(
                email_subject,
                email_message,
                'laclookrestaurant@gmail.com',
                [obj.user.email],
                fail_silently=False,
            )

        super().save_model(request, obj, form, change)

