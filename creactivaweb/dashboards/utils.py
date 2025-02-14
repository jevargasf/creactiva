from suscripciones.models import *
from main.models import Perfil, User

def suscripcion_activa(user):    
    user_object = User.objects.get(username=user)
    perfil_object = Perfil.objects.get(user_id=user_object.id)
    if perfil_object.codigo[0] == '1':
        registro_object = PerfilSuscripcion.objects.get(perfil_id=perfil_object.id, estado_suscripcion='1')
        if registro_object:
            suscripcion_object = Suscripcion.objects.get(pk=registro_object.suscripcion_id, numero_usuarios=1)
            if suscripcion_object:
                return {'suscripcion':suscripcion_object, 'perfil': perfil_object}
            else:
                return {'perfil': perfil_object}
        else:
            return {'perfil': perfil_object}
    else:
        return {'perfil': perfil_object}