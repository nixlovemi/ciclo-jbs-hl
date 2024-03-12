from django.urls import path

from . import views

urlpatterns = [
    # common
    path("", views.index),
    path("<slug:language>/", views.index),
    # pt
    path("<slug:language>/nossa-historia", views.history),
    path("<slug:language>/nosso-negocio", views.business),
    path("<slug:language>/sustentabilidade", views.sustainability),
    path("<slug:language>/contato", views.contact),
    path("<slug:language>/politica-de-privacidade", views.privacy),
    # en
    path("<slug:language>/our-history", views.history),
    path("<slug:language>/our-business", views.business),
    path("<slug:language>/sustainability", views.sustainability),
    path("<slug:language>/contact", views.contact),
    path("<slug:language>/privacy-policy", views.privacy),
    # es
    path("<slug:language>/nuestra-historia", views.history),
    path("<slug:language>/nuestro-negocio", views.business),
    path("<slug:language>/sustentabilidad", views.sustainability),
    path("<slug:language>/contacto", views.contact),
    path("<slug:language>/politica-de-privacidad", views.privacy),
]
