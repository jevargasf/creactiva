from django.urls import path
from suscripciones.views import *

urlpatterns = [
    path('suscripciones/planes/', PlanesView.as_view(), name='planes'),
    path('suscripciones/planes/individual', PlanIndividual.as_view(), name='plan-individual'),
    path('suscripciones/planes/individual/<id_plan>', DetallePlan.as_view(), name='detalle-plan'),
    path('suscripciones/webpay/<id_plan>', PagarView.as_view(), name='pantalla-pagar'),
    path('suscripciones/webpay-respuesta', RespuestaWebpayView.as_view(), name='respuesta-webpay'),
    path('suscripciones/planes/organizacion', SolicitudOrganizacionView.as_view(), name='solicitud-organizacion'),
    path('suscripciones/organizacion/elegir', ElegirOrganizacionView.as_view(), name='elegir-organizacion'),
    path('suscripciones/organizacion/registrar/<id_org>', SuscripcionOrganizacionView.as_view(), name='suscribir-organizacion')
]