from suscripciones.models import *

def get_solicitudes():
    data = SolicitudOrganizacion.objects.all()
    organizaciones = []
    for d in data:
        organizaciones.append((d.id, (f'Organización: {d.nombre_organizacion} | Nombre: {d.usuario.first_name} {d.usuario.last_name} | Correo: {d.usuario}')))
    return organizaciones

def get_planes():
    data = Planes.objects.all()
    planes = []
    for p in data:
        planes.append((p.id, p.nombre))
    return planes

# PERO LA TAREA DE REVISAR LAS SUSCRIPCIONES ACTIVAS ES UNA TAREA AUTOMATIZADA Y TIENE COMO RESULTADO LA ACTUALIZACIÓN DEL CÓDIGO PERFIL
# ENTONCES, DEBO ASUMIR QUE SI EL CÓDIGO PERFIL ESTÁ BIEN, ENTONCES TODAS LAS SUSCRIPCIONES SON ACTIVAS
# SI LA PERSONA YA TIENE UNA SUSCRIPCIÓN INDIVIDUAL, ENTONCES NO LE VA A DEJAR ENTRAR A LA PANTALLA DE PAGO
# EN UNA SEGUNDA INSTANCIA, LE DEBERÍA PREGUNTAR SI QUIERE EXTENDER SU SUSCRIPCIÓN, COSA QUE NO HEMOS DISEñADO TODAVÍA

def suscripcion_activa(user):    
    # validar si tiene una suscripción vigente
    try:
        user_object = User.objects.get(username=user)
        perfil_object = Perfil.objects.get(user_id=user_object.id, codigo='100')
        registro_object = PerfilSuscripcion.objects.get(perfil_id=perfil_object.id, estado_suscripcion='1')
        # DBERÍA AGREGAR EN PERFIL/SUSCRIPCIÓN EL CAMPO SUSCRIPCIÓN ACTIVA, ASÍ AGILIZO LA CONSULTA
        # PORQUE SI PIDO TODOS LOS REGISTROS ORDENADOS POR ID, ME VA A TIRAR SIEMPRE TODOS
        if registro_object:
            suscripcion_object = Suscripcion.objects.get(pk=registro_object.suscripcion_id, numero_usuarios=1)
            if suscripcion_object:
                return suscripcion_object
            else:
                return None
        else:
            return None
    except Suscripcion.DoesNotExist as e:
        print(f"Error: {e}; file: {e.__traceback__.tb_frame.f_code.co_filename}; line: {e.__traceback__.tb_lineno}; type: {e.__class__}")
        return None
    except Exception as e:
        print(f"Error: {e}; file: {e.__traceback__.tb_frame.f_code.co_filename}; line: {e.__traceback__.tb_lineno}; type: {e.__class__}")

def suscripcion_session(session_id):
    suscripcion_object = Suscripcion.objects.get(session_id_transbank=session_id)
    if suscripcion_object:
        return suscripcion_object
    else:
        return None
