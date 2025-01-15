from django import forms
from django.forms import ModelForm
from suscripciones.models import SolicitudOrganizacion
from suscripciones.utils import get_tipo_organizacion
from cursos.utils import pedir_nombres_cursos
class SolicitudOrganizacionForm(ModelForm):
    class Meta:
        model = SolicitudOrganizacion
        fields = ['nombre', 'apellido', 'tipo_organizacion', 'cursos', 'mensaje']
        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'mensaje': 'Mensaje',
            'cursos': 'Selecciona el contenido que te interesa',
            'tipo_organizacion': 'Tipo de organización'
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
            'tipo_organizacion': forms.Select(
                choices=get_tipo_organizacion(),
                attrs={
                    'placeholder': 'Selecciona el tipo de organización',
                    'id': 'tipo_organizacion'
                }
            ),
            'cursos': forms.CheckboxSelectMultiple(
                choices=pedir_nombres_cursos(),
                attrs={
                    'id': 'cursos_checkbox'
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