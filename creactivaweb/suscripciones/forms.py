from django import forms
from django.forms import ModelForm
from suscripciones.models import SolicitudOrganizacion, Suscripcion
from suscripciones.utils import get_tipo_organizacion, SelectCustom, get_comunas, get_paises, get_representantes
from cursos.utils import pedir_nombres_cursos


class SolicitudOrganizacionForm(ModelForm):
    class Meta:

        def __init__(self, *args, **kwargs):
                    super(SolicitudOrganizacionForm, self).__init__(*args, **kwargs)
                    self.fields['cursos'] = forms.CheckboxSelectMultiple(
                        choices=pedir_nombres_cursos(),
                        attrs={
                            'id': 'cursos_checkbox'
                        }
                    )
                    self.fields['titular'] = SelectCustom(
                        choices=('1','b'),
                        attrs={
                            'id': 'titulares_checkbox'
                        }
                    )
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

class SuscripcionOrganizacionForm(ModelForm):
    cursos = forms.CharField(widget=forms.CheckboxSelectMultiple(
                choices=pedir_nombres_cursos(),
                attrs={
                    'id': 'cursos_checkbox'
                }
            ))
    titular = forms.CharField(widget=SelectCustom(
                choices=get_representantes(),
                attrs={
                    'id': 'titular'
                }
            ))
    class Meta:
        model = Suscripcion
        fields = ['fecha_inicio', 'fecha_termino', 'monto', 'numero_usuarios']
        labels = {
            'fecha_inicio': 'Fecha inicio',
            'fecha_termino': 'Fecha término',
            'monto': 'Monto',
            'numero_usuarios': 'Número usuarios',
            'cursos': 'Cursos',
            'titular': 'Usuario titular'
        }
        widgets = {
            'fecha_inicio': forms.DateInput(format='%d/%m/%Y',
                attrs={
                    'id': 'fecha_inicio'
                }
            ),
            'fecha_termino': forms.DateInput(format='%d/%m/%Y',
                attrs={
                    'id': 'fecha_termino'
                }
            ),
            'monto': forms.NumberInput(
                attrs={
                    'id': 'monto'
                }
            ),
            'numero_usuarios': forms.NumberInput(
                attrs={
                    'id': 'numero_usuarios'
                }
            )
        }