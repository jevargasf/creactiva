from django import forms
from django.forms import ModelForm
from main.models import Contacto

class SolicitarResetPasswordForm(forms.Form):
    email = forms.EmailField(
        required=True,
        widget=forms.TextInput()
        )

class ResetPasswordForm(forms.Form):
    password1 = forms.CharField(
        widget = forms.PasswordInput(
            attrs={
                'id': 'password1',
                'placeholder': 'Ingrese su nueva contraseña'
            }
        )
    )

    password2 = forms.CharField(
        widget = forms.PasswordInput(
            attrs={
                'id': 'password2',
                'placeholder': 'Confirme contraseña'
            }
        )
    )
class ContactoModelForm(ModelForm):
    class Meta:
        model = Contacto
        fields = ['nombre', 'apellido', 'email', 'mensaje']
        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'email': 'Correo',
            'mensaje': 'Mensaje'
        }
        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'placeholder': 'Nombre',
                    'id': 'nombre'
                }
            ),
            'apellido': forms.TextInput(
                attrs={
                    'placeholder': 'Apellido',
                    'id': 'apellido'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'sucorreo@sudominio.com',
                    'id': 'email'
                }
            ),
            'mensaje': forms.Textarea(
                attrs={
                    'placeholder': 'Cuéntanos más',
                    'id': 'mensaje',
                    'rows': 4
                }
            )
        }