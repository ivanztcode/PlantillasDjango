from django.contrib import admin
from django.urls import path, include
from facturacion import views

urlpatterns = [
    path("",views.homeFacturacion,name="facturacionHome"),

]
