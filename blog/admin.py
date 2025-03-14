from django.contrib import admin
from .models import Table, Booking


# Register your models here.
@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('number', 'capacity')


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'table', 'date', 'time', 'guests')
    list_filter = ('date', 'time')
    search_fields = ('user__username', 'table__number')

