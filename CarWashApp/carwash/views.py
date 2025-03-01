from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from .models import Customer, Appointment, DeliveredService
from django.contrib import messages
from django.utils.timezone import now
from django.http import HttpResponseForbidden
from .forms import AppointmentForm

def is_admin(user):
    return user.is_staff

def home(request):
    return render(request, 'carwash/home.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials')
    return render(request, 'carwash/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        phone_num = request.POST['phone_num']
        place = request.POST['place']
        adhaar_number = request.POST['adhaar_number']
        user = User.objects.create_user(username=username, password=password)
        Customer.objects.create(user=user, phone_num=phone_num, place=place, adhaar_number=adhaar_number)
        return redirect('login')
    return render(request, 'carwash/register.html')

@login_required
@user_passes_test(is_admin)
def appointments(request):
    if request.user.is_staff:
        appointments = Appointment.objects.all().order_by('-date')
        return render(request, 'carwash/appointments.html', {'appointments': appointments})
    else:
        return redirect('home')

@login_required
def accept_appointment(request, appointment_id):
    if request.user.is_staff:
        appointment = get_object_or_404(Appointment, id=appointment_id)
        appointment.status = 'accepted'
        appointment.save()
        return redirect('appointments')

@login_required
def reject_appointment(request, appointment_id):
    if request.user.is_staff:
        appointment = get_object_or_404(Appointment, id=appointment_id)
        appointment.status = 'rejected'
        appointment.save()
        return redirect('appointments')

@login_required
@user_passes_test(is_admin)  # Only admins
def delivered_services(request):
    delivered_services = DeliveredService.objects.all().order_by('-delivered_date')
    return render(request, 'carwash/admin_delivered_services.html', {'delivered_services': delivered_services})

@login_required
def request_appointment(request):
    # Ensure only non-admin users can request appointments
    if request.user.is_staff:
        return HttpResponseForbidden("Admins cannot request appointments.")
    
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            # Save the appointment, linking it to the logged-in customer
            appointment = form.save(commit=False)
            customer = Customer.objects.get(user=request.user)
            appointment.customer = customer.user  # Assign the User instance
            appointment.status = 'pending'
            appointment.save()
            messages.success(request, "Your appointment has been requested successfully!")
            return redirect('home')
    else:
        form = AppointmentForm()

    return render(request, 'carwash/request_appointment.html', {'form': form})

@login_required
@user_passes_test(is_admin)
def mark_as_delivered(request, appointment_id):
    # Ensure only admins can perform this action
    if not request.user.is_staff:
        return HttpResponseForbidden("You do not have permission to perform this action.")

    appointment = get_object_or_404(Appointment, id=appointment_id)

    if appointment.status != 'accepted':
        messages.error(request, "Only accepted appointments can be marked as delivered.")
        return redirect('appointments')

    # Check if the appointment is already marked as delivered
    if hasattr(appointment, 'delivered_service'):
        messages.error(request, "This appointment has already been delivered.")
        return redirect('appointments')

    # Create a DeliveredService entry
    DeliveredService.objects.create(
        appointment=appointment,
        delivered_by=request.user.username,
        remarks="Service delivered successfully."
    )
    # Update the appointment status
    appointment.status = 'completed'
    appointment.save()

    messages.success(request, f"Appointment {appointment_id} marked as delivered.")
    return redirect('appointments')

@login_required
def customer_past_bookings(request):
    customer = get_object_or_404(Customer, user=request.user)
    # Fetch completed appointments for the logged-in customer
    past_bookings = Appointment.objects.filter(
        customer=request.user
    ).order_by('-date')

    return render(request, 'carwash/customer_past_bookings.html', {'past_bookings': past_bookings})