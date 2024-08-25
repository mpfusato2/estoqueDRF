from rest_framework import serializers

from .views import Produto, Cliente

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

