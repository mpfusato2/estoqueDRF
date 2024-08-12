from rest_framework import serializers

from .views import Produto

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = (
            'id',            
            'descricao',            
            'criacao',
            'atualizacao',
            'ativo'
        )

