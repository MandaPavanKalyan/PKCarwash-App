
from django.contrib import admin
from .models import Appointment, Customer  # Import your models
from .models import DeliveredService

# Customize the display of the Appointment model in the admin panel

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'date', 'time', 'status', 'service_type')
    list_filter = ('status', 'service_type', 'date')
    search_fields = ('customer__user__username', 'customer__phone_num')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        # Only show all appointments for superusers
        if not request.user.is_superuser:
            return qs.none()
        return qs



# Register the Customer model for convenience
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'phone_num', 'place', 'adhaar_number')
    search_fields = ('user__username', 'phone_num')

@admin.register(DeliveredService)
class DeliveredServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'appointment', 'delivered_date', 'delivered_by')
    search_fields = ('appointment__id', 'delivered_by')
    ordering = ('-delivered_date',)