from django.shortcuts import render
from django.views.generic import TemplateView


class Index(TemplateView):
    template_name ='index.html'

class Quem_somos(TemplateView):
    template_name = 'quem-somos.html'

class Contato(TemplateView):
    template_name = 'contato.html'

class Parceiro(TemplateView):
    template_name = 'parceiro.html'

class Acessar_conta(TemplateView):
    template_name = 'acessar_conta.html'

class Relatorio(TemplateView):
    template_name = 'relatorio.html'