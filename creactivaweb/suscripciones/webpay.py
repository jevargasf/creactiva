import requests
import json
import random
from django.conf import settings
from suscripciones.models import *

# MODELO ORDEN DE COMPRA EJEMPLO
# token_ws. listo
# tarjeta. listo
# fecha_transbank. listo
# estado_transbank. listo
# suma. listo
# direccion. no aplica
# observaciones. no aplica
# fecha. listo
# comuna_id. no aplica
# estado_id. listo
# users_metadata_id. listo, pero desde fk