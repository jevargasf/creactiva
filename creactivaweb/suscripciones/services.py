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

def suscripcion_activa(user):    
    try:
        user_object = User.objects.get(username=user)
        perfil_object = Perfil.objects.get(user_id=user_object.id, codigo='100')
        registro_object = PerfilSuscripcion.objects.get(perfil_id=perfil_object.id, estado_suscripcion='1')
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

def suscripcion_perfil(suscripcion) -> Perfil:
    registro_object = PerfilSuscripcion.objects.get(suscripcion=suscripcion)
    return Perfil.objects.get(pk=registro_object.perfil.id)