import json
import ast
from django.forms import Select
from main.models import Perfil

def get_tipo_organizacion():
    f = open("./static/json/organizaciones.json", "rb")
    text = f.read()
    f.close()
    lista = json.loads(text)
    choices = [
        ('','Tipo de organización:')
    ]
    for x, cat in enumerate(lista):
        
        choices.append((str(x+1), cat))
    return choices

def get_comunas():
    f = open("./static/json/cut-comunas.json")
    text = f.read()
    f.close()
    lista = json.loads(text)
    choices = [
        ('','Seleccione comuna:')
    ]
    for cat in lista:
        data = ast.literal_eval(cat)
        choices.append((data['codigo'], data['nombre']))
    
    return choices

def get_paises():
    f = open("./static/json/iso-3166-2.json")
    text = f.read()
    f.close()
    lista = json.loads(text)
    choices = [
        ('', 'Seleccione país:')
    ]
    for cat in lista:
        data = ast.literal_eval(cat)
        choices.append((data['alfa-2'], data['nombre']))
    
    return choices
class SelectCustom(Select):
    def create_option(self, *args, **kwargs):
        option = super().create_option(*args, **kwargs)
        if not option.get('value'):
            option['attrs']['disabled'] = True
        return option

def get_representantes():
    data = Perfil.objects.filter(codigo='010')
    if len(data) != 0:
        for rep in data:
            # Enviar esta data al formulario para que el administrador pueda elegir el representante
            # Tal vez, se debería registrar el nombre de la organización en Perfil, sería útil
            print(rep.user, rep.user.first_name, rep.user.last_name)
    else:
        return None