from suscripciones.models import *
from django.db.models import F, Q

def get_solicitudes():
    data = SolicitudOrganizacion.objects.all()
    organizaciones = []
    for d in data:
        organizaciones.append((d.id, (f'Organizaci贸n: {d.nombre_organizacion} | Nombre: {d.usuario.first_name} {d.usuario.last_name} | Correo: {d.usuario}')))
    return organizaciones

def get_planes():
    data = Planes.objects.all()
    planes = []
    for p in data:
        planes.append((p.id, p.nombre))
    return planes

def planes_montos_mensuales():
    data = Planes.objects.filter(~Q(pk=7)).annotate(monto_mensual=F('monto')/F('duracion'))
    return data

def suscripcion_activa(user):    
    try:
        user_object = User.objects.get(username=user)
        perfil_object = Perfil.objects.get(user_id=user_object.id)
        if perfil_object.codigo[0] == '1':
            registro_object = PerfilSuscripcion.objects.get(perfil_id=perfil_object.id, estado_suscripcion='1')
            if registro_object:
                suscripcion_object = Suscripcion.objects.get(pk=registro_object.suscripcion_id, numero_usuarios=1)
                if suscripcion_object:
                    return suscripcion_object
                else:
                    return None
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

def check_descuento(user_id):
    perfil_object = Perfil.objects.get(user_id=user_id)
    return perfil_object.descuento_creactiva

def validar_codigo(codigo):
    try:
        # C脫DIGO EXISTE Y EST脕 ACTIVO
        consulta = CodigoPromocional.objects.get(codigo=codigo, estado_codigo='1')
        return consulta
    except Exception as e:
        print(f"Error: {e}; file: {e.__traceback__.tb_frame.f_code.co_filename}; line: {e.__traceback__.tb_lineno}; type: {e.__class__}")
        return None
    
def stock_codigo():
    pass

def conseguir_codigo_usado(perfil: Perfil) -> CodigoPromocional:
    try:
        # BUSCA UN CÓDIGO REGISTRADO PARA EL USUARIO Y QUE NO HAYA USADO
        perfil_codigo_object = PerfilCodigo.objects.get(perfil=perfil, estado_uso_codigo='0')
        # SI ESTÁ VIGENTE, LE PERMITE USARLO
        if perfil_codigo_object.codigo.estado_codigo == '1':
            # DEVUELVE EL OBJETO CÓDIGO
            return perfil_codigo_object.codigo
        else:
            return None
    except Exception as e:
        print(f"Error: {e}; file: {e.__traceback__.tb_frame.f_code.co_filename}; line: {e.__traceback__.tb_lineno}; type: {e.__class__}")
        if perfil.descuento_creactiva == True:
            print("Error controlado: Usuario es estudiante o pueblo originario.")
            return True
        else:
            print("Error no controlado: Comportamiento inesperado.")
            return None