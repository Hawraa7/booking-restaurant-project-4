from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Booking, MenuItem

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['table', 'date', 'time', 'guests']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'})
        }


class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ['name', 'description', 'price']
        widgets = {
            'description': SummernoteWidget(),
        }