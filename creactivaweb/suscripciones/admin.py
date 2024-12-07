from django.contrib import admin
from suscripciones.models import Suscripcion, CursosSuscripcion, PerfilSuscripcion

# Register your models here.
class SuscripcionAdmin(admin.ModelAdmin):
    pass

class CursosSuscripcionAdmin(admin.ModelAdmin):
    pass

class PerfilSuscripcionAdmin(admin.ModelAdmin):
    pass

admin.site.register(Suscripcion, SuscripcionAdmin)
admin.site.register(CursosSuscripcion, CursosSuscripcionAdmin)
admin.site.register(PerfilSuscripcion, PerfilSuscripcionAdmin)