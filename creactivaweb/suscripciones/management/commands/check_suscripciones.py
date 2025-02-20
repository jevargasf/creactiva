# CONFIGURACIÓN CRONTAB
# 0 0 * * * source /Users/klau/.virtualenvs/creactivaweb/bin/activate && cd /Users/klau/Documents/javier/creactiva/creactivaweb && python manage.py check_suscripciones >> /var/log/django_log.log 2>&1
# <cron_timer> source <ruta archivo activate del venv> && cd <ruta manage.py> && python manage.py <nombre archivo del script .py> >> <ruta archivo log> 2>&1
# RUTA PRODUCCIÓN (probada)
# source /home/creacti3/virtualenv/creactivaweb/3.11/bin/activate && cd /home/creacti3/creactivaweb && python manage.py check_suscripciones >> ~/logs/check_suscripciones.log 2>&1

from django.core.management.base import BaseCommand, CommandError
from suscripciones.models import PerfilSuscripcion
from django.utils.timezone import now

class Command(BaseCommand):
    def handle(self, *args, **options):
        try:
            data = PerfilSuscripcion.objects.filter(estado_suscripcion='1')
            for a in data:
                if now() <= a.suscripcion.fecha_termino:
                    self.stdout.write(f"{now()} Vigente. E: {a.estado_suscripcion}")
                else:
                    a.estado_suscripcion = '0'
                    a.save()
                    self.stdout.write(f'{now()} SUSCRIPCIÓN CADUCA:{a.suscripcion.id} ESTADO: {a.estado_suscripcion}')
            self.stdout.write(self.style.SUCCESS('TAREA COMPLETADA CON ÉXITO.'))
        except Exception as e:
            self.stderr.write(self.style.ERROR_OUTPUT(f"LA OPERACIÓN FALLÓ. Error: {e}; file: {e.__traceback__.tb_frame.f_code.co_filename}; line: {e.__traceback__.tb_lineno}; type: {e.__class__}"))
