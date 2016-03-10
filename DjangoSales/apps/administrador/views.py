from django.shortcuts import render
from django.views.generic import TemplateView
from django.db.models import Sum, Avg
from .models import(
	Proveedor,
	Entradas,
	Inventario
	)

class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['provedores'] = Entradas.objects.filter(proveedor__nombre='Sabritas')
        context['suma'] = Entradas.objects.all().aggregate(Avg('precio'))
        return context

class SecondView(TemplateView):
    template_name = "second.html"