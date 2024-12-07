from django.contrib import admin
from cursos.models import Etiqueta, Idioma, MaterialesComplementario, Autor, Curso, Capitulo, EstadoCapitulo, Visualizacion

class EtiquetaAdmin(admin.ModelAdmin):
    pass

class IdiomaAdmin(admin.ModelAdmin):
    pass
class MaterialComplementarioAdmin(admin.ModelAdmin):
    pass

class AutorAdmin(admin.ModelAdmin):
    pass

class CursoAdmin(admin.ModelAdmin):
    pass
class CapituloAdmin(admin.ModelAdmin):
    pass

class EstadoCapituloAdmin(admin.ModelAdmin):
    pass

class VisualizacionAdmin(admin.ModelAdmin):
    pass

admin.site.register(Etiqueta, EtiquetaAdmin)
admin.site.register(Idioma, IdiomaAdmin)
admin.site.register(MaterialesComplementario, MaterialComplementarioAdmin)
admin.site.register(Autor, AutorAdmin)
admin.site.register(Curso, CursoAdmin)
admin.site.register(Capitulo, CapituloAdmin)
admin.site.register(EstadoCapitulo, EstadoCapituloAdmin)
admin.site.register(Visualizacion, VisualizacionAdmin)