from rest_framework import serializers

from .views import Produto, Cliente, Estoque

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

class EstoqueSerializer(serializers.ModelSerializer):   

    class Meta:
        model = Estoque        
        fields = (
            'id',            
            'produto',
            'quantidade'
        )