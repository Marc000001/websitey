from django import forms
from .models import Patient, Note

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['name', 'description', 'number','level', 'time', 'ward', 'symptoms', 'Admitted', 'None_Admitted']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'number': forms.TextInput(attrs={'class': 'form-control'}),
            'symptoms': forms.TextInput(attrs={'class': 'form-control'}),
            'time': forms.TextInput(attrs={'class': 'form-control'}),
            'level': forms.TextInput(attrs={'class':'form-control'}),
            'ward': forms.TextInput(attrs={'class': 'form-control'}),
        }
        is_Admitted = forms.BooleanField(required=False),
        is_None_Admitted = forms.BooleanField(required=False),


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['note']
        widgets = {
            'note': forms.TextInput(attrs={'class': 'form-control'}),
        }

