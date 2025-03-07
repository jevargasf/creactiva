# CONFIGURACIÓN CRONTAB
# 0 0 * * * source /Users/klau/.virtualenvs/creactivaweb/bin/activate && cd /Users/klau/Documents/javier/creactiva/creactivaweb && python manage.py check_suscripciones >> /var/log/django_log.log 2>&1
# <cron_timer> source <ruta archivo activate del venv> && cd <ruta manage.py> && python manage.py <nombre archivo del script .py> >> <ruta archivo log> 2>&1
# RUTA PRODUCCIÓN (probada)
# source /home/creacti3/virtualenv/creactivaweb/3.11/bin/activate && cd /home/creacti3/creactivaweb && python manage.py check_suscripciones >> ~/logs/check_suscripciones.log 2>&1

from django.core.management.base import BaseCommand, CommandError
from suscripciones.models import PerfilSuscripcion
from django.utils.timezone import now
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from main.utils import enviar_correo
class Command(BaseCommand):
    def handle(self, *args, **options):
        try:
            data = PerfilSuscripcion.objects.filter(estado_suscripcion='1')
            for a in data:
                if now() <= a.suscripcion.fecha_termino:
                    self.stdout.write(f"{now()} Vigente. E: {a.estado_suscripcion}")
                    user_object = User.objects.get(perfil_id=a.perfil_id)
                    correo_user = enviar_correo(
                        r_nombre=user_object.first_name,
                        r_email=user_object.email,
                        e_mail="no-reply@creactivaanimaciones.cl",
                        asunto="Tu suscripción a CreActiva Animaciones ha finalizado",
                        app="suscripciones",
                        archivo="suscripcion_caduca"
                    )
                    if correo_user == False:
                        self.stderr.write(self.style.ERROR_OUTPUT(f"NO SE PUDO ENVIAR EL CORREO."))   
                else:
                    a.estado_suscripcion = '0'
                    a.save()
                    self.stdout.write(f'{now()} SUSCRIPCIÓN CADUCA:{a.suscripcion.id} ESTADO: {a.estado_suscripcion}')
            self.stdout.write(self.style.SUCCESS('TAREA COMPLETADA CON ÉXITO.'))
        except CommandError as e:
            self.stderr.write(self.style.ERROR_OUTPUT(f"ERROR DE EJECUCIÓN. Error: {e}; file: {e.__traceback__.tb_frame.f_code.co_filename}; line: {e.__traceback__.tb_lineno}; type: {e.__class__}"))    
        except Exception as e:
            self.stderr.write(self.style.ERROR_OUTPUT(f"LA OPERACIÓN FALLÓ. Error: {e}; file: {e.__traceback__.tb_frame.f_code.co_filename}; line: {e.__traceback__.tb_lineno}; type: {e.__class__}"))
