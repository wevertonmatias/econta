from django.contrib import admin
from django.urls import path,include
from econtas import urls as econtas_url
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', Index.as_view(), name="index"),
    path('quem_somos', Quem_somos.as_view(), name="quem_somos"),
    path('contato', Contato.as_view(), name="contato"),
    path('parceiro', Parceiro.as_view(), name="parceiro"),
    path('acessar_conta', Acessar_conta.as_view(), name="acessar_conta"),
    path('relatorio', Relatorio.as_view(), name="relatorio"),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)