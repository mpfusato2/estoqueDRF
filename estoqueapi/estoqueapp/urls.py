from django.urls import path

from rest_framework.routers import SimpleRouter

from .views import (ProdutoListCreateAPI, ProdutoUpdateDeleteAPI, ClienteViewSet)

router = SimpleRouter()
router.register('clientes', ClienteViewSet)

urlpatterns = [
    path('produtos/', ProdutoListCreateAPI.as_view(), name='produtos'),
    path('produtos/<int:pk>/', ProdutoUpdateDeleteAPI.as_view(), name='produto'),    
]