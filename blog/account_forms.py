from django import forms
from django.utils.timezone import now
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['table', 'date', 'time', 'guests']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'min': now().date()}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
            'guests': forms.NumberInput(attrs={'min': 1}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['table'].empty_label = None
        # Set default date as today
        self.fields['date'].initial = now().date()
        self.fields['time'].required = False