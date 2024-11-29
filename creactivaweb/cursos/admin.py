from django.contrib import admin
from cursos.models import *

class EtiquetaAdmin(admin.ModelAdmin):
    pass

class MaterialComplementarioAdmin(admin.ModelAdmin):
    pass

class CursoAdmin(admin.ModelAdmin):
    pass

class CapituloAdmin(admin.ModelAdmin):
    pass

admin.site.register(Etiqueta, EtiquetaAdmin)
admin.site.register(MaterialComplementario, MaterialComplementarioAdmin)
admin.site.register(Curso, CursoAdmin)
admin.site.register(Capitulo, CapituloAdmin)