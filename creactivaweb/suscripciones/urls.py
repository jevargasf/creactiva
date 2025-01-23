from django.urls import path
from suscripciones.views import PlanesView, PlanIndividual, PlanOrganizacion, PagarView, SolicitudOrganizacionView

urlpatterns = [
    path('planes/', PlanesView.as_view(), name='planes'),
    path('planes/individual', PlanIndividual.as_view(), name='plan-individual'),
    path('planes/organizacion', SolicitudOrganizacionView.as_view(), name='solicitud-organizacion'),
    path('pagar/', PagarView.as_view(), name='pantalla-compra')
]