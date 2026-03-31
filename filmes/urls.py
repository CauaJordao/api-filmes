from django.urls import path
from . import views

urlpatterns = [
    path('filmes/', views.listar_filmes), 
    path('filmes/genero/<str:genero>/', views.filmes_por_genero), 
]