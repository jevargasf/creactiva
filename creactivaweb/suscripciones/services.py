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

def suscripcion_usuario(user):    
    # validar si tiene una suscripción vigente
    try:
        user_object = User.objects.get(username=user)
        perfil_object = Perfil.objects.get(user_id=user_object.id)
        registro_object = PerfilSuscripcion.objects.filter(perfil=perfil_object).order_by('-id')[0] 
        suscripcion_object = Suscripcion.objects.get(pk=registro_object.suscripcion_id, estado_suscripcion='2')
        return suscripcion_object
    except Exception as e:
        print(f"Error: {e}; line: {e.__traceback__.tb_lineno}; type: {e.__class__}")
