from django.db import models

class Client(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dob = models.DateField()  # Date of Birth
    gender = models.CharField(max_length=10, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')])
    contact_info = models.CharField(max_length=100)
    address = models.TextField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)  # Optional notes about the client
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

class Appointment(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='appointments')
    date = models.DateTimeField()  # Date and time of the appointment
    reason = models.CharField(max_length=255)  # Reason for the appointment
    notes = models.TextField(null=True, blank=True)  # Additional notes

    def __str__(self):
        return f"Appointment with {self.client.full_name} on {self.date.strftime('%Y-%m-%d %H:%M')}"

class Message(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='messages')
    sent_at = models.DateTimeField(auto_now_add=True)
    message_type = models.CharField(max_length=50, choices=[
        ('Birthday', 'Birthday'),
        ('Christmas', 'Christmas'),
        ('New Year', 'New Year'),
        ('Appointment Reminder', 'Appointment Reminder'),
    ])
    content = models.TextField()  # The content of the message sent
    status = models.CharField(max_length=50, choices=[
        ('Pending', 'Pending'),
        ('Sent', 'Sent'),
        ('Failed', 'Failed'),
    ])

    def __str__(self):
        return f"{self.message_type} to {self.client.full_name} on {self.sent_at.strftime('%Y-%m-%d %H:%M')}"
