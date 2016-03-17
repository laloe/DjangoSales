from django.shortcuts import render
from django.views.generic import TemplateView
<<<<<<< HEAD
=======
from django.db.models import Sum, Avg
>>>>>>> isra/dev
from .models import(
	Proveedor,
	Entradas,
	Inventario
	)

class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
<<<<<<< HEAD
        context['proveedores'] = Proveedor.objects.all()
        return context

class SecondView(TemplateView):
    template_name = "second.html"
=======
        context['provedores'] = Entradas.objects.filter(proveedor__nombre='Sabritas')
        context['suma'] = Entradas.objects.all().aggregate(Avg('precio'))
        return context

class EntradasView(TemplateView):
    template_name = "entradas.html"

    def get_context_data(self, **kwargs):
        context = super(EntradasView, self).get_context_data(**kwargs)
        context['entradas'] = Entradas.objects.all()
        return context
>>>>>>> isra/dev
