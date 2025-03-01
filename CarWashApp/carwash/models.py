from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_num = models.CharField(max_length=15)
    place = models.CharField(max_length=100)
    adhaar_number = models.CharField(max_length=12)

    def __str__(self):
        return self.user.username


class Appointment(models.Model):
    SERVICE_TYPES = [
        (1, 'Internal Wash'),
        (2, 'External Wash'),
        (3, 'Comprehensive Wash'),
    ]
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
        ('completed', 'Completed'),
    ]
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    service_type = models.PositiveSmallIntegerField(choices=SERVICE_TYPES)

    def __str__(self):
        return f"{self.customer.username} - {dict(self.SERVICE_TYPES).get(self.service_type)} - {self.status}"


class ShopCollection(models.Model):
    date = models.DateField()
    amount = models.FloatField()

    def __str__(self):
        return f"{self.date} - {self.amount}"


class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class DeliveredService(models.Model):
    appointment = models.OneToOneField(
        'Appointment',
        on_delete=models.CASCADE,
        related_name='delivered_service',
    )  # Link to the Appointment
    delivered_date = models.DateField(default=now)  # When the service was delivered
    delivered_by = models.CharField(max_length=100)  # Employee who delivered the service
    remarks = models.TextField(blank=True, null=True)  # Additional notes/remarks

    def __str__(self):
        return f"Service for Appointment {self.appointment.id} delivered on {self.delivered_date}"
