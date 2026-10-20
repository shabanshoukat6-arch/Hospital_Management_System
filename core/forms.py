
from django import forms
from .models import Patient


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = [
            "full_name",
            "age",
            "gender",
            "phone",
            "email",
            "address",
        ]

        widgets = {
            "full_name": forms.TextInput(attrs={
                "placeholder": "Enter patient's full name"
            }),
            "age": forms.NumberInput(attrs={
                "placeholder": "Enter age",
                "min": 0
            }),
            "phone": forms.TextInput(attrs={
                "placeholder": "Enter phone number"
            }),
            "email": forms.EmailInput(attrs={
                "placeholder": "Enter email address"
            }),
            "address": forms.Textarea(attrs={
                "placeholder": "Enter address",
                "rows": 3
            }),
        }
