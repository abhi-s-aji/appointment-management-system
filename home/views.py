from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from .forms import BookingForm
from .models import Departments, doctor, Booking, ContactMessage, UserProfile
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.contrib import messages

# --- Public Pages ---
def index(request): 
    return render(request, 'index.html')

def about(request): 
    return render(request, 'about.html')

def doctors(request): 
    return render(request, 'doctors.html', {'doctors_list': doctor.objects.all()})

def department(request): 
    return render(request, 'department.html', {'dept': Departments.objects.all()})

def contact(request):
    if request.method == "POST":
        ContactMessage.objects.create(
            name=request.POST.get('name'), 
            email=request.POST.get('email'), 
            message=request.POST.get('message')
        )
        messages.success(request, "Message sent successfully!")
        return redirect('contact')
    return render(request, 'contact.html')

# --- Authentication & Onboarding Flow ---
@login_required
def login_redirect(request):
    if not hasattr(request.user, 'profile') or not request.user.profile.onboarding_completed:
        return redirect('profile_setup')
    return redirect('track_progress')

@login_required
def profile_setup(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        profile.full_name = request.POST.get('full_name')
        profile.age = request.POST.get('age')
        profile.gender = request.POST.get('gender')
        profile.phone = request.POST.get('phone')
        profile.address = request.POST.get('address')
        profile.emergency_contact = request.POST.get('emergency_contact')
        profile.onboarding_completed = True
        profile.save()
        messages.success(request, "Profile setup complete!")
        return redirect('track_progress')
    return render(request, 'onboarding.html')

# --- Booking & Dashboard ---
def booking(request):
    form = BookingForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        if request.user.is_authenticated: 
            obj.user = request.user
        obj.save()
        messages.success(request, "Booking requested successfully!")
        return redirect('track_progress')
    return render(request, 'booking.html', {'form': form})

@login_required
@never_cache
def track_progress(request): 
    return render(request, 'track_progress.html', {
        'bookings': Booking.objects.filter(user=request.user).order_by('-id')
    })

@login_required
def patient_accept_reschedule(request, booking_id):
    b = get_object_or_404(Booking, id=booking_id, user=request.user)
    b.status = 'Approved'
    b.save()
    return redirect('track_progress')

@login_required
def patient_reject_reschedule(request, booking_id):
    b = get_object_or_404(Booking, id=booking_id, user=request.user)
    b.status = 'Rejected_By_Patient'
    b.save()
    return redirect('track_progress')

@login_required
@never_cache
def user_profile_settings(request):
    if request.method == 'POST':
        request.user.first_name = request.POST.get('first_name', '')
        request.user.last_name = request.POST.get('last_name', '')
        request.user.save()
        messages.success(request, "Settings updated successfully.")
        return redirect('track_progress')
    return render(request, 'profile_settings.html', {'user': request.user})

@login_required
def download_ticket(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    html_string = render_to_string('ticket_template.html', {'booking': booking})
    return HttpResponse(html_string)