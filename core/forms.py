from django import forms
from django.core.exceptions import ValidationError
from .models import Preinscricao
import re

class PreinscricaoForm(forms.ModelForm):
    class Meta:
        model = Preinscricao
        fields = ['nome', 'email', 'whatsapp', 'genero', 'idade', 'ocupacao']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': ''}),
            'email': forms.EmailInput(attrs={'class': 'form-control mb-3', 'placeholder': ''}),
            'whatsapp': forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': ''}),
            'genero': forms.Select(attrs={'class': 'form-control mb-3'}),
            'idade': forms.NumberInput(attrs={'class': 'form-control mb-3', 'placeholder': ''}),
            'ocupacao': forms.Select(attrs={'class': 'form-control mb-3'}),
        }
        labels = {
            'nome': 'Nome completo',
            'email': 'Email',
            'whatsapp': 'Whatsapp',
            'genero': 'Gênero',
            'idade': 'Idade',
            'ocupacao': 'Ocupação',
        }
    
    def clean_nome(self):
        nome = self.cleaned_data.get('nome')
        if not all(x.isalpha() or x.isspace() for x in nome):
            raise ValidationError('O nome deve conter apenas letras e espaços.')
        return nome

    def clean_whatsapp(self):
        whatsapp = self.cleaned_data.get('whatsapp')
        # Remover caracteres não numéricos
        whatsapp = re.sub(r'\D', '', whatsapp)
        if not (10 <= len(whatsapp) <= 11):
            raise ValidationError('O número do Whatsapp deve ter entre 10 e 11 dígitos.')
        return whatsapp
