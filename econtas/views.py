from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Banner, Pagamento, Boleto

class Index(TemplateView):
    template_name ='index.html'

    def get_context_data(self, **kwargs):
        ctx = super(Index, self).get_context_data(**kwargs)
        ctx['banners'] = Banner.objects.all()
        return ctx

class Relatorio(TemplateView):
    template_name = 'relatorio.html'

    def get_context_data(self, **kwargs):
        ctx = super(Relatorio, self).get_context_data(**kwargs)
        ctx['boletos'] = Boleto.objects.all()
        return ctx

class Quem_somos(TemplateView):
    template_name = 'quem-somos.html'

class Contato(TemplateView):
    template_name = 'contato.html'

class Parceiro(TemplateView):
    template_name = 'parceiro.html'

class Acessar_conta(TemplateView):
    template_name = 'acessar_conta.html'
