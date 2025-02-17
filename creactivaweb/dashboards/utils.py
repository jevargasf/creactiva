from suscripciones.models import *
from main.models import Perfil, User

def suscripcion_activa(user):
    try:    
        user_object = User.objects.get(username=user)
        perfil_object = Perfil.objects.get(user_id=user_object.id)
        if perfil_object.codigo[0] == '1':
            with PerfilSuscripcion.objects.get(perfil_id=perfil_object.id, estado_suscripcion='1') as registro_object: 
                if registro_object:
                    suscripcion_object = Suscripcion.objects.get(pk=registro_object.suscripcion_id, numero_usuarios=1)
                    if suscripcion_object:
                        return {
                            'suscripcion':suscripcion_object, 
                            'dias_restantes': (suscripcion_object.fecha_termino - now()).days, 
                            'perfil': perfil_object
                            }
                    else:
                        return {'perfil': perfil_object}
                else:
                    return {'perfil': perfil_object}
        else:
            return {'perfil': perfil_object}
    except Exception as e:
        print(f"Error: {e}; file: {e.__traceback__.tb_frame.f_code.co_filename}; line: {e.__traceback__.tb_lineno}; type: {e.__class__}")
        return {'perfil': perfil_object}
