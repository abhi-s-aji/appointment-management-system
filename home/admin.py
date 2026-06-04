from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Departments, doctor, Booking

@admin.action(description=' Accept and Approve selected requests')
def approve_appointments(modeladmin, request, queryset):
    queryset.update(status='Approved', proposed_date=None, proposed_time=None)

class BookingAdmin(admin.ModelAdmin):
    list_display = ('patient_name', 'assigned_doctor', 'appointment_date', 'appointment_time', 'status_badge', 'booked_on')
    list_filter = ('status', 'assigned_doctor', 'appointment_date')
    search_fields = ('patient_name', 'patient_email')
    actions = [approve_appointments]

    def save_model(self, request, obj, form, change):
        if obj.proposed_date or obj.proposed_time:
            if obj.status != 'Rejected_By_Patient':
                obj.status = 'Rescheduled'
        super().save_model(request, obj, form, change)

    def status_badge(self, obj):
        if obj.status == 'Approved':
            return mark_safe('<span style="background-color: #d1e7dd; color: #0f5132; padding: 5px 10px; border-radius: 12px; font-weight: bold;">Approved</span>')
        elif obj.status == 'Rescheduled':
            return mark_safe('<span style="background-color: #cff4fc; color: #055160; padding: 5px 10px; border-radius: 12px; font-weight: bold;">Proposed Reschedule</span>')
        elif obj.status == 'Rejected_By_Patient':
            return mark_safe('<span style="background-color: #f8d7da; color: #842029; padding: 5px 10px; border-radius: 12px; font-weight: bold;">Patient Rejected</span>')
        return mark_safe('<span style="background-color: #fff3cd; color: #664d03; padding: 5px 10px; border-radius: 12px; font-weight: bold;">Pending</span>')
    
    status_badge.short_description = 'Current Status'

admin.site.register(Departments)
admin.site.register(doctor)
admin.site.register(Booking, BookingAdmin)







from .models import ContactMessage

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'submitted_at')
    list_filter = ('submitted_at',)
    search_fields = ('name', 'email', 'message')
    readonly_fields = ('name', 'email', 'message', 'submitted_at') # Prevents editing messages directly

admin.site.register(ContactMessage, ContactMessageAdmin)