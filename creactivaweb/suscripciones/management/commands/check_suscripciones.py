# CONFIGURACIÓN CRONTAB
# 0 0 * * * source /Users/klau/.virtualenvs/creactivaweb/bin/activate && cd /Users/klau/Documents/javier/creactiva/creactivaweb && python manage.py check_suscripciones >> /var/log/django_log.log 2>&1
# <cron_timer> source <ruta archivo activate del venv> && cd <ruta manage.py> && python manage.py <nombre archivo del script .py> >> <ruta archivo log> 2>&1

from django.core.management.base import BaseCommand, CommandError
from suscripciones.models import Suscripcion
from django.utils.timezone import now

class Command(BaseCommand):
    def handle(self, *args, **options):
        try:
            data = Suscripcion.objects.filter(estado_suscripcion='1')
            for suscripcion in data:
                if now() <= suscripcion.fecha_termino:
                    print(now(), "Vigente.", suscripcion.estado_suscripcion)
                else:
                    suscripcion.estado_suscripcion = '0'
                    suscripcion.save()
                    print(f'{now()} SUSCRIPCIÓN CADUCA:{suscripcion.id} ESTADO: {suscripcion.estado_suscripcion}')
        
            self.stdout.write(self.style.SUCCESS('OPERACIÓN REALIZADA CON ÉXITO.'))
        except:
            print("LA OPERACIÓN FALLÓ.")
            self.stderr.write(self.style.ERROR_OUTPUT('LA OPERACIÓN FALLÓ.'))