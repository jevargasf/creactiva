import json
from django.forms import Select

def get_tipo_organizacion():
    f = open("./static/json/tipo-organizacion.json", "r")
    text = f.read()
    f.close()
    lista = json.loads(text)
    choices = [
        ('','Tipo de organización:')
    ]
    for x, cat in enumerate(lista):
        
        choices.append((str(x+1), list(cat.keys())[0]))
    print(choices)
    return choices

class SelectCustom(Select):
    def create_option(self, *args, **kwargs):
        option = super().create_option(*args, **kwargs)
        if not option.get('value'):
            option['attrs']['disabled'] = True
        return option
