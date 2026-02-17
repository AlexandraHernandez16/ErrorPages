from django import forms
from django.core.exceptions import ValidationError
import re

class ContactoForm(forms.Form):

    nombre = forms.CharField(
        min_length=10,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Tu nombre',
            'pattern': r'[A-Za-z ]+',
            'title': 'Solo letras y espacios. Mínimo 10 caracteres'
        })
    )

    matricula = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Tu matrícula',
            'pattern': r'\d{5}[A-Za-z]{2}\d{3}',
            'title': 'Formato: 5 dígitos, 2 letras, 3 dígitos'
        })
    )

    correo = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'correo@utez.edu.mx',
            'pattern': r'^[a-zA-Z0-9]+@utez\.edu\.mx$',
            'title': 'Formato: correo válido con finalización utez.edu.mx'
        })
    )

    telefono = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Tu teléfono',
            'pattern': r'^\d{10}$',
            'title': 'Formato: 10 dígitos numéricos'
        })
    )

    rfc = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Tu RFC',
            'pattern': r'[A-Z]{4}\d{6}[A-Z0-9]{3}',
            'title': 'Formato: 4 letras, 6 números, 3 alfanuméricos'
        })
    )

    contraseña = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Tu contraseña',
            'pattern': r'(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}',
            'title': 'Mínimo 8 caracteres, una mayúscula, una minúscula, un número y un símbolo especial (@$!%*?&)'
        })
    )


    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']

        if not re.fullmatch(r'[A-Za-z ]+', nombre):
            raise ValidationError("El nombre solo debe contener letras y espacios.")
        return nombre

    def clean_matricula(self):
        matricula = self.cleaned_data['matricula']

        if not re.fullmatch(r'\d{5}[A-Za-z]{2}\d{3}', matricula):
            raise ValidationError("Formato inválido de matrícula.")

        return matricula

    def clean_correo(self):
        correo = self.cleaned_data['correo']

        if not re.fullmatch(r'[a-zA-Z0-9]+@utez\.edu\.mx', correo):
            raise ValidationError("El correo debe terminar en @utez.edu.mx")

        return correo

    def clean_telefono(self):
        telefono = self.cleaned_data['telefono']

        if not re.fullmatch(r'\d{10}', telefono):
            raise ValidationError("El teléfono debe contener exactamente 10 dígitos.")

        return telefono

    def clean_rfc(self):
        rfc = self.cleaned_data['rfc']

        if not re.fullmatch(r'[A-Z]{4}\d{6}[A-Z0-9]{3}', rfc):
            raise ValidationError("Formato de RFC inválido.")

        return rfc

    def clean_contraseña(self):
        contraseña = self.cleaned_data['contraseña']

        patron = r'(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}'

        if not re.fullmatch(patron, contraseña):
            raise ValidationError(
                "La contraseña debe tener mínimo 8 caracteres, una mayúscula, "
                "una minúscula, un número y un símbolo especial."
            )

        return contraseña
