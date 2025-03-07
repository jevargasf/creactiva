import json
import ast
from django.forms import Select
from django.utils.timezone import now
from datetime import timedelta

def get_tipo_organizacion():
    f = open("./static/json/organizaciones.json", "r", encoding='utf-8')
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
    f = open("./static/json/cut-comunas.json", "r", encoding='utf-8')
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
    f = open("./static/json/iso-3166-2.json", "r", encoding='utf-8')
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

def get_regiones():
    f = open("./static/json/regiones.json", "r", encoding='utf-8')
    text = f.read()
    f.close()
    lista = json.loads(text)
    choices = [
        ('', 'Seleccione región:')
    ]
    for reg in lista:
        data = ast.literal_eval(reg)
        choices.append((data['codigo'], data['nombre']))
    
    return choices

class SelectCustom(Select):
    def create_option(self, *args, **kwargs):
        option = super().create_option(*args, **kwargs)
        if not option.get('value'):
            option['attrs']['disabled'] = True
        return option

def str_to_list(string: str):
    lista = []
    for a in string:
        if a.isdigit():
            lista.append(a)
        else:
            continue
    return lista

def sumar_fecha(fecha, meses):
    dias = meses*30
    nueva_fecha = fecha + timedelta(days=dias)
    return nueva_fecha

def find_comuna(id_comuna):
    f = open("./static/json/cut-comunas.json")
    text = f.read()
    f.close()
    lista = json.loads(text)

    for cat in lista:
        data = ast.literal_eval(cat)
        if data['codigo'] == id_comuna:
    
            return data['nombre']

def find_tipo_organizacion(id_tipo):
    f = open("./static/json/organizaciones.json", "rb")
    text = f.read()
    f.close()
    lista = json.loads(text)

    for x, cat in enumerate(lista):
        if x == int(id_tipo):
            return cat