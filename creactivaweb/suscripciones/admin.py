from django.contrib import admin
from suscripciones.models import *

# Register your models here.

class CodigoPromocionalAdmin(admin.ModelAdmin):
    pass

class PerfilCodigoAdmin(admin.ModelAdmin):
    pass
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
admin.site.register(CodigoPromocional, CodigoPromocionalAdmin)
admin.site.register(PerfilCodigo, PerfilCodigoAdmin)