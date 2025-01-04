from django.urls import path
from suscripciones.views import PlanesView, PlanIndividual, PlanOrganizacion, PagarView

url_patterns = [
    path('planes/', PlanesView.as_view(), name='planes'),
    path('planes/individual', PlanIndividual.as_view(), name='plan-individual'),
    path('planes/organizacion', PlanOrganizacion.as_view(), name='plan-organizacion'),
    path('pagar/', PagarView.as_view(), name='pantalla-compra')
]