from django.urls import path
from . import views


urlpatterns = [
    path('produtos/', views.listar_produtos),
    path('cadastrar', views.cadastrar_produto)
]