from django import forms
from django.forms import ModelForm
from suscripciones.models import SolicitudOrganizacion
from suscripciones.utils import get_tipo_organizacion, SelectCustom, get_comunas, get_paises
from cursos.utils import pedir_nombres_cursos


class SolicitudOrganizacionForm(ModelForm):
    class Meta:
        model = SolicitudOrganizacion
        fields = ['nombre_organizacion', 'tipo_organizacion', 'pais', 'comuna', 'cursos', 'mensaje']
        labels = {
            'nombre_organizacion': 'Nombre organización',
            'mensaje': 'Mensaje',
            'cursos': 'Selecciona el contenido que te interesa',
            'tipo_organizacion': 'Tipo de organización',
            'comuna': 'Comuna',
            'pais': 'País'
        }
        widgets = {
            'nombre_organizacion': forms.TextInput(
                attrs={
                    'placeholder': 'Nombre organización',
                    'id': 'nombre_organizacion'
                }
            ),
            'tipo_organizacion': SelectCustom(
                choices=get_tipo_organizacion(),
                attrs={
                    'placeholder': 'Selecciona el tipo de organización',
                    'id': 'tipo_organizacion'
                }
            ),
            'comuna': SelectCustom(
                choices=get_comunas(),
                attrs={
                    'id': 'comuna'
                }
            ),    
            'pais': SelectCustom(
                choices=get_paises(),
                attrs={
                    'id': 'pais'
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
                    'rows': 6
                }
            )
        }