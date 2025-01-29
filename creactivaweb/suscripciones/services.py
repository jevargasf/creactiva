from suscripciones.models import SolicitudOrganizacion, Planes

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