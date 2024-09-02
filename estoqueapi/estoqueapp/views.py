from rest_framework import generics
from rest_framework.generics import get_object_or_404

from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Produto, Cliente, Estoque
from .serializers import ProdutoSerializer, ClienteSerializer, EstoqueSerializer 
     
'''
API de Produto usado os tipos de forma separada 
'''
# Classe responsavel por listar e inserir produtos
class ProdutoListCreateAPI(generics.ListCreateAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

# Classe responsavel por atualizar e excluir produtos
class ProdutoUpdateDeleteAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

'''
API de Cliente
'''  
class ClienteViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
   ):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

'''
API de Estoque

'''    
class EstoqueViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
   ):
    queryset = Estoque.objects.all()
    serializer_class = EstoqueSerializer    



