from suscripciones.models import SolicitudOrganizacion

def get_solicitudes():
    data = SolicitudOrganizacion.objects.all()
    organizaciones = []
    for d in data:
        organizaciones.append((d.id, (f'Organización: {d.nombre_organizacion} | Representante: {d.usuario}')))
    return organizaciones