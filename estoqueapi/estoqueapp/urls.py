from django.urls import path

from rest_framework.routers import SimpleRouter

from .views import (ProdutoListCreateAPI, ProdutoUpdateDeleteAPI, ClienteViewSet, EstoqueViewSet)

router = SimpleRouter()
router.register('clientes', ClienteViewSet)
router.register('estoques', EstoqueViewSet)

urlpatterns = [
    path('produtos/', ProdutoListCreateAPI.as_view(), name='produtos'),
    path('produtos/<int:pk>/', ProdutoUpdateDeleteAPI.as_view(), name='produto')   
]