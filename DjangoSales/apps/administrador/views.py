from django.shortcuts import render
from django.views.generic import TemplateView
from .models import(
	Proveedor,
	Entradas,
	Inventario
	)

class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['proveedores'] = Proveedor.objects.all()
        return context

class SecondView(TemplateView):
    template_name = "second.html"