import json
import ast
from django.forms import Select

def get_tipo_organizacion():
    f = open("./static/json/organizaciones.json", "r")
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
