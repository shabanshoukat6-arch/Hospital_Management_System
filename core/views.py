from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import PatientForm
from .models import Patient, Doctor, Appointment
from .forms import PatientForm


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Step 1: Credentials verify karo
        user = authenticate(
            request,
            username=username,
            password=password
        )

        # Step 2: Check karo user valid hai ya nahi
        if user is not None:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect("dashboard")

        else:
            messages.error(request, "Invalid username or password")

    return render(request, "core/login.html")





@login_required
def dashboard(request):
    context = {
        "total_patients": Patient.objects.count(),
        "total_doctors": Doctor.objects.count(),
        "total_appointments": Appointment.objects.count(),
        "scheduled_appointments": Appointment.objects.filter(
            status="Scheduled"
        ).count(),
        "recent_appointments": Appointment.objects.select_related(
            "patient", "doctor"
        ).order_by("-appointment_date")[:5],
    }

    return render(request, "core/dashboard.html", context)



@login_required
def logout_view(request):
    if request.method == "POST":
        logout(request)
        messages.success(request, "You have logged out successfully.")
        return redirect("login")

    return redirect("dashboard")


@login_required
def patient_list(request):
    patients = Patient.objects.order_by("-created_at")
    return render(request, "core/patient_list.html", {
        "patients": patients
    })


@login_required
def patient_add(request):
    if request.method == "POST":
        form = PatientForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Patient added successfully!")
            return redirect("patient_list")
    else:
        form = PatientForm()

    return render(request, "core/patient_form.html", {
        "form": form,
        "page_title": "Add Patient"
    })


@login_required
def patient_edit(request, pk):
    patient = get_object_or_404(Patient, pk=pk)

    if request.method == "POST":
        form = PatientForm(request.POST, instance=patient)

        if form.is_valid():
            form.save()
            messages.success(request, "Patient updated successfully!")
            return redirect("patient_list")
    else:
        form = PatientForm(instance=patient)

    return render(request, "core/patient_form.html", {
        "form": form,
        "page_title": "Edit Patient"
    })


@login_required
def patient_delete(request, pk):
    patient = get_object_or_404(Patient, pk=pk)

    if request.method == "POST":
        patient.delete()
        messages.success(request, "Patient deleted successfully!")
        return redirect("patient_list")

    return render(request, "core/patient_confirm_delete.html", {
        "patient": patient
    })
