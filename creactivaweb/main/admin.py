from django.contrib import admin
from main.models import Perfil, Contacto

class PerfilAdmin(admin.ModelAdmin):
    pass

class ContactoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Perfil, PerfilAdmin)
admin.site.register(Contacto, ContactoAdmin)

admin.site.site_header = "Creactiva Animaciones"
admin.site.index_title = f"Bienvenido al portal de administración de {admin.site.site_header}"