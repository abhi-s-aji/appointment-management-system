from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('booking/', views.booking, name='booking'),
    path('doctors/', views.doctors, name='doctors'),
    path('contact/', views.contact, name='contact'),
    path('department/', views.department, name='department'),
    path('departments/', views.department, name='departments_plural'),

    # Custom Auth
    path('auth/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('auth/logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),

    
    path("accounts/", include("allauth.urls")),

    path('login-redirect/', views.login_redirect, name='login_redirect'),
    path('profile-setup/', views.profile_setup, name='profile_setup'),

    path('profile/settings/', views.user_profile_settings, name='user_profile_settings'),

    path('track-progress/', views.track_progress, name='track_progress'),
    path('track/<int:booking_id>/', views.track_progress, name='view_individual_booking'),
    path('track/<int:booking_id>/accept/', views.patient_accept_reschedule, name='accept_reschedule'),
    path('track/<int:booking_id>/reject/', views.patient_reject_reschedule, name='reject_reschedule'),
    path('track/<int:booking_id>/ticket/', views.download_ticket, name='download_ticket'),
]