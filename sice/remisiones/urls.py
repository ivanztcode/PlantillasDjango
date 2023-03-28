from django.contrib import admin
from django.urls import path, include
from remisiones import views

urlpatterns = [
    path("",views.homeRemisiones,name="remisionesHome"),

]
