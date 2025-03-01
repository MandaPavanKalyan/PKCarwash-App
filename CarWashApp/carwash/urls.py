from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('appointments/', views.appointments, name='appointments'),
    path('appointments/<int:appointment_id>/accept/', views.accept_appointment, name='accept_appointment'),
    path('appointments/<int:appointment_id>/reject/', views.reject_appointment, name='reject_appointment'),
    path('services/delivered/', views.delivered_services, name='delivered_services'),
    path('request_appointment/', views.request_appointment, name='request_appointment'),
    path('mark_as_delivered/<int:appointment_id>/', views.mark_as_delivered, name='mark_as_delivered'),
    path('delivered_services/', views.delivered_services, name='delivered_services'),
    path('customer/past_bookings/', views.customer_past_bookings, name='customer_past_bookings'),
]
