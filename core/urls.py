from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("logout/", views.logout_view, name="logout"),
    path("patients/", views.patient_list, name="patient_list"),
    path("patients/add/", views.patient_add, name="patient_add"),
    path("patients/<int:pk>/edit/", views.patient_edit, name="patient_edit"),
    path("patients/<int:pk>/delete/", views.patient_delete, name="patient_delete"),

]