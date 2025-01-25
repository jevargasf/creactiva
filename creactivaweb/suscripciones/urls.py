from django.urls import path
from suscripciones.views import PlanesView, PlanIndividual, PlanOrganizacion, PagarView, SolicitudOrganizacionView, ElegirOrganizacionView, SuscripcionOrganizacionView

urlpatterns = [
    path('planes/', PlanesView.as_view(), name='planes'),
    path('planes/individual', PlanIndividual.as_view(), name='plan-individual'),
    path('planes/organizacion', SolicitudOrganizacionView.as_view(), name='solicitud-organizacion'),
    path('pagar/', PagarView.as_view(), name='pantalla-compra'),
    path('suscripciones/organizacion/elegir', ElegirOrganizacionView.as_view(), name='elegir-organizacion'),
    path('suscripciones/organizacion/registrar', SuscripcionOrganizacionView.as_view(), name='suscribir-organizacion')
]