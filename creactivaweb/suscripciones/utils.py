import json

def get_tipo_organizacion():
    f = open("./static/json/tipo-organizacion.json", "r")
    text = f.read()
    f.close()
    lista = json.loads(text)
    choices = []
    for x, cat in enumerate(lista):
        
        #choices.append((x, cat.keys()))
        choices.append((str(x+1), list(cat.keys())[0]))
    return choices

