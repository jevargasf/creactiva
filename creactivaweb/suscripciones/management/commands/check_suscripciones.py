# CONFIGURACIÓN CRONTAB
# 0 0 * * * source /Users/klau/.virtualenvs/creactivaweb/bin/activate && cd /Users/klau/Documents/javier/creactiva/creactivaweb && python manage.py check_suscripciones >> /var/log/django_log.log 2>&1
# <cron_timer> source <ruta archivo activate del venv> && cd <ruta manage.py> && python manage.py <nombre archivo del script .py> >> <ruta archivo log> 2>&1
# RUTA PRODUCCIÓN
# source /home/creacti3/virtualenv/creactivaweb/3.11/bin/activate && cd /home/creacti3/creactivaweb python manage.py check_suscripciones.py >> /home/creacti3/logs/check_suscripciones.log 2>&1

from django.core.management.base import BaseCommand, CommandError
from suscripciones.models import PerfilSuscripcion
from django.utils.timezone import now

class Command(BaseCommand):
    def handle(self, *args, **options):
        try:
            data = PerfilSuscripcion.objects.filter(estado_suscripcion='1')
            for suscripcion in data:
                if now() <= suscripcion.fecha_termino:
                    self.stdout.write(now(), "Vigente.", suscripcion.estado_suscripcion)
                else:
                    suscripcion.estado_suscripcion = '0'
                    suscripcion.save()
                    self.stdout.write(f'{now()} SUSCRIPCIÓN CADUCA:{suscripcion.suscripcion.id} ESTADO: {suscripcion.estado_suscripcion}')

            self.stdout.write(self.style.SUCCESS('TAREA COMPLETADA CON ÉXITO.'))
        except Exception as e:
            self.stderr.write(self.style.ERROR_OUTPUT(f"LA OPERACIÓN FALLÓ. Error: {e}; file: {e.__traceback__.tb_frame.f_code.co_filename}; line: {e.__traceback__.tb_lineno}; type: {e.__class__}"))
