from django.urls import path
from . import views

urlpatterns = [
    path('', views.mostrar_carrinho, name='mostrar_carrinho'),
    path('adicionar/<int:produto_id>/', views.adicionar_ao_carrinho, name='adicionar_ao_carrinho'),
    path('remover/<int:item_id>/', views.remover_do_carrinho, name='remover_do_carrinho'),
    path('alterar_quantidade/<int:item_id>/', views.alterar_quantidade, name='alterar_quantidade'),
]

from django.urls import include, path

urlpatterns = [
    # outras rotas
    path('carrinho/', include('carrinho.urls')),
]
