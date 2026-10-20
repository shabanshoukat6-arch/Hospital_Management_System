
from django.contrib import admin
from .models import Patient, Doctor, Appointment


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ("full_name", "age", "gender", "phone")
    search_fields = ("full_name", "phone")


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ("full_name", "specialization", "phone", "available")
    search_fields = ("full_name", "specialization")
    list_filter = ("available", "specialization")


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("patient", "doctor", "appointment_date", "status")
    list_filter = ("status", "appointment_date")
    search_fields = ("patient__full_name", "doctor__full_name")
