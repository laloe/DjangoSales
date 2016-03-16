from django.conf.urls import url, include
from .views import (
	IndexView,EntradasView
	)

urlpatterns = [   
   url(r'^$', IndexView.as_view(), name='index'),
   url(r'^entradas/$', EntradasView.as_view(), name='entradas'),
]