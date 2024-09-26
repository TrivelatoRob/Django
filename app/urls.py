from django.urls import path
from . import views


urlpatterns = [
    path('listar_produtos', views.listar_produtos),
    path('cadastrar_produtos', views.cadastrar_produto),
    path('deletar_produtos', views.deletar_produto),
    path('atualizar_produtos', views.atualizar_produto)
]