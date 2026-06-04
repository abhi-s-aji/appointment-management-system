from django.db import models
from django.contrib.auth.models import User

class Departments(models.Model):
    dep_name = models.CharField(max_length=100)
    dep_description = models.TextField()
    def __str__(self): return self.dep_name

class doctor(models.Model):
    doc_name = models.CharField(max_length=100)
    doc_email = models.EmailField()
    doc_phone = models.CharField(max_length=20)
    doc_department = models.ForeignKey(Departments, on_delete=models.CASCADE)
    def __str__(self): return self.doc_name

class Booking(models.Model):
    TIME_SLOT_CHOICES = [
        ('09:00 AM', '09:00 AM - 10:00 AM'), ('10:00 AM', '10:00 AM - 11:00 AM'),
        ('11:00 AM', '11:00 AM - 12:00 PM'), ('02:00 PM', '02:00 PM - 03:00 PM'),
        ('03:00 PM', '03:00 PM - 04:00 PM'),
    ]
    STATUS_CHOICES = [('Pending', 'Pending'), ('Approved', 'Approved'), ('Rescheduled', 'Rescheduled'), ('Rejected_By_Patient', 'Rejected')]
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    patient_name = models.CharField(max_length=100)
    patient_email = models.EmailField()
    patient_phone = models.CharField(max_length=20)
    assigned_doctor = models.ForeignKey(doctor, on_delete=models.CASCADE)
    appointment_date = models.DateField()
    appointment_time = models.CharField(max_length=20, choices=TIME_SLOT_CHOICES, default='09:00 AM')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    booked_on = models.DateField(auto_now=True)
    proposed_date = models.DateField(null=True, blank=True)
    proposed_time = models.CharField(max_length=20, choices=TIME_SLOT_CHOICES, null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    full_name = models.CharField(max_length=100, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=[('M', 'Male'), ('F', 'Female')], blank=True)
    phone = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)
    emergency_contact = models.CharField(max_length=20, blank=True)
    onboarding_completed = models.BooleanField(default=False)