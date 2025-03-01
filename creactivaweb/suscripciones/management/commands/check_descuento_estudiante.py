from main.models import Perfil
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    def handle(self, *args, **options):
        try:
            data = Perfil.objects.filter(estado_codigo='1')
            for perfil in data:
                if perfil.tipo_descuento == '1':
                    perfil.tipo_descuento = '0'
                    perfil.descuento_creactiva = False
                    perfil.save()
                    self.stdout.write(f'USUARIO: {perfil.user.username} CÓDIGO ESTUDIANTE CADUCO. ESTADO: {perfil.tipo_descuento}, DESCUENTO: {perfil.descuento_creactiva}')
                else:
                    continue
        except CommandError as e:
            self.stderr.write(self.style.ERROR_OUTPUT(f"ERROR DE EJECUCIÓN. Error: {e}; file: {e.__traceback__.tb_frame.f_code.co_filename}; line: {e.__traceback__.tb_lineno}; type: {e.__class__}"))    
        except Exception as e:
            self.stderr.write(self.style.ERROR_OUTPUT(f"LA OPERACIÓN FALLÓ. Error: {e}; file: {e.__traceback__.tb_frame.f_code.co_filename}; line: {e.__traceback__.tb_lineno}; type: {e.__class__}"))
