from django import forms
from .models import Client, Appointment, Message

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['first_name', 'last_name', 'dob', 'gender', 'contact_info', 'address', 'notes']

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = [
            'client',
            'date',
            'reason',
            'notes'
        ]
        widgets = {
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'notes': forms.Textarea(attrs={'rows': 3}),
        }
        
class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = [
            'client',
            'message_type',
            'content'
        ]
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3}),
        }
