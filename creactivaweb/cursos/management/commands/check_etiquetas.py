# CONFIGURACIÓN CRONTAB
# 0 0 * * * source /Users/klau/.virtualenvs/creactivaweb/bin/activate && cd /Users/klau/Documents/javier/creactiva/creactivaweb && python manage.py check_suscripciones >> /var/log/django_log.log 2>&1
# <cron_timer> source <ruta archivo activate del venv> && cd <ruta manage.py> && python manage.py <nombre archivo del script .py> >> <ruta archivo log> 2>&1
# RUTA PRODUCCIÓN (probada)
# source /home/creacti3/virtualenv/creactivaweb/3.11/bin/activate && cd /home/creacti3/creactivaweb && python manage.py check_suscripciones >> ~/logs/check_suscripciones.log 2>&1

from cursos.models import Capitulo, Curso
from django.db.models import Q
from django.core.management.base import BaseCommand, CommandError
from django.utils.timezone import now

class Command(BaseCommand):
    def handle(self, *args, **options):
        try:
            data_cursos = Curso.objects.filter(~Q(fecha_lanzamiento=None))
            data_capitulos = Capitulo.objects.filter(~Q(fecha_lanzamiento=None))
            for curso in data_cursos:
                if now() > curso.fecha_lanzamiento:
                    curso.etiqueta_promocional = '0'
                    curso.save()
                    self.stdout.write(f'{now()} FECHA LANZAMIENTO:{curso.fecha_lanzamiento} NUEVA ETIQUETA: {curso.etiqueta_promocional}')
            for capitulo in data_capitulos:
                if now() > capitulo.fecha_lanzamiento:
                    capitulo.etiqueta_promocional = '0'
                    capitulo.save()
                    self.stdout.write(f'{now()} FECHA LANZAMIENTO:{capitulo.fecha_lanzamiento} NUEVA ETIQUETA: {capitulo.etiqueta_promocional}')
        except CommandError as e:
            self.stderr.write(self.style.ERROR_OUTPUT(f"ERROR DE EJECUCIÓN. Error: {e}; file: {e.__traceback__.tb_frame.f_code.co_filename}; line: {e.__traceback__.tb_lineno}; type: {e.__class__}"))    
        except Curso.DoesNotExist as e:
            self.stderr.write(self.style.ERROR_OUTPUT(f"ERROR EN LA CONSULTA. Error: {e}; file: {e.__traceback__.tb_frame.f_code.co_filename}; line: {e.__traceback__.tb_lineno}; type: {e.__class__}"))    
        except Capitulo.DoesNotExist as e:
            self.stderr.write(self.style.ERROR_OUTPUT(f"ERROR EN LA CONSULTA. Error: {e}; file: {e.__traceback__.tb_frame.f_code.co_filename}; line: {e.__traceback__.tb_lineno}; type: {e.__class__}"))    
        except Exception as e:
            self.stderr.write(self.style.ERROR_OUTPUT(f"LA OPERACIÓN FALLÓ. Error: {e}; file: {e.__traceback__.tb_frame.f_code.co_filename}; line: {e.__traceback__.tb_lineno}; type: {e.__class__}"))
