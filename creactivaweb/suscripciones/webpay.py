import requests
import json
import random
from django.conf import settings
from suscripciones.models import *
from django.http import Http404

def crear_transaccion(suscripcion_id, monto):
    try:
        # obtener valor plan
        url = settings.WEBPAY_URL

        headers = {
            "Tbk-Api-Key-Id": settings.WEBPAY_ID,
            "Tbk-Api-Key-Secret": settings.WEBPAY_SECRET,
            "Content-Type": "application/json"
        }
        
        session_id = str(random.randrange(1000000,9999999))
        
        payload = {
            "buy_order": f"orden{str(suscripcion_id)}",
            "session_id": session_id,
            "amount": float(monto),
            "return_url": f"{settings.BASE_URL}suscripciones/webpay-respuesta"
        }

        res = requests.post(url, json=payload, headers=headers)
        print(res.text)
        respuesta = json.loads(res.text)
        Suscripcion.objects.filter(id=suscripcion_id).update(token_ws=respuesta['token'], session_id_transbank=session_id)
        
        return respuesta
    except Exception as e:
        print(f"Error: {e}; file: {e.__traceback__.tb_frame.f_code.co_filename}; line: {e.__traceback__.tb_lineno}; type: {e.__class__}")

def confirmar_transaccion(token):
    try:
        url = f"{settings.WEBPAY_URL}/{token}"
        headers = {
            "Tbk-Api-Key-Id": settings.WEBPAY_ID,
            "Tbk-Api-Key-Secret": settings.WEBPAY_SECRET,
            "Content-Type": "application/json"
        }

        res = requests.put(url, headers=headers)

        respuesta = json.loads(res.text)
        if res.status_code == 200:
            # REVISAR STATUS QUE IMPRIME Y MEJORAR EL CÓDIGO EN VIEWS
            print(respuesta['status'])
            return [respuesta['status'], respuesta['card_detail']['card_number'], respuesta['transaction_date'], respuesta['session_id']]
        elif res.status_code == 422:
            return ['ABORTED']
        else:
            return ['vacio']
    except Exception as e:
        print(f"Error: {e}; file: {e.__traceback__.tb_frame.f_code.co_filename}; line: {e.__traceback__.tb_lineno}; type: {e.__class__}")
        raise Http404
