from django.urls import path
from suscripciones.views import PlanesView, PlanIndividual, PlanOrganizacion, PagarView, SolicitudOrganizacionView, ElegirOrganizacionView, SuscripcionOrganizacionView, DetallePlan

urlpatterns = [
    path('suscripciones/planes/', PlanesView.as_view(), name='planes'),
    path('suscripciones/planes/individual', PlanIndividual.as_view(), name='plan-individual'),
    path('suscripciones/planes/individual/<id_plan>', DetallePlan.as_view(), name='detalle-plan'),
    path('suscripciones/planes/organizacion', SolicitudOrganizacionView.as_view(), name='solicitud-organizacion'),
    path('suscripciones/individual/pagar/', PagarView.as_view(), name='pantalla-compra'),
    path('suscripciones/organizacion/elegir', ElegirOrganizacionView.as_view(), name='elegir-organizacion'),
    path('suscripciones/organizacion/registrar/<id_org>', SuscripcionOrganizacionView.as_view(), name='suscribir-organizacion')
]