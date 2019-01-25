"""Morpheus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path
from rest_framework import routers
from ComInv.api.viewsets import CommercialInvoiceViewSet
from Clientes.api.viewsets import ClientesViewSet
from Materiais.api.viewsets import MateriaisViewSet
from Pacotes.api.viewsets import PacotesViewSet

router = routers.DefaultRouter()
router.register(r'cominv', CommercialInvoiceViewSet),
router.register(r'clientes', ClientesViewSet)
router.register(r'produtos', MateriaisViewSet)
router.register(r'pacotes', PacotesViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
