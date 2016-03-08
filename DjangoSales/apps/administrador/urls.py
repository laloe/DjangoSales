from django.conf.urls import url, include
from apps.administrador import views

urlpatterns = [   
   url(r'^$', views.IndexView, name='index'),
]