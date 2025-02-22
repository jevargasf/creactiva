from django import forms
from django.forms import ModelForm
from suscripciones.models import SolicitudOrganizacion, Suscripcion
from suscripciones.utils import get_tipo_organizacion, SelectCustom, get_comunas, get_paises, get_regiones
from suscripciones.services import get_solicitudes, get_planes
from cursos.utils import pedir_nombres_cursos


class CodigoPromocionalForm(forms.Form):
     codigo = forms.CharField(
          label='Ingresa tu código de descuento:',
          max_length=50
     )

class SolicitudOrganizacionForm(ModelForm):
    region = forms.CharField(widget=SelectCustom(
                choices=get_regiones(),
                attrs={
                    'id': 'region'
                }
    ))    
    class Meta:

        def __init__(self, *args, **kwargs):
                    super(SolicitudOrganizacionForm, self).__init__(*args, **kwargs)
                    self.fields['cursos'] = forms.CheckboxSelectMultiple(
                        choices=pedir_nombres_cursos(),
                        attrs={
                            'id': 'cursos_checkbox'
                        }
                    )
                    self.fields['representante'] = SelectCustom(
                        choices=('1','b'),
                        attrs={
                            'id': 'representantes_checkbox'
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
            'pais': 'País',
            'region': 'Región'
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
            'pais': SelectCustom(
                choices=get_paises(),
                attrs={
                    'id': 'pais'
                }
            ),     
            'comuna': SelectCustom(
                choices=get_comunas(),
                attrs={
                    'id': 'comuna'
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


class ElegirOrganizacionForm(forms.Form):
      organizacion = forms.CharField(widget=SelectCustom(
                choices=get_solicitudes(),
                attrs={
                    'id': 'representante'
                }
            ))
# Crear el formulario para elegir la organización. El formulario tiene que mandar al menos
# Datos básicos de la solicitud como nombre de la organización y nombre del usuario que lo subió
# También, crear la url para realizar la solicitud

class SuscripcionOrganizacionForm(ModelForm):
    cursos = forms.CharField(widget=forms.CheckboxSelectMultiple(
                choices=pedir_nombres_cursos(),
                attrs={
                    'id': 'cursos_checkbox'
                }
            ))
    representante = forms.CharField(label='representante', widget=SelectCustom(
          choices=get_solicitudes())
          )
    class Meta:
        model = Suscripcion
        fields = ['fecha_inicio', 'fecha_termino', 'numero_usuarios']
        labels = {
            'fecha_inicio': 'Fecha inicio',
            'fecha_termino': 'Fecha término',
            'numero_usuarios': 'Número usuarios'
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
            'numero_usuarios': forms.NumberInput(
                attrs={
                    'id': 'numero_usuarios'
                }
            )
        }

class SuscripcionIndividualForm(forms.Form):
    planes = forms.CharField(label='plan', widget=forms.RadioSelect(
          choices=get_planes())
          )