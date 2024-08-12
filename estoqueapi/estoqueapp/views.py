from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Produto
from .serializers import ProdutoSerializer

class ProdutoApiView(APIView):
    """
    API de Produtos
    """

    def get(self, request):
        produtos = Produto.objects.all()
        serializer = ProdutoSerializer(produtos, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ProdutoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

