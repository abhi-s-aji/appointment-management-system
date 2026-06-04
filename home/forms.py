from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['patient_name', 'patient_email', 'patient_phone', 'assigned_doctor', 'appointment_date', 'appointment_time']
        
        widgets = {
            'patient_name': forms.TextInput(attrs={
                'placeholder': 'Patient name'
            }),
            'patient_email': forms.EmailInput(attrs={
                'placeholder': 'Patient email'
            }),
            'patient_phone': forms.TextInput(attrs={
                'placeholder': 'Patient phone'
            }),
            'assigned_doctor': forms.Select(),
            'appointment_time': forms.Select(),
            
            
            'appointment_date': forms.TextInput(attrs={
                'class': 'datepicker',
                'placeholder': 'Select appointment date...',
                'autocomplete': 'off'
            }),
        }