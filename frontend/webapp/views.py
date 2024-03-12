from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

import datetime
import json
import logging

from webapp import config, models


def build_context(language="pt", **kwargs):
    text = None
    year = datetime.datetime.now().year

    if language == "pt":
        text = {
            "language": language,
            "lang": "pt-br",
            "title_prefix": "JBS Higiene & Limpeza",
            "description": "A JBS HIGIENE & LIMPEZA É ESPECIALIZADA NA PRODUÇÃO DE SABONETES, SABÕES EM BARRA, MASSA BASE E GLICERINA.",
            "copyright": f"JBS {year} - Todos os direitos reservados",
            "business_unit": "Uma unidade de negócios:",
            "where_we_are": "Onde estamos",
            "address": "Rodovia BR 153 KM 179 s/n <br/>Zone Rural    |    Lins/SP    |    CEP: 16400-900",
            "menu_labels": {
                "home": "Home",
                "our_history": "Nossa História",
                "our_business": "Nosso Negócio",
                "sustainability": "Sustentabilidade",
                "contact": "Contato",
                "privacy": "Termos e condições - Política de Privacidade",
                "cookies": "Definições de Cookies",
            },
            "menu_links": {
                "home": f"/{language}/",
                "our_history": f"/{language}/nossa-historia",
                "our_business": f"/{language}/nosso-negocio",
                "sustainability": f"/{language}/sustentabilidade",
                "contact": f"/{language}/contato",
                "privacy": f"/{language}/politica-de-privacidade",
                "pt": f"/pt",
                "en": f"/en",
                "es": f"/es",
            },
        }

    if language == "en":
        text = {
            "language": language,
            "lang": "en-us",
            "title_prefix": "JBS Hygiene & Cleaning's",
            "description": "JBS HYGIENE & CLEANING'S CORE BUSINESS IS PRODUCING SOAPS, BAR SOAP, SOAP NOODLE, AND GLYCERIN.",
            "copyright": f"JBS {year} - All rights reserved",
            "business_unit": "A JBS business unit",
            "where_we_are": "Where we are",
            "address": "Rodovia BR 153 KM 179 s/n <br/>Zone Rural    |    Lins/SP    |    CEP: 16400-900",
            "menu_labels": {
                "home": "Home",
                "our_history": "Our History",
                "our_business": "Our Business",
                "sustainability": "Sustainability",
                "contact": "Contact",
                "privacy": "Privacy Policy",
                "cookies": "Cookie Settings",
            },
            "menu_links": {
                "home": f"/{language}/",
                "our_history": f"/{language}/our-history",
                "our_business": f"/{language}/our-business",
                "sustainability": f"/{language}/sustainability",
                "contact": f"/{language}/contact",
                "privacy": f"/{language}/privacy-policy",
                "pt": f"/pt",
                "en": f"/en",
                "es": f"/es",
            },
        }

    if language == "es":
        text = {
            "language": language,
            "lang": "es",
            "title_prefix": "JBS Higiene Y Limpieza",
            "description": "JBS HIGIENE Y LIMPIEZA SE ESPECIALIZA EN LA PRODUCCIÓN DE JABONES DE TOCADOR, JABONES BARRA, MASA BASE Y GLICERINA.",
            "copyright": f"JBS {year} - Todos los derechos reservados",
            "business_unit": "Una Unidad de negocios",
            "where_we_are": "Dónde estamos",
            "address": "Rodovia BR 153 KM 179 s/n <br/>Zone Rural    |    Lins/SP    |    CEP: 16400-900",
            "menu_labels": {
                "home": "Home",
                "our_history": "Nuestra Historia",
                "our_business": "Nuestro Negocio",
                "sustainability": "Sustentabilidad",
                "contact": "Contacto",
                "privacy": "Términos y condiciones - Política de privacidad",
                "cookies": "Configuración de cookies",
            },
            "menu_links": {
                "home": f"/{language}/",
                "our_history": f"/{language}/nuestra-historia",
                "our_business": f"/{language}/nuestro-negocio",
                "sustainability": f"/{language}/sustentabilidad",
                "contact": f"/{language}/contacto",
                "privacy": f"/{language}/politica-de-privacidad",
                "pt": f"/pt",
                "en": f"/en",
                "es": f"/es",
            },
        }

    base_context = {
        "config": config,
        "text": text,
    }
    return {**base_context, **kwargs}


def index(request, language="pt"):
    context = build_context(language)
    return HttpResponse(render(request, f"{language}/home.html", context))


def history(request, language="pt"):
    context = build_context(language)
    return HttpResponse(render(request, f"{language}/history.html", context))


def business(request, language="pt"):
    context = build_context(language)
    return HttpResponse(render(request, f"{language}/business.html", context))


def sustainability(request, language="pt"):
    context = build_context(language)
    return HttpResponse(render(request, f"{language}/sustainability.html", context))


def contact(request, language="pt"):
    context = build_context(language)
    return HttpResponse(render(request, f"{language}/contact.html", context))


def privacy(request, language="pt"):
    context = build_context(language)
    return HttpResponse(render(request, f"{language}/privacy.html", context))


@csrf_exempt
def mail(request):

    # get data
    object = json.loads(request.body)
    logging.debug(object)
    nome = object["name"]
    email = object["email"]
    telefone = object["phone"]
    mensagem = object["message"]
    message = """Dados informados no formulario de contato:
- Nome: %s
- Email: %s
- Telefone: %s
- Mensagem:
%s""" % (
        nome,
        email,
        telefone,
        mensagem,
    )

    logging.debug(message)

    status = send_mail(
        subject="[JBS H&L] Contact Form",
        from_email=config.EMAIL_FROM,
        recipient_list=[config.EMAIL_TO],
        message=message,
        fail_silently=False,
    )

    logging.debug("status = %d" % status)
    return HttpResponse("")
