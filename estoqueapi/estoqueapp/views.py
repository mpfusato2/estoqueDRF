from rest_framework import generics
from rest_framework.generics import get_object_or_404

from rest_framework import viewsets
from rest_framework import mixins

from .models import Produto, Cliente
from .serializers import ProdutoSerializer, ClienteSerializer
     
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


