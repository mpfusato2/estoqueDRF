from rest_framework import serializers

from .views import Produto, Cliente, Pedido

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = (
            'id',            
            'descricao',            
            'criacao',
            'atualizacao',
            'ativo',
            'valor'
        )

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = (
            'id',            
            'nome',            
            'criacao',
            'atualizacao',
            'ativo'            
        )

class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = (
            'id',            
            'produto',            
            'quantidade',
            'valor_total',
            'ativo'            
        )