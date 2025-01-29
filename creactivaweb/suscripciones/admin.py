from django.contrib import admin
from suscripciones.models import Suscripcion, CursosSuscripcion, PerfilSuscripcion, SolicitudOrganizacion, Planes

# Register your models here.
class SuscripcionAdmin(admin.ModelAdmin):
    pass

class CursosSuscripcionAdmin(admin.ModelAdmin):
    pass

class PerfilSuscripcionAdmin(admin.ModelAdmin):
    pass

class SolicitudOrganizacionAdmin(admin.ModelAdmin):
    pass

class PlanesAdmin(admin.ModelAdmin):
    pass

admin.site.register(Suscripcion, SuscripcionAdmin)
admin.site.register(CursosSuscripcion, CursosSuscripcionAdmin)
admin.site.register(PerfilSuscripcion, PerfilSuscripcionAdmin)
admin.site.register(SolicitudOrganizacion, SolicitudOrganizacionAdmin)
admin.site.register(Planes, PlanesAdmin)