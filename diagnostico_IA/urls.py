
from django.urls import path
from . import views
from .views import home

urlpatterns = [
    path('', home, name='home'), 
    path('predecir/', views.predecir_epilepsia, name='predecir_epilepsia'),
    path('formulario_predecir/', views.formulario_diagnostico, name='formulario'),
]
