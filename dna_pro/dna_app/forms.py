from django import forms
from .models import Agendar

class AgendarForm(forms.ModelForm):
    class Meta:
        model = Agendar
        fields = '__all__'

        widgets = {
            'nome': forms.TextInput(attrs={'class':'form-control'}),
            'sobrenome': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control'}),
            'cidade': forms.TextInput(attrs={'class':'form-control'}),
            'estado': forms.TextInput(attrs={'class':'form-select'}),
            'celular': forms.TextInput(attrs={'class':'form-control'}),
            'observacoes': forms.TextInput(attrs={'class':'form-control'}),
        }
