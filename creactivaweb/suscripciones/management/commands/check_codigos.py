# CONFIGURACIÓN CRONTAB
# 0 0 * * * source /Users/klau/.virtualenvs/creactivaweb/bin/activate && cd /Users/klau/Documents/javier/creactiva/creactivaweb && python manage.py check_suscripciones >> /var/log/django_log.log 2>&1
# <cron_timer> source <ruta archivo activate del venv> && cd <ruta manage.py> && python manage.py <nombre archivo del script .py> >> <ruta archivo log> 2>&1
# RUTA PRODUCCIÓN (probada)
# source /home/creacti3/virtualenv/creactivaweb/3.11/bin/activate && cd /home/creacti3/creactivaweb && python manage.py check_suscripciones >> ~/logs/check_suscripciones.log 2>&1

from suscripciones.models import CodigoPromocional
from django.core.management.base import BaseCommand, CommandError
from django.utils.timezone import now

class Command(BaseCommand):
    def handle(self, *args, **options):
        try:
            data = CodigoPromocional.objects.filter(estado_codigo='1')
            for codigo in data:
                if now() > codigo.fecha_caducidad:
                    codigo.estado_codigo = '0'
                    codigo.save()
                    self.stdout.write(f'{now()} CÓDIGO CADUCO:{codigo.codigo} ESTADO: {codigo.estado_codigo}')
                else:
                    self.stdout.write(f'{now()} CÓDIGO VIGENTE:{codigo.codigo} ESTADO: {codigo.estado_codigo}')
        except CommandError as e:
            self.stderr.write(self.style.ERROR_OUTPUT(f"ERROR DE EJECUCIÓN. Error: {e}; file: {e.__traceback__.tb_frame.f_code.co_filename}; line: {e.__traceback__.tb_lineno}; type: {e.__class__}"))    
        except Exception as e:
            self.stderr.write(self.style.ERROR_OUTPUT(f"LA OPERACIÓN FALLÓ. Error: {e}; file: {e.__traceback__.tb_frame.f_code.co_filename}; line: {e.__traceback__.tb_lineno}; type: {e.__class__}"))
