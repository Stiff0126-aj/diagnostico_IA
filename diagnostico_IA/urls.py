
from django.urls import path
from . import views

urlpatterns = [
    path('formulario_predecir/', views.formulario_diagnostico, name='formulario'),
]
