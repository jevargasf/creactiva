from django.contrib.auth.models import User
from main.models import Perfil
from jwt import JWT
from jwt.jwk import OctetJWK
from django.utils import timezone
from creactivaweb.settings import JWT_SECURE

def crear_usuario(username: str, first_name: str, last_name: str, email: str, password: str):
    user = User.objects.create_user(
        username=username,
        email=email,
        password=password,
        first_name=first_name,
        last_name=last_name,
        is_active=False
    )
    user.save()
    perfil = Perfil.objects.create(
        codigo='000',
        user=user
    )
    perfil.save()
    return True

def get_representantes():
    data = Perfil.objects.filter(codigo='010')
    if len(data) != 0:
        lista_rep = [['0', 'Seleccione al representante de la organización']]
        for rep in data:
            lista_rep.append([str(rep.id), f'{rep.user} | {rep.user.first_name} {rep.user.last_name}'])
        return lista_rep
    else:
        return None
    
def crear_token(**kwargs):
    jwt = JWT()
    jwk = OctetJWK(key=JWT_SECURE.encode('utf-8'))
    
    ts = str(timezone.now())
    payload = {
        'ts': ts
    }

    for key, arg in kwargs.items():
        payload[key] = arg
        
    token = jwt.encode(payload, jwk, alg='HS256')
    return token

def traducir_token(token):
    jwt = JWT()
    jwk = OctetJWK(key=JWT_SECURE.encode('utf-8'))

    mensaje = jwt.decode(token, jwk, do_time_check=True)
    return mensaje
