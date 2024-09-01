from django import forms
from .models import CustomUser

class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'full_name', 'gender', 'national_code', 'birthday_date', 'ceremony_datetime', 'country']
        widgets = {
            'birthday_date': forms.DateInput(attrs={'type': 'datetime-local'}),
            'ceremony_datetime': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
