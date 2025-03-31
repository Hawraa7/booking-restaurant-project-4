from django import forms  # Importing Django's forms module
from django.utils.timezone import now  # Importing 'now' function
from .models import Booking  # Importing the Booking model


# Defining the BookingForm class, inheriting from Django's ModelForm
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking  # Linking the form to the Booking model
        fields = ['table', 'date', 'time', 'guests']  # Specifying the fields
        widgets = {
            # Customizing the input widget for the 'date' field
            'date': forms.DateInput(attrs={'type': 'date',
                                    'min': now().date()}),
            # Customizing the input widget for the 'time' field
            'time': forms.TimeInput(attrs={'type': 'time'}),
            # Customizing the input widget for the 'guests' field
            'guests': forms.NumberInput(attrs={'min': 1}),
        }

    # Customizing the initialization method for the form
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # Calling the parent __init__ method

        # Setting the empty_label for the 'table' field to None
        self.fields['table'].empty_label = None

        # Setting the default value for the 'date' field to today's date
        self.fields['date'].initial = now().date()

        # Making the 'time' field optional (not required)
        self.fields['time'].required = False
